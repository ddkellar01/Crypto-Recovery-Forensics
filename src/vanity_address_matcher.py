from eth_account import Account
import secrets

def search_vanity_prefix(target_prefix: str, max_iterations: int = 1000):
    target_prefix = target_prefix.lower().replace("0x", "")
    print(f"Searching for addresses starting with: 0x{target_prefix} (Max: {max_iterations} tries)")
    
    for i in range(max_iterations):
        priv_key = "0x" + secrets.token_hex(32)
        acct = Account.from_key(priv_key)
        addr = acct.address.lower()
        
        if addr[2:].startswith(target_prefix):
            print(f"[Match Found on try {i}]")
            print(f"Address: {acct.address}")
            print(f"Private Key: {priv_key}")
            return acct.address
            
    print("No match found within iteration limit.")
    return None

if __name__ == "__main__":
    search_vanity_prefix("123", max_iterations=500)
  
