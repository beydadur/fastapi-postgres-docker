resource "docker_network" "fastapi_network" {
    name = "fastapi_network"
}

resource "docker_volume" "pgdata_volume" {
    name = "pgdata_volume"
}

resource "docker_container" "db_container" {
    image = "postgres:16-alpine"
    name = "postgres-db"
    restart = "unless-stopped"
    ports {
        internal = 5432
        external = var.postgres_port
    }
    env = [ 
        "POSTGRES_USER=${var.postgres_user}",
        "POSTGRES_PASSWORD=${var.postgres_password}",
        "POSTGRES_DB=${var.postgres_db}"
    ]
    volumes { 
        volume_name = docker_volume.pgdata_volume.name 
        container_path = "/var/lib/postgresql/data"
    }

    networks_advanced { name = docker_network.fastapi_network.name }
    healthcheck {
        test = ["CMD-SHELL", "pg_isready -U ${var.postgres_user} -d ${var.postgres_db}"]
        interval = "5s"
        timeout = "3s"
        retries = 5
    }
}

locals {
  app_dir_win   = replace(abspath("${path.cwd}/backend/app"), "\\", "/")
  # Docker Desktop (önerilen)
  app_dir_linux = replace(lower(local.app_dir_win), "c:/", "/run/desktop/mnt/host/c/")
  # Eğer üstteki çalışmazsa bunu deneyin:
  # app_dir_linux = replace(lower(local.app_dir_win), "c:/", "/host_mnt/c/")
}

# FastAPI uygulamanız için Docker imajını oluşturmanız gerekmektedir.
# Dockerfile'ınızın bulunduğu dizinde 'docker build -t fastapi-app:latest ./backend' komutunu çalıştırabilirsiniz.
resource "docker_container" "api_container" {
    image = "fastapi-app:latest"
    name = "fastapi-api"
    ports {
        internal = 8000
        external = var.app_port
    }
    volumes {
        host_path      = local.app_dir_linux
        container_path = "/app/app"
        read_only      = false
    }
    env = ["DATABASE_URL=postgresql+psycopg://${var.postgres_user}:${var.postgres_password}@${docker_container.db_container.name}:5432/${var.postgres_db}"]
    networks_advanced {
        name = docker_network.fastapi_network.name
    }
    depends_on = [docker_container.db_container]
}
