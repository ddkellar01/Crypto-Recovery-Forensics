from eth_account import Account

def parse_raw_tx(raw_tx_hex: str) -> dict:
    # Requires raw RLP-encoded hex string
    decoded = Account.decode_transaction(raw_tx_hex)
    return {
        "nonce": decoded.get("nonce"),
        "gasPrice": decoded.get("gasPrice"),
        "gasLimit": decoded.get("gas"),
        "to": decoded.get("to"),
        "value": decoded.get("value"),
        "data": decoded.get("data"),
        "v": decoded.get("v"),
        "r": decoded.get("r"),
        "s": decoded.get("s"),
    }

if __name__ == "__main__":
    # Sample legacy transaction raw hex
    sample_raw_hex = "0xf86c098504a817c800825208943535353535353535353535353535353535353535880de0b6b3a7640000801ca028041d55e0b21f577d0a1323e65c23e931bc7d37327686eef4038a80a6dd0b10a02c0c4a169b2d8804febd3176d6eb1610cc4f112a1218b04e9d0ce8ba9486f0b0"
    parsed = parse_raw_tx(sample_raw_hex)
    for key, value in parsed.items():
        print(f"{key}: {value}")
      
