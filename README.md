# litecoin-bech32

> ltc · bech32 · mweb-shaped

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

Litecoin bech32 account helper — stub RPC, labeled accounts.

## Features

- HD derivation along m/84'/2'/0' for LTC
- Passphrase-wrapped vault stored as local JSON
- Deterministic address codec (SHA-256 simulation, no live keys)
- Fee estimator with low / medium / high presets
- Balance sync against a stub RPC client
- Click CLI with vault, account and portfolio commands

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd litecoin-bech32
python -m pip install -e .
python -m ltcbech32 --help
```

## CLI Usage

```bash
ltcbech32 create-vault --name "Main"
# Create an encrypted local vault

ltcbech32 list-vaults
# List vault files in the storage directory

ltcbech32 add-account --label Savings
# Derive the next HD account

ltcbech32 sync
# Refresh stub balances

ltcbech32 balance
# Print account table

ltcbech32 portfolio
# Show coin + stub USD total
```

## Project Structure

```
ltcbech32/
  crypto/          seed, derive, address
  chain/           stub RPC and fee table
  storage/         vault JSON
  services/        wallet + sync
  cli.py           click entry
tests/             pytest
```

## Configuration

Defaults live in `ltcbech32/config.py` (`WalletConfig`).

| Setting | Default | Description |
|---------|---------|-------------|
| `network` | `mainnet` | mainnet / testnet |
| `rpc_endpoint` | `http://127.0.0.1:9332` | LTC node URL (unused in stub mode) |
| `storage_dir` | `.wallets` | Local vault directory |
| `derivation_path` | `m/84'/2'/0'` | BIP path |

## Tests

```bash
python -m pytest -q
```

## Background

LTC scripts want bech32 in the slug, not another bitcoin clone.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![litecoin](https://img.shields.io/badge/litecoin-111827?style=flat-square) ![bech32](https://img.shields.io/badge/bech32-111827?style=flat-square) ![litecoin-bech32](https://img.shields.io/badge/litecoin%20bech32-111827?style=flat-square) ![cryptocurrency](https://img.shields.io/badge/cryptocurrency-111827?style=flat-square) ![wallet](https://img.shields.io/badge/wallet-111827?style=flat-square) ![blockchain](https://img.shields.io/badge/blockchain-111827?style=flat-square) ![web3](https://img.shields.io/badge/web3-111827?style=flat-square) ![bitcoin](https://img.shields.io/badge/bitcoin-111827?style=flat-square)

`litecoin` `bech32` `litecoin-bech32` `cryptocurrency` `wallet` `blockchain` `web3` `bitcoin` `ethereum` `hd-wallet` `open-source` `python`

Search: litecoin-bech32 · ltc · bech32 · mweb-shaped · Litecoin bech32 account helper — stub RPC, labeled accounts.

---

<sub>Litecoin bech32 account helper — stub RPC, labeled accounts.</sub>
