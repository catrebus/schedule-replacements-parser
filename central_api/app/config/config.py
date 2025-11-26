import os
# API
API_HOST = os.getenv("CENTRAL_API_HOST")
API_PORT = int(os.getenv("CENTRAL_API_PORT"))
API_KEY = os.getenv("CENTRAL_API_KEY")

BOT_API_KEY = os.getenv('BOT_API_KEY')
BOT_URL = os.getenv('CENTRAL_API_BOT_URL')

# DATABASE
DB_USER = os.getenv('CENTRAL_DB_USER')
DB_PASSWORD = os.getenv('CENTRAL_DB_PASSWORD')
DB_HOST = os.getenv('CENTRAL_DB_HOST')
DB_PORT = int(os.getenv('CENTRAL_DB_PORT'))
DB_NAME = os.getenv('CENTRAL_DB_NAME')

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

