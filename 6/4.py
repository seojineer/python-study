class Stock:
    market = "kospi"

a = Stock()
b = Stock()

print(a.market)
# kospi

print(b.market)
# kospi

print(Stock.market)
# kospi

a.market = "kosdaq"
b.market = "nasdaq"

print(a.market)
# kosdaq

print(b.market)
# nasdaq

print(Stock.market)
#"kospi
