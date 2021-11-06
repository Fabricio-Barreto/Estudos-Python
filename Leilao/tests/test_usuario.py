from app.dominio import Usuario, Leilao
import pytest

def usuario():
    vini = Usuario('vini', 100.0)

    leilao = Leilao('Celular')

    return vini, leilao

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    vini, leilao = usuario()

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira():
    vini, leilao = usuario()

    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_valor_da_carteira():
    with pytest.raises(ValueError):
        vini, leilao = usuario()

        vini.propoe_lance(leilao, 110.0)



def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_que_o_valor_da_carteira():
    vini, leilao = usuario()

    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0