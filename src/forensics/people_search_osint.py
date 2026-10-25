"""
Educational Crypto OSINT & Entity Attribution Module.
Performs ENS reverse resolution and retrieves public metadata records
associated with blockchain addresses for investigative context.
"""

from web3 import Web3

def search_wallet_identity(rpc_url: str, address: str) -> dict:
    """
    Performs on-chain reverse lookup to find ENS names and associated 
    public text profile records (e.g., Twitter, GitHub, email) tied to an address.
    """
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if not w3.is_address(address):
        raise ValueError(f"Invalid Ethereum address format: {address}")
        
    checksum_addr = w3.to_checksum_address(address)
    identity_data = {
        "address": checksum_addr,
        "ens_name": None,
        "records": {}
    }
    
    try:
        # Attempt ENS reverse resolution using web3.ens
        # Note: Requires an archive/full provider that supports ENS registry mapping
        ens_name = w3.ens.name(checksum_addr)
        if ens_name:
            identity_data["ens_name"] = ens_name
            
            # Fetch common public text attributes if an ENS name exists
            keys_to_fetch = ["email", "url", "com.twitter", "com.github", "avatar"]
            for key in keys_to_fetch:
                try:
                    val = w3.ens.get_text(ens_name, key)
                    if val:
                        identity_data["records"][key] = val
                except Exception:
                    pass
    except Exception as e:
        identity_data["lookup_error"] = str(e)
        
    return identity_data

if __name__ == "__main__":
    # Example using a public Ethereum mainnet RPC endpoint
    RPC_URL = "https://ethereum-rpc.publicnode.com"
    
    # Test vector (e.g., vitalik.eth address or known entity)
    sample_address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045" 
    
    print(f"[*] Querying public identity registry for: {sample_address}")
    try:
        result = search_wallet_identity(RPC_URL, sample_address)
        print("--- OSINT Identity Search Results ---")
        for k, v in result.items():
            print(f"{k}: {v}")
    except Exception as err:
        print(f"Search execution failed: {err}")
      
