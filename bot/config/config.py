import os

# BOT
BOT_TOKEN = os.getenv('REPLACEMENTS_BOT_TOKEN')

# DATABASE
DB_USER = os.getenv('BOT_DB_USER')
DB_PASSWORD = os.getenv('BOT_DB_PASSWORD')
DB_HOST = os.getenv('BOT_DB_HOST')
DB_PORT = int(os.getenv('BOT_DB_PORT'))
DB_NAME = os.getenv('BOT_DB_NAME')

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# API
API_HOST = os.getenv('BOT_API_HOST')
API_PORT = int(os.getenv('BOT_API_PORT'))
API_KEY = os.getenv('BOT_API_KEY')


