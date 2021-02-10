class Constants:
    RESPONSE_CODES_SUCCESS = [200, 201]
    RESPONSE_CODES_FAILURE = [400, 401, 404, 500]
    URL = "https://api.coingecko.com/api/v3/coins/{}?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
    CONTENT_TYPE = "application/json"
