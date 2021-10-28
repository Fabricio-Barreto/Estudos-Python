from cpf_cnpj import Documento
from telefone import TelefonesBr
from cep import BuscaEndereco
from data import DatasBr


telefone = "556198768274"

telefone_objeto = TelefonesBr(telefone)

print(telefone_objeto)

cpf = "59822433026"
cpf = str(cpf)

cpf_objeto = Documento()

cpf_objeto = cpf_objeto.cria_documento(cpf)

print(cpf_objeto)

objeto_data = DatasBr()

print(objeto_data)

cep = 72210000

objeto_cep = BuscaEndereco(cep)

print(objeto_cep)
