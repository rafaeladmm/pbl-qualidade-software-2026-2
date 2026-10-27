
"""Regras de negocio relacionadas ao calculo de pedidos."""


def validar_item(item: dict) -> None:
    """Valida preco e quantidade de um item.

    Raises:
        ValueError: se o preco ou a quantidade nao forem positivos.
    """
    if item["preco"] <= 0:
        raise ValueError("O preco deve ser positivo.")

    if item["quantidade"] <= 0:
        raise ValueError("A quantidade deve ser positiva.")


def calcular_total(itens: list[dict]) -> float:
    """Calcula o total do pedido.

    Uma lista vazia resulta em total igual a zero.
    """
    total = 0

    for item in itens:
        validar_item(item)
        total += item["preco"] * item["quantidade"]

    return total



def calcular_taxa_entrega(distancia_km, total_pedido):
    """Calcula a taxa de entrega."""
    if total_pedido >= 100:
        return 0.00

    if distancia_km <= 3:
        return 5.00

    return 5.00 + (distancia_km - 3) * 2.00

