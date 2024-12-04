# Cryptocurrency Address Checker Script

## Project Description
This script generates random cryptocurrency wallet addresses for Ethereum, Dogecoin, and BNB. It then checks their balances using relevant APIs. The primary purpose of this script is **educational**, demonstrating how private keys and wallet addresses are generated and used securely and legally.

---

## Requirements
To run this script, the following Python libraries are required:

- `requests`
- `requests-random-user-agent`
- `cryptofuzz`
- `colorthon`
- `web3`
- `eth-account`

You can install them using the following command:
```bash
pip install requests requests-random-user-agent cryptofuzz colorthon web3 eth-account
```
## How to Run
Ensure you have Python 3.9 or later installed on your system.
Install the required libraries using the command above.
Make sure the bip39.txt file is available in the same directory as the script. 
Run the script:
```bash
python CryptocurrencyAddressChecker.py
```
## Disclaimer
Warning: This script is intended for educational purposes only.
The author is not responsible for any illegal use or misuse of this script.
Please ensure you use it legally and ethically and comply with the laws in your country.

## Additional Information
Wallets with discovered balances are saved in a file named found.txt in the same directory.

> The script supports the following cryptocurrencies: 
-Ethereum (ETH)
-Dogecoin (DOGE)
-Binance Coin (BNB)
## Contribution
If you wish to contribute to this project, feel free to open pull requests or create issues on the GitHub repository.
