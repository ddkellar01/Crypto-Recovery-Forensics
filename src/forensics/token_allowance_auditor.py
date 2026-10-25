"""
ERC-20 Token Allowance Auditor.
Queries smart contracts to identify active spending approvals
granted by a compromised or audited address.
"""

from web3 import Web3

def audit_allowance(rpc_url: str, token_addr: str, owner_addr: str, spender_addr: str) -> int:
    """
    Queries an ERC-20 allowance mapping: allowance(owner, spender)
    """
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    # Minimal ABI for ERC-20 allowance check
    erc20_abi = [{"constant": True, "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "", "type": "uint256"}], "type": "function"}]
    
    contract = w3.eth.contract(address=w3.to_checksum_address(token_addr), abi=erc20_abi)
    allowance_val = contract.functions.allowance(
        w3.to_checksum_address(owner_addr), 
        w3.to_checksum_address(spender_addr)
    ).call()
    
    return allowance_val

if __name__ == "__main__":
    print("Module loaded. Pass RPC URL, token, owner, and spender to audit_allowance.")
  
