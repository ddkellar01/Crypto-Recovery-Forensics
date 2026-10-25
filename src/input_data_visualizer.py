def decode_calldata(calldata_hex: str) -> dict:
    if calldata_hex.startswith("0x"):
        calldata_hex = calldata_hex[2:]
        
    if len(calldata_hex) < 8:
        return {"error": "Calldata too short for function selector"}
        
    selector = "0x" + calldata_hex[:8]
    arguments_payload = calldata_hex[8:]
    
    # Split argument slots into 32-byte chunks (64 hex characters)
    chunks = [arguments_payload[i:i+64] for i in range(0, len(arguments_payload), 64)]
    
    return {
        "function_selector": selector,
        "argument_chunks": chunks
    }

if __name__ == "__main__":
    # Sample ERC-20 transfer calldata (a9059cbb + recipient + value)
    sample_calldata = "0xa9059cbb00000000000000000000000035353535353535353535353535353535353535350000000000000000000000000de0b6b3a7640000"
    decoded = decode_calldata(sample_calldata)
    print(decoded)
  
