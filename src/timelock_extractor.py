import pyevmasm

def check_timelock_opcodes(bytecode_hex: str) -> dict:
    if bytecode_hex.startswith("0x"):
        bytecode_hex = bytecode_hex[2:]
        
    instructions = pyevmasm.disassemble_all(bytes.fromhex(bytecode_hex))
    
    timestamp_instructions = []
    blocknum_instructions = []

    for instr in instructions:
        if instr.name == "TIMESTAMP": # 0x42 opcode
            timestamp_instructions.append(instr.pc)
        elif instr.name == "NUMBER":    # 0x43 opcode (block height)
            blocknum_instructions.append(instr.pc)

    return {
        "has_timestamp_check": len(timestamp_instructions) > 0,
        "timestamp_pcs": timestamp_instructions,
        "has_block_number_check": len(blocknum_instructions) > 0,
        "block_number_pcs": blocknum_instructions,
    }

if __name__ == "__main__":
    # Bytecode incorporating TIMESTAMP (0x42)
    sample_code = "608060405242600080fd"
    report = check_timelock_opcodes(sample_code)
    print(report)
  
