from .base import BaseCoin


class Blackcoin(BaseCoin):
    coin_symbol = "BLK"
    display_name = "Blackcoin"
    segwit_supported = False
    magicbyte = 0x19  # 25 - addresses start with 'B'
    script_magicbyte = 0x55  # 85 - addresses start with 'b'
    minimum_fee = 1000
    wif_prefix: int = 0x99  # 153 - private keys start with '6'
    hd_path = 10  # BIP44 coin index for Blackcoin
    client_kwargs = {
        "server_file": "blackcoin.json",
    }

    testnet_overrides = {
        "display_name": "Blackcoin Testnet",
        "coin_symbol": "tBLK",
        "magicbyte": 0x6F,  # 111 - addresses start with 'm'/'n'
        "script_magicbyte": 0xC4,  # 196 - addresses start with '2'
        "hd_path": 1,
        "wif_prefix": 0xEF,  # 239 - private keys start with '9'
        "minimum_fee": 1000,
        "client_kwargs": {"server_file": "blackcoin_testnet.json", "use_ssl": False},
        "electrum_pkey_format": "wif",
        "xprv_headers": {
            "p2pkh": 0x04358394,
            "p2sh": 0x04358394,
        },
        "xpub_headers": {
            "p2pkh": 0x043587CF,
            "p2sh": 0x043587CF,
        },
    }
