def calculate_entropy_bits(word_count: int) -> dict:
    if word_count not in [12, 15, 18, 21, 24]:
        raise ValueError("Invalid BIP-39 word count.")
    entropy_bits = (word_count * 11) * 32 // 33
    checksum_bits = word_count // 3
    return {"words": word_count, "entropy_bits": entropy_bits, "checksum_bits": checksum_bits}

if __name__ == "__main__":
    print(calculate_entropy_bits(12))
  
