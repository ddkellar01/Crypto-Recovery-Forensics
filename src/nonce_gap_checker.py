def check_nonce_gap(onchain_nonce: int, mempool_nonce: int) -> int:
    return max(0, mempool_nonce - onchain_nonce)

if __name__ == "__main__":
    print(f"Nonce gap: {check_nonce_gap(5, 8)}")
  
