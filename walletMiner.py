from colorama import Fore, Style
import requests
from bs4 import BeautifulSoup as bs
from requests.structures import CaseInsensitiveDict
from time import sleep
import os

with open('hits.txt', 'r') as hits_:
    hits_ = hits_.read()

while True:
    uri_ = "https://www.bitcoinlist.io/"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"

    req = requests.get(uri_, headers=headers)
    soup = bs(req.content, 'html.parser')
    wallets = soup.find_all('tr')

    checked = 0

    for wallet in wallets:
        getwallet = str(wallet.getText()).strip()
        privkey = getwallet.split()[0].strip()
        uncompaddy = getwallet.split()[1].strip()
        compaddy = getwallet.split()[2].strip()
        balance = getwallet.split()[3].strip()
        if "Private Key" in getwallet:
            pass
        else:
            checked += 1
            if float(balance) > 0:
                print(f"{privkey} {Fore.GREEN} > {balance} BTC{Style.RESET_ALL}")
                with open('hits.txt', 'w') as whits_:
                    whits_.write(f"{hits_}\n{privkey} | {balance} BTC")
                break
            else:
                print(f"{privkey} {Fore.RED} > {balance} BTC {Style.RESET_ALL}")
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')