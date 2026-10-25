import re

def validate_derivation_path(path: str) -> bool:
    pattern = r"^m(\/\d+'?)+$"
    return bool(re.match(pattern, path))

if __name__ == "__main__":
    print(validate_derivation_path("m/44'/60'/0'/0/0")) # False because of unprimed index at end or format check
    print(validate_derivation_path("m/44'/60'/0'/0"))
  
