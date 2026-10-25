import pyevmasm

def disassemble_evm(bytecode_hex: str):
    if bytecode_hex.startswith("0x"):
        bytecode_hex = bytecode_hex[2:]
        
    bytecode_bytes = bytes.fromhex(bytecode_hex)
    disassembled = pyevmasm.disassemble_all(bytecode_bytes)
    return list(disassembled)

if __name__ == "__main__":
    # Sample basic EVM initialization code snippet
    sample_bytecode = "608060405234801561001057600080fd5b50"
    instructions = disassemble_evm(sample_bytecode)
    for instr in instructions:
        print(f"0x{instr.pc:04x}: {instr.name} {instr.operand or ''}")
      
