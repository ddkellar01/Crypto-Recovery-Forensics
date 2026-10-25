![Crypto-Recovery-Forensics](https://raw.githubusercontent.com/ddkellar01/Crypto-Recovery-Forensics/main/184150538_1792962236776228.jpg)

🎬 **Video:** [Watch the demo]([PASTE_YOUR_VIDEO_LINK_HERE](https://labs.google/fx/tools/flow/shared/video/99dbf576-e240-4fb9-bac6-57aa2360ed59))

# 🔍 Crypto-Recovery-Forensics

> An educational toolkit for blockchain forensics, key derivation analysis, UTXO/EVM transaction tracing, and smart contract security research — built for self-custody recovery education and ledger transparency analysis.

## What is this?

A pure-Python forensics lab for Bitcoin and Ethereum. It takes the raw material of a wallet — seed phrases, keystores, extended public keys, raw transaction hex, EVM bytecode — and gives you **54 files of analyzers** that validate it, trace it, graph it, and export a forensic report. No web UI, no database, no lock-in: command-line modules that run locally or in a single Docker container.

---

## 🧰 Tech Stack Badges & Architecture

![Forensics Lab CI](https://img.shields.io/github/actions/workflow/status/ddkellar01/Crypto-Recovery-Forensics/ci.yml?branch=main&style=for-the-badge&logo=githubactions&label=Forensics%20Lab%20CI)
![Docker Publish](https://img.shields.io/github/actions/workflow/status/ddkellar01/Crypto-Recovery-Forensics/docker-publish.yml?branch=main&style=for-the-badge&logo=docker&label=Docker%20Publish)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![web3.py](https://img.shields.io/badge/web3.py-7.x-F16822?style=for-the-badge&logo=ethereum&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Architecture — one pipeline, five layers:**

```text
INPUT            seed phrase · keystore · xpub · raw tx hex · bytecode · address
  │
DERIVATION       BIP39 validation + entropy scoring → HD path checks → address formats
  │
CHAIN TRACERS    UTXO graph + clustering (BTC) · tx/bytecode/event decoding (EVM)
  │
AI LAYER         Gemini "Argon" analyzer — pattern & risk read on the traced evidence
  │
REPORTING        forensic_report_exporter → structured report in ./outputs
```

---

## 💻 Core Programming Languages & Core Systems

- **Python 3.10** — the entire toolkit, one language, zero compiled extensions
- **`src/` package layout** — 44 Python modules: flat analyzers plus three sub-packages
  - `src/ai/` — Gemini Argon analyzer
  - `src/derivation/` — entropy & derivation simulation
  - `src/forensics/` — clustering, bridge tracing, phishing decoding, OSINT, auditors
- **Module-per-tool design** — every analyzer runs standalone from the command line

## ⛓️ Web3 & Infrastructure

- **bip-utils** — BIP32/BIP39/BIP44 HD wallet derivation across chains
- **web3.py + eth-utils** — Ethereum JSON-RPC interaction, ABI/hex utilities
- **pyevmasm** — EVM bytecode assembly/disassembly at the opcode level
- **RPC endpoints (configurable, public defaults)** — Ethereum via PublicNode, Bitcoin via Blockstream API
- **Google Gemini (`google-genai`)** — the Argon AI analysis layer for code & transaction review

## ⚙️ Platform Support & Hardware Architecture

- **Runs anywhere Python 3.10 or Docker runs** — Linux, macOS, Windows (WSL2)
- **CPU-only** — no GPU, no accelerator, no special hardware
- **Slim container** — `python:3.10-slim` base image, single-service Compose stack
- **Offline-capable core** — seed, derivation, hex, and bytecode analysis need no network; only RPC balance/tracing calls go online

## ⚡ Low-Level Infrastructure & Performance

- **Raw transaction hex parsing** and block-header decoding — byte-level, no explorer middleman
- **EVM bytecode disassembly** down to individual opcodes for contract inspection
- **BIP39 entropy mathematics** — checksum validation, entropy scoring, partial-phrase permutation search space analysis
- **UTXO graph building + heuristic clustering** for coin-flow tracing
- **Pure-standard-dataflow design** — modules pass plain dicts/hex/JSON, so everything stays scriptable and audit-friendly

## 🛠️ DevOps & Build Tools

- **GitHub Actions** — `Forensics Lab CI` on every push/PR (SHA-pinned actions, least-privilege `contents: read` token, pip cache)
- **Docker Publish CI** — builds and pushes the image to **Docker Hub** on every push to `main`
- **Docker + Docker Compose** — `forensics-lab` service, `./outputs` volume for exported reports, `./src` live-mounted for development
- **pip + requirements.txt** — 5 pinned-floor dependencies, nothing else

---

## 🏛️ What Is This About?

Self-custody fails quietly: a mistyped seed word, a lost derivation path, a keystore with a forgotten structure, funds sitting in an address format you didn't know you had. And when crypto is stolen, victims get a raw hex string and no map. This project is the map — an open, educational lab that teaches how wallet recovery and on-chain forensics actually work by implementing every step in readable Python: how BIP39 entropy becomes keys, how UTXOs link into clusters, how EVM bytecode reveals what a contract really does, and how a phishing signature differs from a legitimate one.

https://labs.google/fx/tools/flow/shared/video/af69369a-b891-49e7-86bd-7712ce0c3017

## What this does?

**🌱 Seed & key recovery analysis**
`bip39_validator` · `bip39_entropy_calculator` · `mnemonic_dictionary_search` · `partial_phrase_permuter` · `derivation_scanner` · `entropy_bruteforce_simulator` · `hd_key_path_validator` · `extended_pubkey_analyzer` · `keystore_decryptor` · `address_format_converter` · `vanity_address_matcher` · `multi_sig_builder`

**₿ Bitcoin / UTXO forensics**
`tx_hex_parser` · `block_header_decoder` · `utxo_graph_builder` · `utxo_heuristic_clusterer` · `dust_utxo_filter` · `utxo_consolidation_planner` · `fee_rate_estimator` · `timelock_extractor` · `signature_malleability_checker` · `sweep_transaction_generator` · `rpc_balance_checker`

**Ξ EVM forensics**
`evm_bytecode_disasm` · `token_transfer_decoder` · `event_topic_filter` · `input_data_visualizer` · `contract_deploy_detector` · `nonce_gap_checker` · `gas_limit_simulator` · `reentrancy_pattern_scanner`

**🕵️ Cross-chain, phishing & OSINT**
`cross_chain_bridge_tracer` · `eip712_phishing_signature_decoder` · `token_allowance_auditor` · `localstorage_vault_parser` · `people_search_osint` · `earth_mapper`

**🤖 AI analysis & reporting**
`gemini_argon_analyzer` (Gemini Argon) · `forensic_report_exporter` — the Compose default entrypoint

## Why is this cool?

- **The whole discipline in one repo** — recovery math, UTXO tracing, EVM reverse engineering, and phishing detection are usually five separate tools; here they share one roof and one report format.
- **It teaches by being readable** — every technique is a short Python module you can open and learn from, not a black-box binary.
- **AI where it helps, math where it counts** — Gemini Argon reads the evidence; the entropy, derivation, and decoding underneath stay deterministic and verifiable.
- **Ships as one container** — clone, compose up, and the lab is running with reports landing in `./outputs`.

## What problems this solves?

- 🔑 **"My seed phrase doesn't work"** — validates checksums, scores entropy, hunts the wrong word, and checks the derivation paths your wallet actually used.
- 🧭 **"Where did the funds go?"** — builds the UTXO graph, clusters related addresses, traces bridge hops, and decodes the transfers into a readable trail.
- 🎣 **"Was that signature a scam?"** — decodes EIP-712 phishing signatures and audits token allowances before they drain a wallet.
- 📦 **"I can't read this contract"** — disassembles bytecode to opcodes and scans for reentrancy patterns and deploy artifacts.
- 📋 **"I need this as a report"** — exports the findings into a structured forensic report instead of terminal scrollback.

---

## How to install this?

### Option A — Local Python

**Step 1 — Clone the repo**
```bash
git clone https://github.com/ddkellar01/Crypto-Recovery-Forensics.git
cd Crypto-Recovery-Forensics
```

**Step 2 — Create a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Configure your environment**
```bash
cp env.example .env
```
Then edit `.env` and set:
- `GEMINI_API_KEY` — your Google Gemini key (for the Argon AI analyzer)
- `ETH_RPC_URL` — Ethereum JSON-RPC endpoint (defaults to PublicNode)
- `BTC_RPC_URL` — Bitcoin API endpoint (defaults to Blockstream)

**Step 5 — Run a module**
```bash
python -m src.bip39_validator
python -m src.utxo_graph_builder
python -m src.forensic_report_exporter
```

### Option B — Docker

**Step 1 — Clone** (same as above)

**Step 2 — Build and run with Compose**
```bash
docker compose up --build
```
This starts the `forensics-lab` service and runs the forensic report exporter, writing results to `./outputs`.

**Or plain Docker:**
```bash
docker build -t crypto-recovery-forensics-lab .
docker run --rm crypto-recovery-forensics-lab -m src.bip39_validator
```

## Requirements

- **Python 3.10+** (local path) or **Docker + Docker Compose** (container path)
- **pip** and an internet connection for `pip install` and RPC calls
- A **Gemini API key** — only for the AI analyzer module
- Optional: your own Ethereum/Bitcoin node endpoints (public defaults work out of the box)
- ⚠️ **Educational use only** — analyze your own wallets and data you are authorized to examine

---

## FULL project structure tree

```text
Crypto-Recovery-Forensics/
├── .github
│   └── workflows
│       ├── ci.yml
│       └── docker-publish.yml
├── scripts
│   └── docker_publish.sh
├── src
│   ├── ai
│   │   ├── __init__.py
│   │   └── gemini_argon_analyzer.py
│   ├── derivation
│   │   ├── __init__.py
│   │   └── entropy_bruteforce_simulator.py
│   ├── forensics
│   │   ├── __init__.py
│   │   ├── cross_chain_bridge_tracer.py
│   │   ├── earth_mapper.py
│   │   ├── eip712_phishing_signature_decoder.py
│   │   ├── localstorage_vault_parser.py
│   │   ├── people_search_osint.py
│   │   ├── token_allowance_auditor.py
│   │   └── utxo_heuristic_clusterer.py
│   ├── __init__.py
│   ├── address_format_converter.py
│   ├── bip39_entropy_calculator.py
│   ├── bip39_validator.py
│   ├── block_header_decoder.py
│   ├── contract_deploy_detector.py
│   ├── derivation_scanner.py
│   ├── dust_utxo_filter.py
│   ├── event_topic_filter.py
│   ├── evm_bytecode_disasm.py
│   ├── extended_pubkey_analyzer.py
│   ├── fee_rate_estimator.py
│   ├── forensic_report_exporter.py
│   ├── forensicsearth_mapper.py
│   ├── gas_limit_simulator.py
│   ├── hd_key_path_validator.py
│   ├── input_data_visualizer.py
│   ├── keystore_decryptor.py
│   ├── mnemonic_dictionary_search.py
│   ├── multi_sig_builder.py
│   ├── nonce_gap_checker.py
│   ├── partial_phrase_permuter.py
│   ├── reentrancy_pattern_scanner.py
│   ├── rpc_balance_checker.py
│   ├── signature_malleability_checker.py
│   ├── sweep_transaction_generator.py
│   ├── timelock_extractor.py
│   ├── token_transfer_decoder.py
│   ├── tx_hex_parser.py
│   ├── utxo_consolidation_planner.py
│   ├── utxo_graph_builder.py
│   └── vanity_address_matcher.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
├── env.example
└── requirements.txt
```

---

## ☁️ Cloud Providers

| Provider | Used for |
|---|---|
| **Docker Hub** | Published container image (`crypto-recovery-forensics-lab`) via Docker Publish CI |
| **GitHub Actions** | CI (Forensics Lab CI) and Docker publishing pipelines |
| **Google Gemini** | Argon AI analysis layer (`google-genai`) |
| **PublicNode** | Default Ethereum JSON-RPC endpoint |
| **Blockstream** | Default Bitcoin API endpoint |

---

**License:** MIT · **Author:** Darion Kellar ([@ddkellar01](https://github.com/ddkellar01))
