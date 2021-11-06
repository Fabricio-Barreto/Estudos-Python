from app.dominio import Usuario, Leilao
import pytest

@pytest.fixture()
def usuario():
    return Usuario('vini', 100.0)

@pytest.fixture()
def leilao():
    leilao = Leilao('Celular')
    return leilao



def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(usuario, leilao):
    usuario.propoe_lance(leilao, 50.0)

    assert usuario.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(usuario, leilao):
    usuario.propoe_lance(leilao, 1.0)

    assert usuario.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_valor_da_carteira(usuario, leilao):
    with pytest.raises(ValueError):

        usuario.propoe_lance(leilao, 110.0)

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_que_o_valor_da_carteira(usuario, leilao):
    usuario.propoe_lance(leilao, 100.0)

    assert usuario.carteira == 0.0