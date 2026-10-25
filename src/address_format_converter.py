from bip_utils import Bip32PublicKey, Bip44Coins, Bip84Coins, Bip44, Bip84

def pubkey_to_addresses(pubkey_bytes: bytes) -> dict:
    # Import raw compressed public key bytes
    bip44_ctx = Bip44.FromPublicKey(pubkey_bytes, Bip44Coins.BITCOIN)
    bip84_ctx = Bip84.FromPublicKey(pubkey_bytes, Bip84Coins.BITCOIN)
    
    legacy_addr = bip44_ctx.PublicKey().ToAddress()
    segwit_addr = bip84_ctx.PublicKey().ToAddress()

    return {
        "p2pkh_legacy": legacy_addr,
        "p2wpkh_segwit": segwit_addr
    }

if __name__ == "__main__":
    # Test compressed public key hex
    sample_pubkey = bytes.fromhex("0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798")
    addrs = pubkey_to_addresses(sample_pubkey)
    for k, v in addrs.items():
        print(f"{k}: {v}")
      
