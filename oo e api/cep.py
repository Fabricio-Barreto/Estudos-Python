import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.validar(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def __str__(self):
        return self.padronizar()

    def validar(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def padronizar(self):
        bairro, localidade, uf = self.acessa_via_cep()
        return "{}-{}, {} {} {}".format(self.cep[:4], self.cep[4:], bairro, localidade, uf)

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )