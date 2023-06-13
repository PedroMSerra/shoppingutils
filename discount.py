def apply_discount(cart, discount):
    carrinho_desconto = []
    for item in cart:
        preco = item.get('preco', 0)
        desconto = preco * desconto_percentual / 100
        preco_desconto = preco - desconto
        item_desconto = {'produto': item['produto'], 'preco_desconto': discount}
        cart_desconto.append(item_desconto)
    return carrinho_desconto

version='1.0.0'