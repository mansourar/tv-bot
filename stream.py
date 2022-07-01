import asyncio
import requests
import json
from binance import AsyncClient, BinanceSocketManager


async def main():
    TEST_NET = False
    if TEST_NET:
        BINANCE_API_KEY = "IwkSffbhbl4xvzav8kj5XcxBO1OC5u5nWkaCv0kZwPibfTjhrAW6zOiR3HXZXoRm"
        BINANCE_API_SEC = "1REVTYypRFWoWcf2vriifiEsHnb8cvk9SnCjfwSmNX3NuCccUTzCXdPQAlWQK8qC"
    else:
        BINANCE_API_KEY = "yzKipyseCkuyoj88nHzMyN7OQCh3S2piE9fUxAG3Pav1U966afTTJVYfgpAPurdm"
        BINANCE_API_SEC = "1rclPeY0eXeUNxi6tNNM3BqHtCHwg1PDxAvl6hRKI5m2BVUl1j9D19A5C989uUU8"

    client = await AsyncClient.create(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SEC, testnet=TEST_NET)
    bm = BinanceSocketManager(client)
    ts = bm.user_socket()
    async with ts as tscm:
        while True:
            res = await tscm.recv()

           
            if res["e"] != "executionReport":
                continue
            print("Json Type : " + res["e"])

            print("Order Type : " + res["S"])
            if res["S"] != "SELL":
                continue

            print("Order Status : " + res["X"])
            if res["X"] != "FILLED":
                continue

            Price = float(res["p"]) - (float(res["p"]) * 0.3 / 100)
            print(res["S"] + " Order : " + res["X"])
            print(f"Sold Quantity : " + res["q"])
            print(f"Sold Price : " + res["p"])
            print(f"Buy Price : {Price}")

            url = "http://127.0.0.1:5000/LimitBuyOrder"
            payload = {
                "Username": "admin",
                "Password": "1",
                "AssetPair": "BTCBUSD",
                "Price": Price
            }
            headers = {'Content-Type': 'application/json'}
            print()
            print(payload)

            response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
            print()
            print(response.text)

    await client.close_connection()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
