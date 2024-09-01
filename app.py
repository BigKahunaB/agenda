from decouple import config

# Asegúrate de que las variables se cargan correctamente desde el archivo .env
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_name = config('DB_NAME')
db_host = config('DB_HOST', default='localhost')  # Puedes definir valores predeterminados
db_port = config('DB_PORT', default='5432')

print(f"Conectando a la base de datos {db_name} como usuario {db_user} en {db_host}:{db_port}")