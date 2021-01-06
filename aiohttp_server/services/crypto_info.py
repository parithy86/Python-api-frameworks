import requests

from aiohttp_server.constants.constants import Constants


async def get_crypto_details(request):
    response = requests.get(Constants.URL)
    if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
        return response.text, response.status_code

    else:
        return {"status": "failure"}, response.status_code


async def get_crypto(request):
    url = "https://api.coingecko.com/api/v3/coins/ethereum?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
    response = requests.get(url)
    if response.status_code in Constants.RESPONSE_CODES_SUCCESS:
        return response.text, response.status_code

    else:
        return {"status": "failure"}, response.status_code
