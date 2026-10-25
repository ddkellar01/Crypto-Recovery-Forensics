import json

def parse_utxo_tx(tx_data: dict) -> dict:
    inputs = [f"{txin['txid']}:{txin['vout']}" for txin in tx_data.get("vin", [])]
    outputs = []
    
    for vout in tx_data.get("vout", []):
        outputs.append({
            "address": vout.get("scriptPubKey", {}).get("address"),
            "value_satoshis": int(vout.get("value", 0) * 1e8)
        })

    return {
        "txid": tx_data.get("txid"),
        "inputs": inputs,
        "outputs": outputs
    }

if __name__ == "__main__":
    sample_tx = {
        "txid": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
        "vin": [{"txid": "0000000000000000000000000000000000000000000000000000000000000000", "vout": 0}],
        "vout": [{"value": 50.0, "scriptPubKey": {"address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}}]
    }
    graph = parse_utxo_tx(sample_tx)
    print(json.dumps(graph, indent=2))
  
