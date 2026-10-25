from bip_utils import Bip39MnemonicValidator, Bip39Languages

def validate_mnemonic(phrase: str) -> bool:
    validator = Bip39MnemonicValidator(Bip39Languages.ENGLISH)
    is_valid = validator.IsValid(phrase)
    return is_valid

if __name__ == "__main__":
    sample_phrase = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    valid = validate_mnemonic(sample_phrase)
    print(f"Mnemonic Valid: {valid}")
  
