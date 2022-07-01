import json
import cfg
from flask import request
from flask_restful import Resource
from binance.client import Client


class CancelOrderByID (Resource):

    def post(self):
        Data = json.loads(request.data)
        if (Data["Username"] != "admin" or Data["Password"] != "1"):
            return {
                "Response": 500,
                "Message": "Invalid API User Name Or Password"
            }
        AssetPair = Data["AssetPair"]
        OrderID = Data["OrderID"]
        self.client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)
        result = self.client.cancel_order(symbol=AssetPair, orderId=OrderID)
        return (result)
