from eth_utils import keccak

# Topic 0 signature hash for Transfer(address,address,uint256)
TRANSFER_EVENT_TOPIC = "0x" + keccak(text="Transfer(address,address,uint256)").hex()

def decode_transfer_log(log: dict) -> dict:
    topics = log.get("topics", [])
    if not topics or topics[0].lower() != TRANSFER_EVENT_TOPIC.lower():
        return {"error": "Not a standard Transfer event"}

    # Indexed parameters are zero-padded to 32 bytes in topics
    from_address = "0x" + topics[1][-40:]
    to_address = "0x" + topics[2][-40:]
    
    # Non-indexed parameter (value/tokenId) stored in data field
    raw_data = log.get("data", "0x0")
    value = int(raw_data, 16)

    return {
        "event": "Transfer",
        "from": from_address,
        "to": to_address,
        "value_raw": value
    }

if __name__ == "__main__":
    sample_log = {
        "topics": [
            TRANSFER_EVENT_TOPIC,
            "0x0000000000000000000000001111111111111111111111111111111111111111",
            "0x0000000000000000000000002222222222222222222222222222222222222222"
        ],
        "data": "0x000000000000000000000000000000000000000000000005f5e100" # 100000000 wei
    }
    decoded = decode_transfer_log(sample_log)
    print(decoded)
  
