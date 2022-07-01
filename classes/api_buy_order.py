from cgi import test
import json
import cfg
from flask import request
from flask_restful import Resource
from binance.client import Client
from classes import helper_binance as Bin


class BuyLimitOrder (Resource):

    def post(self):
        Data = json.loads(request.data)
        self.client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)

        if (Data["Username"] != "admin" or Data["Password"] != "1"):
            return {
                "Response": 500,
                "Message": "Invalid API User Name Or Password"
            }

        Amount = Bin.GetAssetAmount(cfg.ASSET_STABLE)
        Quantity = float(Amount) / float(Data["Price"])

        Quantity = float(round(Quantity, 6))
        Quantity = "{:.6f}".format(Quantity)[:-1]
        BuyOrder = Bin.Create_Limit_Order_Buy(Data["AssetPair"], Data["Price"], Quantity)

        return BuyOrder
