def decode_bitcoin_block_header(header_hex: str) -> dict:
    if header_hex.startswith("0x"):
        header_hex = header_hex[2:]
    if len(header_hex) != 160: # 80 bytes * 2 hex chars
        raise ValueError("Block header must be exactly 80 bytes (160 hex chars).")
        
    return {
        "version": header_hex[0:8],
        "prev_block_hash": header_hex[8:72],
        "merkle_root": header_hex[72:136],
        "timestamp": int(header_hex[136:144], 16),
        "bits": header_hex[144:152],
        "nonce": int(header_hex[152:160], 16)
    }

if __name__ == "__main__":
    # Genesis block header test vector (reversed byte representation)
    sample_header = "0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c"
    print(decode_bitcoin_block_header(sample_header))
  
