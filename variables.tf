variable "postgres_user" {
    type = string
    description = "Postgres user"
    default = "admin"
}

variable "postgres_password" {
    type = string
    description = "Postgres password"
    default = "admin"
}

variable "postgres_db" {
    type = string
    description = "Postgres database name"
    default = "fastapi_postgres_docker"
}

variable "postgres_port" {
    type = number
    description = "Port for Postgres database"
    default = 5432
}

variable "app_port" {
    type = number
    description = "Port for FastAPI application"
    default = 8000
}

variable "app_host" {
    type = string
    description = "Host for FastAPI application"
    default = "0.0.0.0"
}