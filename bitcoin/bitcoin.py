import sys
import requests

if(len(sys.argv)==1):
    sys.exit("Missing command-line argument")
if(len(sys.argv)>2):
    sys.exit("Invalid usage")
try:
    number_bitcoins=float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_price=r.json()
    price=float(bitcoin_price["bpi"]["USD"]["rate_float"])
    amount=price*number_bitcoins
except requests.RequestException:
    sys.exit("Request error")
except ValueError:
    sys.exit("Invalid bitcoin price")

print(f"${amount:,.4f}")