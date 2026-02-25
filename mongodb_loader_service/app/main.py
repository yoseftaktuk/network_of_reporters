from fastapi import FastAPI
from route import route
import uvicorn
import logging 


logger = logging.basicConfig()
app = FastAPI()
app.include_router(route)
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    uvicorn.run(app , host='localhost', port=8080)
    logger.info('Finished')

if __name__ == '__main__':
    main()