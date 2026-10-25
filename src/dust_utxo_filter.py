def filter_dust_utxos(utxo_list: list, estimated_fee_satoshis: int) -> list:
    dust_list = []
    viable_list = []
    
    for utxo in utxo_list:
        value = utxo.get("value_satoshis", 0)
        if value < estimated_fee_satoshis:
            dust_list.append(utxo)
        else:
            viable_list.append(utxo)
            
    return {"dust": dust_list, "viable": viable_list}

if __name__ == "__main__":
    sample_utxos = [
        {"txid": "abc1...", "vout": 0, "value_satoshis": 300},
        {"txid": "def2...", "vout": 1, "value_satoshis": 50000}
    ]
    # Assuming current spending cost is ~1000 satoshis
    filtered = filter_dust_utxos(sample_utxos, estimated_fee_satoshis=1000)
    print(f"Identified Dust UTXOs: {len(filtered['dust'])}")
    print(f"Viable UTXOs: {len(filtered['viable'])}")
  
