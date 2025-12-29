import unittest

from cryptos import coins_async
from cryptos.main import script_to_scripthash
from cryptos.types import TxInput, Tx
from cryptos.testing.testcases_async import BaseAsyncCoinTestCase
from cryptos.electrumx_client.types import ElectrumXTx, ElectrumXMultiBalanceResponse
from typing import List, Type
from unittest import mock


class TestBlackcoin(BaseAsyncCoinTestCase):
    name: str = "Blackcoin"
    coin: Type[coins_async.BaseCoin] = coins_async.Blackcoin
    addresses: List[str] = [
        "BDPQ2XQCws2aos1Q1g9srf8wkQDCtZekXw",
        "BFeVKmzRHNYxMMzcWg1zExjT8nuZYoFfxv",
        "BPx45mphDKoCQY2tuhGmguf5zJ58dXAA8g",
    ]
    # No segwit addresses for Blackcoin
    multisig_addresses: List[str] = [
        "bg7y9rH9pQ1m2c3d4e5f6g7h8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5",
        "b9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i1h0g9f8e7d6c5b4a3z2y1x0w",
    ]
    privkeys: List[str] = [
        "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
        "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321",
    ]
    privkey_standard_wifs: List[str] = [
        "6htVdWeLBUpSyqqSnnJoQnCiuc33Kg86i8V1gc1tKK13tw1Cqrg",
        "6wW1FKxkfefDyVStxvKH9qCCb9qaiFXBFZUy2mPLvTMap2f5YaXR",
        "6KJRe1vYXbE4hhvNjJjPX6iS1tqpksNKHChrQjzyYVDgh9Z8H5o",
    ]
    fee: int = 1000
    max_fee: int = fee
    testnet: bool = False
    balance: ElectrumXMultiBalanceResponse = {
        "confirmed": 100000000000,
        "unconfirmed": 0,
        "address": "BDPQ2XQCws2aos1Q1g9srf8wkQDCtZekXw",
    }
    balances: List[ElectrumXMultiBalanceResponse] = [
        {
            "confirmed": 100000000000,
            "unconfirmed": 0,
            "address": "BDPQ2XQCws2aos1Q1g9srf8wkQDCtZekXw",
        },
        {
            "confirmed": 50000000000,
            "unconfirmed": 0,
            "address": "BFeVKmzRHNYxMMzcWg1zExjT8nuZYoFfxv",
        },
    ]
    history: List[ElectrumXTx] = [
        {
            "tx_hash": "6bad37e8bbf9dfbe5a43bb3d66245864ebd4d81f34e744c3c14fcfe1d182f137",
            "height": 5000,
            "value": 10000000110000,
        },
        {
            "tx_hash": "d7d29c3ee14f2586b7dc18a23c193499831ed24fa43c0504e91fe1296d1cd075",
            "height": 5000,
            "value": 10000000110000,
        },
    ]
    txid: str = "6bad37e8bbf9dfbe5a43bb3d66245864ebd4d81f34e744c3c14fcfe1d182f137"
    txheight: int = 5000
    block_hash: str = "000000000032c7897d4cfd01a48df7d7b43b861eb9c6fd5a2575e3761fa158d8"
    raw_tx: str = "0100000069ba0f53010000000000000000000000000000000000000000000000000000000000000000ffffffff1f0288130478ba0f5308f8000239020000000d2f7374726174756d506f6f6c2f0000000001b0bda6d4e800000023210320fb59f0f70c491a5d54082bc18cce6f33a856b2bbc814a80755ab3c8cf8c3cfac00000000"
    unspent: List[ElectrumXTx] = [
        {
            "height": 5000,
            "tx_hash": "6bad37e8bbf9dfbe5a43bb3d66245864ebd4d81f34e744c3c14fcfe1d182f137",
            "value": 10000000110000,
            "address": "B9T76ZNriKoWvZwyi2cScBySfn4vm5tUxn",
        }
    ]
    tx: Tx = {
        "locktime": 0,
        "version": 1,
        "ins": [
            {
                "script": "",
                "sequence": 0,
                "outpoint": {
                    "hash": "0000000000000000000000000000000000000000000000000000000000000000",
                    "index": 4294967295,
                },
            }
        ],
        "outs": [
            {
                "value": 10000000110000,
                "script": "210320fb59f0f70c491a5d54082bc18cce6f33a856b2bbc814a80755ab3c8cf8c3cfac",
            }
        ],
    }

    # Blackcoin-specific test methods if needed
    def test_blackcoin_specific_feature(self):
        """Test any Blackcoin-specific functionality"""
        pass
