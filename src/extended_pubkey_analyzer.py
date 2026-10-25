from bip_utils import Bip44PublicKey, Bip44Coins, Bip44Changes

def analyze_xpub(xpub_str: str, count: int = 5):
    bip44_pub = Bip44PublicKey.FromExtendedKey(xpub_str)
    change_chain = bip44_pub.Change(Bip44Changes.CHAIN_EXT)

    print(f"--- Analyzing xpub: {xpub_str[:15]}... ---")
    for i in range(count):
        addr = change_chain.AddressIndex(i).ToAddress()
        print(f"Child Address {i}: {addr}")

if __name__ == "__main__":
    # Standard test vector xpub
    sample_xpub = "xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8"
    try:
        analyze_xpub(sample_xpub, count=3)
    except Exception as e:
        print(f"Error parsing xpub: {e}")
      
