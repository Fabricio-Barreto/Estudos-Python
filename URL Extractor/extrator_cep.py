import re

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
