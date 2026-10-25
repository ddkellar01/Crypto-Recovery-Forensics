# secp256k1 curve order half-point constant
SECP256K1_N_DIV_2 = 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0

def check_signature_s_value(s_hex: str) -> dict:
    s_int = int(s_hex, 16) if s_hex.startswith("0x") else int(s_hex, 16)
    is_high = s_int > SECP256K1_N_DIV_2
    
    return {
        "s_value": hex(s_int),
        "is_high_s": is_high,
        "warning": "High s-value detected (potential malleability issue)" if is_high else "Normal s-value"
    }

if __name__ == "__main__":
    sample_s = "0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a1"
    result = check_signature_s_value(sample_s)
    print(result)
  
