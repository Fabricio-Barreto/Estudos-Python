class Account:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extract(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposit(self, value):
        self.__saldo += value

    def withdraw(self, value):
        if value <= self.saldo + self.limite:
            self.__saldo -= value
        else:
            print("O valor {} passou o limite da conta".format(value))

    def transfer(self, value, destino):
        self.deposit(value)
        destino.withdraw(value)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, value):
        self.__limite = value

    @staticmethod
    def codigo_banco():
        return "001"


