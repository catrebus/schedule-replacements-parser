########################################################################################
#  Чтобы все заработало, этот файл нужно заполнить и переименовать в config_private.py #
########################################################################################

# BOT
BOT_TOKEN = 'your_bot_token'

# DATABASE
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_HOST = "your_db_host"
DB_PORT = 3306
DB_NAME = "your_db_name"

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# API
API_HOST = 'your_host'
API_PORT = 8001
API_KEY = 'your_api_key'


