import uvicorn
from fastapi import FastAPI

from fast_api_server.utils import function_router

app = FastAPI()


@app.get("/health")
async def health():
    return {"REST API using Fast API framework, Health Ok "}


app.include_router(
    function_router.router,
    prefix="/v1/services"
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
