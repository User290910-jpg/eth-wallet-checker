# eth-wallet-checker

A lightweight command-line tool to inspect Ethereum wallet activity — built with Python and Web3.py.

## Features

- Check ETH balance
- Fetch transaction history with timestamps and gas fees
- Check ERC-20 token balances (only shows non-zero balances)
- Export transaction history to CSV

## Requirements

- Python 3
- web3
- requests

Install dependencies:

```bash
pip install web3 requests
```

## Setup

This project uses environment variables for API keys. Set them before running:

```bash
export api_key_rpc="your_infura_project_id"
export api_key="your_etherscan_api_key"
```

- Get your Infura RPC key at: https://infura.io
- Get your Etherscan API key at: https://etherscan.io/myapikey

## Usage

```bash
python3 main.py
```

Enter an Ethereum address when prompted. The tool will:

1. Print ETH balance
2. Print transaction history (latest 100 transactions)
3. Print non-zero ERC-20 token balances
4. Export transaction history to `file1.csv`

## Project Structure

```
eth-wallet-checker/
├── main.py       # Entry point
├── eth.py        # Ethereum logic (balance, history, tokens)
├── export.py     # CSV export
└── README.md
```

## Notes

- Built and tested on Termux (Android)
- ERC-20 contracts are hardcoded in `eth.py` — edit `contract_list()` to add or remove tokens
