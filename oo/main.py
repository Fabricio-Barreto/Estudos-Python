from account import Account
from movie import *

conta = Account(123, "Fabricio Barreto", 140, 1000)

conta.extract()

conta.deposit(200)

conta.extract()

conta.withdraw(300)

conta.extract()

vingadores = Movie('vingadores', 2018, 160)
vingadores.give_like()

walkingdead = Serie('Walking Dead', 2010, 10)
walkingdead.give_like()

movies_and_series = [vingadores, walkingdead]

myplaylist = PlayList("minha playlist", movies_and_series)

for programa in movies_and_series:
    print(programa)

for programa in myplaylist:
    print(programa)