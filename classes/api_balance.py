import json
import cfg
from flask import request
from flask_restful import Resource
from binance.client import Client


class Balance (Resource):

    def post(self):
        Data = json.loads(request.data)
        if (Data["Username"] != "admin" or Data["Password"] != "1"):
            return {
                "Response": 500,
                "Message": "Invalid API User Name Or Password"
            }
        Asset = Data["Asset"]
        self.client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)
        balance = self.client.get_asset_balance(asset=Asset)
        return (balance)
