import json, requests

__address__ = input("Write the correct address:\n")

def CheckCorrectWallet(address):
    global __address__
    while True:                                         #проверка корректности кошелька
        if len(__address__) == 35 and list(__address__)[0] == 'z':  #проверка на анонимность кошелька
            print('ERROR: Sorry, this wallet is anonymous. Unable to view balance')
            __address__ = input("Write the address(not anonymous):\n")   # сброс значения адреса и предложение ввести другой
            continue
        elif len(__address__) == 35 and list(__address__)[0] == 't':  # если кошелек корректный, продолжить
            site = "https://api.zcha.in/v2/mainnet/accounts/" + __address__
            return site
            break
        else:
            print('ERROR: Sorry, you entered an incorrect address.')
            __address__ = input("Write the correct address:\n") # сброс значения адреса и предложение ввести другой
            continue
        
        
def BalanceZec():           #getting balance info
    getApi = requests.get(CheckCorrectWallet(__address__))
    data = json.loads(getApi.text)
    return data['balance']


def RateRUB_ZEC():   #rate ZEC-RUB
    getApi = requests.get('https://api.coinmarketcap.com/v2/ticker/1437/?convert=RUB')
    data = json.loads(getApi.text)
    return data["data"]["quotes"]['RUB']["price"]


def RateUSD_ZEC():  #rate ZEC-USD
    getApi = requests.get('https://api.coinmarketcap.com/v2/ticker/1437/?convert=RUB')
    data = json.loads(getApi.text)
    return data["data"]["quotes"]['USD']["price"]


print('ZEC balance: ' + str(BalanceZec()))
print('ZEC balance in USD: ' + str(RateUSD_ZEC()*BalanceZec()))
print('ZEC balance in RUB: ' + str(RateRUB_ZEC()*BalanceZec()))
input('\nEnter for exit...')
