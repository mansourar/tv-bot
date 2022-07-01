import json
import cfg
from binance.client import Client
from binance.enums import *


def GetAssetAmount(Asset):
    client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)
    balance = client.get_asset_balance(asset=Asset)
    return balance["free"]


def GetOpenOrders(AssetPair):
    try:
        client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)
        trades = client.get_open_orders(symbol=AssetPair)
        return trades
    except:
        return "ERROR"


def Create_Limit_Order_Sell(AssetPair, AtPrice, Quantity):
    client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)
    order = client.order_limit_sell(
        symbol=AssetPair,
        quantity=Quantity,
        price=AtPrice
    )
    return order


def Create_Market_Order_Sell(AssetPair, Quantity):
    client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)
    order = client.order_market_sell(
        symbol=AssetPair,
        quantity=Quantity
    )
    return order


def Create_Limit_Order_Buy(AssetPair, AtPrice, Quantity):
    client = Client(cfg.BINANCE_API_KEY, cfg.BINANCE_API_SEC, testnet=cfg.TEST_NET)
    order = client.order_limit_buy(
        symbol=AssetPair,
        quantity=Quantity,
        price=AtPrice
    )
    return order
