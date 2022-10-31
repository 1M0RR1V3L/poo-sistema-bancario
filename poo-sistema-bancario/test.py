from conta_especial import ContaEspecial
from poo.conta.conta import Conta

class teste():
    conta = Conta("31.345-X")
    conta.creditar(20)
    especial = ContaEspecial("31.567-X")
    conta.creditar(20)
    conta = especial
    conta.creditar(20)
    print(type(Conta))
    conta = especial
    conta.creditar(20)
    print(type(conta))
