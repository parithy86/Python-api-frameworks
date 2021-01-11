import requests
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from aiohttp_server.constants.constants import Constants

router = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def get_crypto_details():
    return"""<h1> Hello World </h1>"""


# async def get_crypto(request):
#     url = "https://api.coingecko.com/api/v3/coins/ethereum?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
#     response = requests.get(url)
#     if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
#         return response.text, response.status_code
#
#     else:
#         return {"status": "failure"}, response.status_code
