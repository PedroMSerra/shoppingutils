def check_availability(cart):
    total_itens = len(cart)
    total_preco = sum(item.get('preco', 0) for item in cart)
    produtos = [item.get('produto', '') for item in cart]

    inventario = {
        'total_itens': total_itens,
        'total_preco': total_preco,
        'produtos': produtos
    }

    if inventario == 0:
        return 'false'

    return inventario

version='1.0.0'