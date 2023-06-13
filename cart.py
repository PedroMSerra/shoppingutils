def calculate_total_price(cart):
    total = 0
    for item in cart:
        preco = item.get('preco', 0)
        total += preco
    return total

version='1.0.0'