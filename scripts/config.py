import os
config_db = {
    "HOST": os.getenv("DB_HOST", "127.0.0.1"),
    "PORT": int(os.getenv("DB_PORT", "5432")),
    "USER": os.getenv("DB_USER", "user"),
    "PASSWORD": os.getenv("DB_PASSWORD", "root"),
    "DATABASE": os.getenv("DB_DATABASE", "dvf"),
}