from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, Bip84, Bip84Coins

def derive_addresses(mnemonic: str, count: int = 5):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    
    # Ethereum (m/44'/60'/0'/0/i)
    bip44_eth = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    eth_acc = bip44_eth.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)
    
    # Bitcoin Native SegWit (m/84'/0'/0'/0/i)
    bip84_btc = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)
    btc_acc = bip84_btc.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)

    print("--- Ethereum (BIP-44) ---")
    for i in range(count):
        addr = eth_acc.AddressIndex(i).PublicKey().ToAddress()
        print(f"Index {i}: {addr}")

    print("\n--- Bitcoin Native SegWit (BIP-84) ---")
    for i in range(count):
        addr = btc_acc.AddressIndex(i).PublicKey().ToAddress()
        print(f"Index {i}: {addr}")

if __name__ == "__main__":
    sample_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    derive_addresses(sample_mnemonic, count=3)
  
