import json
import cfg
from flask import request
from flask_restful import Resource
from classes import helper_binance as Bin


class SalesLimitOrder(Resource):

    def post(self):
        try:
            print(request.data)
            self.data = json.loads(request.data)
            self.order_type = self.data["strategy"]["order_action"]
            self.order_price = self.data["strategy"]["order_price"]
        except Exception as E:
            return {
                "Response": 500,
                "Message": "Invalid Json",
                "log": str(E)
            }

        if self.order_type != "sell":
            return {
                "Response": 500,
                "Message": "Api Error",
                "log": "Invalid Order Type"
            }

        if self.data["Token"] != "112143":
            return {
                "Response": 500,
                "Message": "Api Error",
                "log": "Invalid Order"
            }

        if self.data["exchange"] != "BINANCE":
            return {
                "Response": 500,
                "Message": "Api Error",
                "log": "Invalid Exchange"
            }

        Amount = str(Bin.GetAssetAmount(cfg.ASSET_COIN))[:-3]
        SellOrder = Bin.Create_Limit_Order_Sell(
            self.data["ticker"],
            self.order_price,
            f"{float(Amount):.5f}"
        )

        return {
            "Response": 200,
            "Message": "Limnit Order Created",
            "SellOrder": SellOrder
        }
