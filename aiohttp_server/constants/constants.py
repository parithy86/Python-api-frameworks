class Constants:
    RESPONSE_CODES_SUCCESS = [200, 201]
    RESPONSE_CODES_FAILURE = [400, 401, 404, 500]
    URL = "https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
    CONTENT_TYPE = "application/json"

    SERVICE_CONFIG = {
        "get_crypto_details": {
            "function_name": "crypto_info",
            "execute_method": "get_crypto_details"
        },
        "get_crypto": {
            "function_name": "crypto_info",
            "execute_method": "get_crypto"
        }
    }
