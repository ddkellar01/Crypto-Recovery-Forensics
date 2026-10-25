from web3 import Web3

def get_network_gas_prices(rpc_url: str):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    gas_price = w3.eth.gas_price
    
    return {
        "gas_price_wei": gas_price,
        "gas_price_gwei": w3.from_wei(gas_price, 'gwei')
    }

if __name__ == "__main__":
    RPC_URL = "https://ethereum-rpc.publicnode.com"
    try:
        fees = get_network_gas_prices(RPC_URL)
        print(f"Current Gas Price: {fees['gas_price_gwei']} Gwei")
    except Exception as e:
        print(f"Failed to fetch gas: {e}")
      
