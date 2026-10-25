from eth_account import Account
import json

def decrypt_keystore_json(keystore_dict: dict, password: str) -> str:
    private_key_bytes = Account.decrypt(keystore_dict, password)
    return private_key_bytes.hex()

if __name__ == "__main__":
    # Standard encrypted V3 test vector keystore
    sample_keystore = {
        "crypto": {
            "cipher": "aes-128-ctr",
            "ciphertext": "17088710373df92d4f3ddbcf685e1b20c24298150f56a31c5b05a76e9384777d",
            "cipherparams": {"iv": "c76c1a1795c6131c778c1a1795c6131c"},
            "kdf": "scrypt",
            "kdfparams": {"dklen": 32, "n": 2, "r": 8, "p": 1, "salt": "624024479e0a8111977759b646c2415d"},
            "mac": "b53f6521be945952dfa24a52ff37c8ee306e6ff70c7980eefb187515320e8b24"
        },
        "id": "7876a31b-2520-410e-8f5b-6b80145c23d5",
        "version": 3
    }
    # Note: Password for this test vector is "testpassword"
    try:
        pk = decrypt_keystore_json(sample_keystore, "testpassword")
        print(f"Successfully decrypted private key: 0x{pk}")
    except Exception as e:
        print(f"Decryption failed: {e}")
      
