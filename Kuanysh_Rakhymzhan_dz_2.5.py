def show_price(items, show_delim=True):
    for price in items:
        price = int(round(price * 100))
        rubles = price // 100
        cent = price % 100
        print(f' {rubles:02d} тенге {cent:02d} коп ', end=',')
    if show_delim:
        print()


prices = [57.8, 46.51, 97, 25.78, 84.66, 99.45, 16.78, 83.84, 31.85, 45.87, 23.45, 84.25, 64.82, 65.25, 48.73]
show_price(prices)
prices.sort()
show_price(prices)
prices_desc = sorted(prices, reverse=True)
show_price(prices_desc)
show_price(prices_desc[4::-1], False)

