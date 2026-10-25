from web3 import Web3

def estimate_tx_gas(rpc_url: str, tx_dict: dict) -> int:
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    estimated_gas = w3.eth.estimate_gas(tx_dict)
    return estimated_gas

if __name__ == "__main__":
    print("Module loaded. Pass RPC node URL and transaction dictionary to estimate_tx_gas.")
  
