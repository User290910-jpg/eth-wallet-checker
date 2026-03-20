from web3 import Web3
import requests, json, sys, os
from datetime import datetime

api_key_rpc = os.environ.get('api_key_rpc')
api_key = os.environ.get('api_key')
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{api_key_rpc}"))

def cek_eth(main_address):
  try:
    saldo_wei = w3.eth.get_balance(main_address)
    saldo_eth = w3.from_wei(saldo_wei, "ether")
    print(f"ETH balance: {saldo_eth:.18f} ETH")
  except Exception as e:
    print(e)
    sys.exit()

def cek_history(main_address):
  url = f"https://api.etherscan.io/v2/api?chainid=1&module=account&action=txlist&address={main_address}&startblock=0&endblock=99999999&page=1&offset=100&sort=desc&apikey={api_key}"
  hasil_transaksi = []
  try:
    response = requests.get(url)
    data = response.json()
    transaksi = data["result"]
    for tx in transaksi:
      print("___","nonce", tx["nonce"],"___")
      timestamp = int(tx["timeStamp"])
      ts = datetime.fromtimestamp(timestamp)
      print(ts)
      print("from: ", tx["from"])
      print("to: ", tx["to"])
      val = w3.from_wei(int(tx["value"]), "ether")
      print("value: ", w3.from_wei(int(tx["value"]), "ether"), "ETH")
      gas_used = int(tx["gasUsed"])
      gas_price = int(tx["gasPrice"])
      fee_wei = gas_used * gas_price
      fee = fee_wei / 10**18
      fee_str = f"{fee:.20f}"
      print(f"txn fee: {fee:.20f} ETH")
      hasil_transaksi.append({
        "date": ts,
        "from": tx["from"],
        "to": tx["to"],
        "value": val,
        "fee": fee_str
      })
  except Exception as e:
    print(e)
  return hasil_transaksi

def contract_list():
  contract_address = [
  "0xdAC17F958D2ee523a2206206994597C13D831ec7",
  "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
  "0x514910771AF9Ca656af840dff83E8264EcF986CA",
  "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
  "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
  "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE",
  "0x6B175474E89094C44Da98b954EedeAC495271d0F",
  "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
  "0x455e53cbb86018ac2b8092fdcd39d8444affc3f6",
  "0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32"
  ]
  return contract_address

def cek_saldo_token(main_address, contract_address):
  abi = '[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"type":"function"}]'
  for x in contract_address:
    try:
      contract = w3.eth.contract(
        address=w3.to_checksum_address(x),
        abi=abi)
      symbol = contract.functions.symbol().call()
      decimals = contract.functions.decimals().call()
      saldo_raw = contract.functions.balanceOf(main_address).call()
      saldo = saldo_raw / 10**decimals
      if saldo > 0.0:
        print("symbol: ", symbol)
        print("decimals: ", decimals)
        print(f"saldo: {saldo} {symbol}")
    except Exception as e:
      print(e)
