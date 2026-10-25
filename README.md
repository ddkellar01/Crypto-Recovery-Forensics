# Crypto-Recovery-Forensics
An educational toolkit for blockchain forensics, key derivation analysis, UTXO/EVM transaction tracing, and smart contract security research. Designed strictly for self-custody recovery education and ledger transparency analysis.

crypto-recovery-forensics-lab/          <-- [ROOT DIRECTORY]
├── README.md                           <-- Documentation
├── SECURITY.md                         <-- Security policy
├── LICENSE                             <-- License file
├── requirements.txt                    <-- Dependencies (bip-utils, web3, etc.)
└── src/                                <-- [SOURCE FOLDER] Put the 10 scripts here
    ├── __init__.py                     <-- Empty file to make src a package
    ├── bip39_validator.py              <-- Script 1
    ├── derivation_scanner.py           <-- Script 2
    ├── tx_hex_parser.py                <-- Script 3
    ├── utxo_graph_builder.py           <-- Script 4
    ├── evm_bytecode_disasm.py          <-- Script 5
    ├── partial_phrase_permuter.py      <-- Script 6
    ├── rpc_balance_checker.py          <-- Script 7
    ├── address_format_converter.py     <-- Script 8
    ├── token_transfer_decoder.py       <-- Script 9
    └── timelock_extractor.py           <-- Script 10
    
