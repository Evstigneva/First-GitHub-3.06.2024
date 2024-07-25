from dataclasses import dataclass
class BaseConfig:
    def __new__(cls, *args, **kwargs):
        instance=super(BaseConfig, cls).__new__(cls)
        instance.debug=False
        instance.log_level = 'INFO'
        return instance
@dataclass
class EmailConfig(BaseConfig):
    smtp_server: str = 'smtp.gmail.com'
    smtp_port: int = 587
    username: str = 'boss_of_gym@gmail.com'
    password: None = '' 
@dataclass
class DatabaseConfig(BaseConfig):
    db_host: str = '127.0.0.1'
    db_port: int = 5432
    db_name: str = 'cookies'
    db_user: str = 'admin'
    db_password: str = 'admin'

database_config = DatabaseConfig()

print("Database Configuration:")
print(f"Host: {database_config.db_host}")
print(f"Port: {database_config.db_port}")
print(f"Database name: {database_config.db_name}")
print(f"User: {database_config.db_user}")
print(f"Password: {database_config.db_password}")
print(f"Debug: {database_config.debug}")
print(f"Logger: {database_config.log_level}")