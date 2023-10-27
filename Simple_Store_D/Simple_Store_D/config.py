
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    simple_store_database_hostname : str 
    simple_store_database_port : str 
    simple_store_database_password: str
    simple_store_database_name : str
    simple_store_database_username : str 
    simple_store_secret_key : str
    simple_store_default_email:str 
    simple_store_default_password:str
    simple_store_email: str 
    simple_store_password: str
    

    #we use pydantic to collect the necesary data from .env file 
    #for our schema and validated it 
    class Config:
        env_file = ".env"

settings_core = Settings()
