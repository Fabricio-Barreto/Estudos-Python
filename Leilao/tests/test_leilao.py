from unittest import TestCase

from app.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.yuri = Usuario('Yuri', 500.0)
        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def valores(self):
        self.menor_valor_esperado = 100.0
        self.maior_valor_esperado = 150.0

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.valores()

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.valores()

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        fabricio = Usuario('Fabricio', 500.0)

        lance_do_fabricio = Lance(fabricio, 170.0)

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_fabricio)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 170.0

        self.valores()

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(1, len(self.leilao.lances))

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_deve_permitir_propor_um_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200)

        try:
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)
            self.fail(msg='Não lançou exceção')
        except ValueError:
            self.assertEqual(1, len(self.leilao.lances))

    def test_nao_deve_permitir_propor_um_lance_caso_o_usuario_seja_o_mesmo_2(self):
        lance_do_gui200 = Lance(self.gui, 200)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)

