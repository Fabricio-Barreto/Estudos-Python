from extrator_url import *

extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOriginal=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

print("O tamanho da URL é",len(extrator_url))

print(extrator_url)

