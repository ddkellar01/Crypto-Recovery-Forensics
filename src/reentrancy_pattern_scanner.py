import pyevmasm

def scan_reentrancy_indicators(bytecode_hex: str) -> list:
    if bytecode_hex.startswith("0x"):
        bytecode_hex = bytecode_hex[2:]
    instructions = list(pyevmasm.disassemble_all(bytes.fromhex(bytecode_hex)))
    
    findings = []
    for i, instr in enumerate(instructions):
        if instr.name in ["CALL", "DELEGATECALL", "STATICCALL"]:
            findings.append({"pc": instr.pc, "instruction": instr.name, "index": i})
    return findings

if __name__ == "__main__":
    print(scan_reentrancy_indicators("6080604052f1"))
  
