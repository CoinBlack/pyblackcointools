import unittest

from cryptos import coins_async
from cryptos.testing.testcases_async import BaseAsyncCoinTestCase
from cryptos.electrumx_client.types import ElectrumXTx, ElectrumXMultiBalanceResponse
from typing import List, Type


class TestBlackcoinTestnet(BaseAsyncCoinTestCase):
    name: str = "Blackcoin Testnet"
    coin: Type[coins_async.BaseCoin] = coins_async.Blackcoin
    addresses: List[str] = [
        "mpXHfVnLbywU8Z1v7getn6vLP8w6T8aKrj",
        "mfs5b3QATcJAaLVaKpTUp1rT4mkb6zdaCP",
        "mzBc4XEFSdzFDcyzEo7XNJWFd3fGFyy7rV",
    ]
    # No segwit addresses for Blackcoin
    multisig_addresses: List[str] = [
        "2MzQ7sXbKqVxS7U1mKPRo8fXS5nGN5bFcpV",
        "2N8oWqWqorv3oV3HB8WFYvXqP4vU4vX4vX4",
    ]
    privkeys: List[str] = [
        "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
        "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321",
    ]
    public_keys: List[str] = [
        "04de476e251a827e58199ed4d6d7c2177f0a97a2dda150d7a9e59fc5682519eb94d37bc387edff66e7b0f16e92dd045fe968d63e1f203613b76ad733e5cdf8e818",
        "0391ed6bf1e0842997938ea2706480a7085b8bb253268fd12ea83a68509602b6e0",
        "0415991434e628402bebcbaa3261864309d2c6fd10c850462b9ef0258832822d35aa26e62e629d2337e3716784ca6c727c73e9600436ded7417d957318dc7a41eb",
    ]
    privkey_standard_wifs: List[str] = [
        "91f8DFTsmhtawuLjR8CiHNkgZGPkUqfJ45LxmENPf3k6fuX1m4N",
        "cMrziExc6iMV8vvAML8QX9hGDP8zNhcsKbdS9BqrRa1b4mhKvK6f",
        "9354Dkk67pJCfmRfMedJPhGPfZCXv2uWd9ZoVNMUtDxjUBbCVZK",
    ]
    fee: int = 1000
    max_fee: int = 2000
    testnet: bool = True
    min_latest_height: int = 2000000
    balance: ElectrumXMultiBalanceResponse = {
        "confirmed": 50000000000,
        "unconfirmed": 0,
        "address": "mpXHfVnLbywU8Z1v7getn6vLP8w6T8aKrj",
    }
    balances: List[ElectrumXMultiBalanceResponse] = [
        {
            "confirmed": 50000000000,
            "unconfirmed": 0,
            "address": "mpXHfVnLbywU8Z1v7getn6vLP8w6T8aKrj",
        },
        {
            "confirmed": 25000000000,
            "unconfirmed": 0,
            "address": "mfs5b3QATcJAaLVaKpTUp1rT4mkb6zdaCP",
        },
    ]
    history: List[ElectrumXTx] = [
        {
            "tx_hash": "d7d29c3ee14f2586b7dc18a23c193499831ed24fa43c0504e91fe1296d1cd075",
            "height": 5000,
            "value": 10000000110000,
        },
        {
            "tx_hash": "31fee1df8ab67a285c5f03e67865e0ac780c788832e9bc618c3d89a46a5f8797",
            "height": 5000,
            "value": 10000000110000,
        },
    ]
    txid: str = "d7d29c3ee14f2586b7dc18a23c193499831ed24fa43c0504e91fe1296d1cd075"
    txheight: int = 5000
    block_hash: str = "000000000032c7897d4cfd01a48df7d7b43b861eb9c6fd5a2575e3761fa158d8"
    raw_tx: str = "0100000069ba0f53010000000000000000000000000000000000000000000000000000000000000000ffffffff1f0288130478ba0f5308f8000239020000000d2f7374726174756d506f6f6c2f0000000001b0bda6d4e800000023210320fb59f0f70c491a5d54082bc18cce6f33a856b2bbc814a80755ab3c8cf8c3cfac00000000"
    unspent: List[ElectrumXTx] = [
        {
            "height": 5000,
            "tx_hash": "d7d29c3ee14f2586b7dc18a23c193499831ed24fa43c0504e91fe1296d1cd075",
            "value": 10000000110000,
            "address": "B9T76ZNriKoWvZwyi2cScBySfn4vm5tUxn",
        }
    ]
    tx: dict = {
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

    # Blackcoin testnet-specific test methods if needed
    def test_blackcoin_testnet_specific_feature(self):
        """Test any Blackcoin testnet-specific functionality"""
        pass
