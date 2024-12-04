import os
import random
import requests
import sys
import time
from colorthon import Colors
from web3 import Web3
from eth_account import Account

# Terminal Title
def titler(text_title: str):
    sys.stdout.write(f"\x1b]2;{text_title}\x07")
    sys.stdout.flush()

# Clear Terminal
def clearNow():
    os.system("cls") if "win" in sys.platform.lower() else os.system("clear")

# Colors
red = Colors.RED
green = Colors.GREEN
cyan = Colors.CYAN
yellow = Colors.YELLOW
reset = Colors.RESET

# Fetch Rates
def fetch_rate(api_url, multiplier=1):
    try:
        req = requests.get(api_url)
        if req.status_code == 200:
            rate = req.json().get("rates", {}).get("usd", 0)
            return float(rate) * multiplier
    except Exception as e:
        print(f"{red}Error fetching rate: {e}{reset}")
    return 0
def print_big_text():
     big_text = """
╔═══╗╔════╗    ╔═══╗╔═══╗╔╗  ╔╗╔═══╗╔════╗╔═══╗
╚╗╔╗║╚══╗ ║    ║╔═╗║║╔═╗║║╚╗╔╝║║╔═╗║║╔╗╔╗║║╔═╗║
 ║║║║  ╔╝╔╝    ║║ ╚╝║╚═╝║╚╗╚╝╔╝║╚═╝║╚╝║║╚╝║║ ║║
 ║║║║ ╔╝╔╝     ║║ ╔╗║╔╗╔╝ ╚╗╔╝ ║╔══╝  ║║  ║║ ║║
╔╝╚╝║╔╝ ╚═╗    ║╚═╝║║║║╚╗  ║║  ║║    ╔╝╚╗ ║╚═╝║
╚═══╝╚════╝    ╚═══╝╚╝╚═╝  ╚╝  ╚╝    ╚══╝ ╚═══╝
                                               
                                               
                             
"""
     print(f"{green} {big_text}")
def eth_rate(amount):
    return fetch_rate("https://ethbook.guarda.co/api/v2/tickers/?currency=usd") * amount

def doge_rate(amount):
    return fetch_rate("https://dogecoin.atomicwallet.io/api/v2/tickers/?currency=usd") * amount

def bnb_rate(amount):
    return fetch_rate("https://bsc-nn.atomicwallet.io/api/v2/tickers/?currency=usd") * amount

# Check Balances
def check_balance(api_url, address):
    try:
        url = api_url.format(address)
        req = requests.get(url)
        if req.status_code == 200:
            return float(req.json().get("balance", 0))
    except Exception as e:
        print(f"{red}Error checking balance: {e}{reset}")
    return 0

# Main Execution
clearNow()
print_big_text()
# Download BIP39 File if not exists
bip39_file = "bip39.txt"
# Read BIP39 Words
with open(bip39_file, "r", encoding="utf-8") as f:
    words = f.read().splitlines()

# Variables
found = 0
usd = 0
z = 0

while True:
    z += 1
    titler(f"Generated: {z} | Found: {found} | USD: {usd}$")

    # Generate Random Mnemonic
    mnemonic = " ".join(random.choice(words) for _ in range(random.choice([12, 24])))

    # Generate Private Key and Ethereum Address
    private_key = Web3.keccak(text=mnemonic).hex()
    account = Account.from_key(private_key)
    eth_address = account.address

    # Dogecoin and BNB can follow similar address-generation logic
    doge_address = "DOGE_" + eth_address[3:]  # Mock generation for simplicity
    bnb_address = eth_address

    # Check Balances
    eth_balance = check_balance("https://ethbook.guarda.co/api/v2/address/{}", eth_address)
    doge_balance = check_balance("https://dogecoin.atomicwallet.io/api/v2/address/{}", doge_address)
    bnb_balance = check_balance("https://bsc-nn.atomicwallet.io/api/v2/address/{}", bnb_address)

    # Update USD Total
    usd += eth_rate(eth_balance) + doge_rate(doge_balance) + bnb_rate(bnb_balance)

    # Log and Save Found Addresses
    if eth_balance > 0 or doge_balance > 0 or bnb_balance > 0:
        found += 1
        with open("found.txt", "a") as f:
            f.write(f"\nMnemonic: {mnemonic}\nPrivate Key: {private_key}\n")
            if eth_balance > 0:
                f.write(f"ETH Address: {eth_address} | Balance: {eth_balance}\n")
            if doge_balance > 0:
                f.write(f"DOGE Address: {doge_address} | Balance: {doge_balance}\n")
            if bnb_balance > 0:
                f.write(f"BNB Address: {bnb_address} | Balance: {bnb_balance}\n")
        titler(f"Generated: {z} | Found: {found} | USD: {usd}$")

    print(f"[{z}] ETH: {cyan}{eth_address}{reset} Balance: {eth_balance}")
    print(f"[{z}] DOGE: {yellow}{doge_address}{reset} Balance: {doge_balance}")
    print(f"[{z}] BNB: {green}{bnb_address}{reset} Balance: {bnb_balance}")
    print("-" * 50)
