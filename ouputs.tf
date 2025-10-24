output "api-endpoint" {
    description = "The endpoint URL for the FastAPI application"
    value = "http://${var.app_host}:${var.app_port}"
}

output "database_connection_info" {
    description = "Connection information for the Postgres database"
    value = "postgresql+psycopg2://${var.postgres_user}:${var.postgres_password}@localhost:${var.postgres_port}/${var.postgres_db}"
}