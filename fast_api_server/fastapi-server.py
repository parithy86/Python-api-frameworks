from fastapi import FastAPI, Request
import uvicorn
import requests
from fast_api_server.services import crypto_info

# import requests
#
# from FastApi_server.constants.constants import Constants
# from FastApi_server.utils.helpers_util import read_yaml_configs


app = FastAPI()


@app.get("/health")
async def health():
    return {"REST API using Fast API framework, Health Ok "}


app.include_router(
    crypto_info.router,
    prefix="",
    responses={418: {"description": "I'm a teapot"}},
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
