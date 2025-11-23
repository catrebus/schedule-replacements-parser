from central_api.app.config import API_HOST, API_PORT
from central_api.app.main import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host=API_HOST, port=API_PORT)