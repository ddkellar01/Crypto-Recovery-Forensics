from web3 import Web3

def get_address_balances(rpc_url: str, address_list: list) -> dict:
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    results = {}
    
    for address in address_list:
        if w3.is_address(address):
            checksum_addr = w3.to_checksum_address(address)
            balance_wei = w3.eth.get_balance(checksum_addr)
            balance_eth = w3.from_wei(balance_wei, 'ether')
            results[checksum_addr] = float(balance_eth)
        else:
            results[address] = None
            
    return results

if __name__ == "__main__":
    # Standard public node endpoint
    RPC_URL = "https://ethereum-rpc.publicnode.com"
    targets = ["0x0000000000000000000000000000000000000000"]
    try:
        balances = get_address_balances(RPC_URL, targets)
        print(balances)
    except Exception as e:
        print(f"RPC connection failed: {e}")
      
