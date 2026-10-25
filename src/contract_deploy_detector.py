def is_contract_deployment(tx_to_field) -> bool:
    return tx_to_field is None or tx_to_field == "" or tx_to_field == "0x"

if __name__ == "__main__":
    print(f"Is deployment: {is_contract_deployment(None)}")
  
