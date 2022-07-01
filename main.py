from flask import Flask
from flask_restful import Api
from classes import api_ping as ping
from classes import api_sales_order as so
from classes import api_buy_order as bo
from classes import api_trading_fees as tf
from classes import api_balance as ba
from classes import api_trades_list as tl
from classes import api_open_trades_list as ot
from classes import api_cancel_order as co


app = Flask(__name__)
api = Api(app)


api.add_resource(ping.Ping, "/")
api.add_resource(tl.TradesList, "/TradesList")
api.add_resource(so.SalesLimitOrder, "/LimitSalesOrder")
api.add_resource(bo.BuyLimitOrder, "/LimitBuyOrder")
api.add_resource(tf.TradeFees, "/TradeFees")
api.add_resource(ba.Balance, "/Balance")
api.add_resource(ot.OpenTradesList, "/OpenTradesList")
api.add_resource(co.CancelOrderByID, "/CancelOrderByID")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
