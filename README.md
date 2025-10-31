# FastAPI, PostgreSQL and Docker Project

Bu proje, FastAPI, PostgreSQL ve Docker kullanılarak oluşturulmuş bir REST API'sidir. Proje, Docker Compose ve Terraform olmak üzere iki farklı şekilde çalıştırılabilir.

This project is a REST API built using FastAPI, PostgreSQL, and Docker. The project can be run in two different ways: using Docker Compose or Terraform.

## Özellikler | Features

- FastAPI ile oluşturulmuş REST API
- PostgreSQL veritabanı
- Docker ile konteynerize edilmiş uygulama
- Docker Compose ile kolay kurulum ve çalıştırma
- Terraform ile altyapının kod olarak yönetimi (Infrastructure as Code)

---

- REST API created with FastAPI
- PostgreSQL database
- Application containerized with Docker
- Easy setup and execution with Docker Compose
- Infrastructure as Code management with Terraform

## Teknolojiler | Technologies

- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- Terraform
- SQLAlchemy

## Ön Gereksinimler | Prerequisites

- Docker
- Docker Compose
- Terraform

## Kurulum | Installation

1.  Projeyi klonlayın | Clone the project:

    ```bash
    git clone [https://github.com/beydadur/fastapi-postgres-docker.git](https://github.com/beydadur/fastapi-postgres-docker.git)
    cd fastapi-postgres-docker
    ```

2.  `.env` dosyasını oluşturun ve aşağıdaki değişkenleri kendi yapılandırmanıza göre düzenleyin | Create a `.env` file and edit the variables below according to your own configuration:

    ```env
    POSTGRES_USER=admin
    POSTGRES_PASSWORD=admin
    POSTGRES_DB=fastapi_postgres_docker
    POSTGRES_PORT=5432
    APP_PORT=8000
    APP_HOST=0.0.0.0
    ```

## Uygulamayı Çalıştırma | Running the Application

Uygulamayı çalıştırmak için iki farklı yöntem kullanabilirsiniz: Docker Compose veya Terraform.

You can use two different methods to run the application: Docker Compose or Terraform.

### Docker Compose ile Çalıştırma | Running with Docker Compose

Aşağıdaki komutu çalıştırarak uygulamayı başlatabilirsiniz | You can start the application by running the following command:

```bash
docker-compose up --build
Terraform ile Çalıştırma | Running with Terraform
FastAPI uygulamanız için Docker imajını oluşturun | Create the Docker image for your FastAPI application:

Bash

docker build -t fastapi-app:latest ./backend
Terraform'u başlatın | Initialize Terraform:

Bash

terraform init
Terraform planını oluşturun | Create a Terraform plan:

Bash

terraform plan
Terraform ile altyapıyı oluşturun | Create the infrastructure with Terraform:

Bash

terraform apply
API Endpoints
POST /api/items/: Yeni bir item oluşturur. | Creates a new item.

GET /api/items/: Tüm item'ları listeler. | Lists all items.

GET /api/items/{item_id}: Belirtilen ID'ye sahip item'ı getirir. | Retrieves the item with the specified ID.

DELETE /api/items/{item_id}: Belirtilen ID'ye sahip item'ı siler. | Deletes the item with the specified ID.

PUT /api/items/{item_id}: Belirtilen ID'ye sahip item'ı günceller. | Updates the item with the specified ID.
