def low_stock(stock, threshold):
    names = []
    for name, count in stock.items():
        if count < threshold:
            names.append(name)
    return sorted(names)
