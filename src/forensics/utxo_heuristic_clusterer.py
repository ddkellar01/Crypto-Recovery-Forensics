"""
UTXO Common-Input Ownership Heuristic Clusterer.
Assumes all inputs consumed in a single Bitcoin transaction
belong to the same controlling entity.
"""

def cluster_utxo_transaction(tx_inputs: list) -> set:
    """
    Extracts and groups unique source addresses from transaction inputs.
    """
    entity_cluster = set()
    for txin in tx_inputs:
        address = txin.get("address")
        if address:
            entity_cluster.add(address)
    return entity_cluster

if __name__ == "__main__":
    sample_inputs = [
        {"txid": "abc...", "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"},
        {"txid": "def...", "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"} # Same entity input
    ]
    cluster = cluster_utxo_transaction(sample_inputs)
    print(f"Clustered Entity Addresses: {list(cluster)}")
  
