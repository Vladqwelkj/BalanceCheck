import json, requests
address1 = "Write the correctx address( t1UGKeunkVVUBMfjEM9USEoapLKJMu7nchC ):\n"  #прием кошелька от пользователя(поменял для регулярного пользования. Надо прописать input()
address = 't1UGKeunkVVUBMfjEM9USEoapLKJMu7nchC' # для регулярного пользования сменил на статичный кошелек

def CheckCorrectWallet(address):
    while True:                                         #проверка корректности кошелька
        if len(address) == 35 and list(address)[0] == 'z':  #проверка на анонимность кошелька
            print('ERROR: Sorry, this wallet is anonymous. Unable to view balance')
            address = input("Write the address(not anonymous):\n")   # сброс значения адреса и предложение ввести другой
            continue
        elif len(address) == 35 and list(address)[0] == 't':  # если кошелек корректный, продолжить
            site = "https://api.zcha.in/v2/mainnet/accounts/" + address
            return site
            break
        else:
            print('ERROR: Sorry, you entered an incorrect address.')
            address = input("Write the correct address:\n") # сброс значения адреса и предложение ввести другой
            continue
        
def BalanceZec():           #получение баланса
    getApi = requests.get(CheckCorrectWallet(address))
    data = json.loads(getApi.text)
    return data['balance']

def RateRUB_ZEC():   #получение курса ZEC-RUB
    getApi = requests.get('https://api.coinmarketcap.com/v2/ticker/1437/?convert=RUB')
    data = json.loads(getApi.text)
    return data["data"]["quotes"]['RUB']["price"]

def RateUSD_ZEC():  #получение курса ZEC-USD
    getApi = requests.get('https://api.coinmarketcap.com/v2/ticker/1437/?convert=RUB')
    data = json.loads(getApi.text)
    return data["data"]["quotes"]['USD']["price"]

print('ZEC balance: ' + str(BalanceZec()))
print('ZEC balance in USD: ' + str(RateUSD_ZEC()*BalanceZec()))
print('ZEC balance in RUB: ' + str(RateRUB_ZEC()*BalanceZec()))
input()
