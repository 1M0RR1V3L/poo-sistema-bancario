from conta_poupanca import ContaPoupanca
from poo.conta.conta import Conta

class CriarPoupanca:
    if __name__ == '__main__':
        conta = Conta('21.342-7')
        poupanca = ContaPoupanca(Conta)
        poupanca.creditar(500.87)
        poupanca.debitar(45.00)

        print(conta.get_saldo())

        poupanca.render__juros(0.01)

        print(conta.get_saldo())