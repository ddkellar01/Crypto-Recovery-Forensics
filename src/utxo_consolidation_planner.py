def plan_utxo_consolidation(utxos: list, fee_per_input: int) -> dict:
    total_val = sum(u["value"] for u in utxos)
    total_fees = len(utxos) * fee_per_input
    net_value = total_val - total_fees
    return {"total_input_value": total_val, "estimated_fees": total_fees, "net_recoverable": net_value}

if __name__ == "__main__":
    utxos = [{"value": 1000}, {"value": 2000}]
    print(plan_utxo_consolidation(utxos, fee_per_input=150))
  
