from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos incorreta!!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self._cpf = documento
        else:
            raise ValueError("Esse CPF é Inválido")

    def __str__(self):
        return self.padronizar()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def padronizar(self):
        mascara = CPF()
        return mascara.mask(self._cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self._cnpj = documento
        else:
            raise ValueError("Esse CNPJ é Inválido")

    def __str__(self):
        return self.padronizar()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def padronizar(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)
