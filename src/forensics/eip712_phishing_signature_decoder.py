"""
EIP-712 Typed Signature Inspector.
Decodes structured off-chain messages (Permit, Permit2, Blur bids, etc.)
frequently analyzed during wallet drainer and phishing investigations.
"""

def decode_eip712_payload(payload: dict) -> dict:
    """
    Parses structural components of an EIP-712 typed data payload.
    """
    return {
        "domain": payload.get("domain", {}),
        "primary_type": payload.get("primaryType"),
        "message_fields": payload.get("message", {}),
        "warning": "Inspect domain separator and allowance limits for unauthorized delegation."
    }

if __name__ == "__main__":
    sample_payload = {
        "domain": {"name": "Permit2", "chainId": 1, "verifyingContract": "0x0000000022D473030f116dDEE9F6B43aC78BA30ef"},
        "primaryType": "PermitSingle",
        "message": {"details": {"token": "0x6b175474e89094c44da98b954eedeac495271d0f", "amount": "1000000000000000000"}}
    }
    print("--- EIP-712 Signature Analysis ---")
    print(decode_eip712_payload(sample_payload))
  
