from cryptos.coins_async.blackcoin import Blackcoin as AsyncBlackcoin
from .base import BaseSyncCoin


class Blackcoin(BaseSyncCoin):
    coin_class = AsyncBlackcoin
