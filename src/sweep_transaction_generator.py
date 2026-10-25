from web3 import Web3

def build_sweep_transaction(rpc_url: str, sender_addr: str, receiver_addr: str) -> dict:
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    checksum_sender = w3.to_checksum_address(sender_addr)
    checksum_receiver = w3.to_checksum_address(receiver_addr)
    
    balance = w3.eth.get_balance(checksum_sender)
    gas_price = w3.eth.gas_price
    gas_limit = 21000 # Standard transfer gas
    total_fee = gas_limit * gas_price
    
    value_to_send = balance - total_fee
    if value_to_send < 0:
        raise ValueError("Insufficient balance to cover gas fees.")
        
    nonce = w3.eth.get_transaction_count(checksum_sender)
    
    tx = {
        'nonce': nonce,
        'to': checksum_receiver,
        'value': value_to_send,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'chainId': w3.eth.chain_id
    }
    return tx

if __name__ == "__main__":
    print("Module loaded. Pass RPC and addresses to build_sweep_transaction.")
  
