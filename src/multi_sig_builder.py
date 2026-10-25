def create_multisig_blueprint(pubkeys: list, threshold: int) -> dict:
    if threshold > len(pubkeys):
        raise ValueError("Threshold cannot exceed number of public keys.")
        
    return {
        "threshold": threshold,
        "total_signers": len(pubkeys),
        "script_type": f"{threshold}-of-{len(pubkeys)} Multisig",
        "public_keys": pubkeys
    }

if __name__ == "__main__":
    sample_pubkeys = [
        "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
        "032ffe53434cf9bc490d1f73b22cf334f590483ea54dfeb797d1b3269b2d86f76c",
        "02c6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5"
    ]
    blueprint = create_multisig_blueprint(sample_pubkeys, threshold=2)
    print(blueprint)
  
