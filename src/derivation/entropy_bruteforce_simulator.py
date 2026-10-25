"""
Passphrase Derivation Permutation Simulator (Educational).
Demonstrates how dictionary matching or partial passphrase verification
is structured defensively during recovery investigations.
"""

import hashlib

def simulate_passphrase_search(target_hash_prefix: str, dictionary: list) -> str:
    """
    Tests candidate passphrases against a target hash prefix.
    """
    print(f"[*] Scanning {len(dictionary)} candidate passphrases...")
    for word in dictionary:
        hashed = hashlib.sha256(word.encode()).hexdigest()
        if hashed.startswith(target_hash_prefix):
            return f"Match found: '{word}' -> Hash: {hashed}"
    return "No match found in dictionary."

if __name__ == "__main__":
    test_dict = ["password", "secret123", "correcthorsebatterystaple", "recovery"]
    target = hashlib.sha256("secret123".encode()).hexdigest()[:6]
    
    result = simulate_passphrase_search(target, test_dict)
    print(result)
      
