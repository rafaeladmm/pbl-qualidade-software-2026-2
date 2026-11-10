import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo


# Responsável: Rafaela Martins

def test_pedido_com_valor_igual_ao_minimo_retorna_true():
    resultado = pedido_atingiu_valor_minimo(30)
    assert resultado is True


def test_pedido_abaixo_do_minimo_retorna_false():
    resultado = pedido_atingiu_valor_minimo(29.99)
    assert resultado is False


def test_pedido_com_valor_negativo_gera_value_error():
    with pytest.raises(ValueError, match="não pode ser negativo"):
        pedido_atingiu_valor_minimo(-1)
