def pedido_atingiu_valor_minimo(valor_pedido):
    """Retorna True quando o pedido atinge R$ 30,00 ou mais.

    Valores negativos não são aceitos e geram ValueError.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    return valor_pedido >= 30
