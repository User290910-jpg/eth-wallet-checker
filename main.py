from eth import cek_eth, contract_list, cek_saldo_token, cek_history
from export import export_csv

main_address = input("enter: ")
contract_address = contract_list()

cek_eth(main_address)

data_tx = cek_history(main_address)

cek_saldo_token(main_address, contract_address)

export_csv(data_tx)