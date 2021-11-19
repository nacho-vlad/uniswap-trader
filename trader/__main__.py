
from uniswap import Uniswap

address = None          # or None if you're not going to make transactions
private_key = None  # or None if you're not going to make transactions
version = 3                       # specify which version of Uniswap to use
provider = "https://mainnet.infura.io/v3/562e9285316d4b029dbe472eae7e938b"    # can also be set through the environment variable `PROVIDER`

# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"


def main():
    uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)
    amount = 10**18
    recieved = uniswap.get_price_input(eth, dai, amount, fee=10000)
    print("For 1 eth you get: " + str(recieved) + " dai")
    recieved = uniswap.get_price_input(eth, dai, amount//2, fee=10000)
    print("For 1 eth you get: " + str(recieved*2) + " dai")
    


if __name__ == '__main__':
    main()
