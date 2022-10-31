from poo.conta.conta import Conta
class ContaPoupanca(Conta):

    def __init__(self, numero):
        super().__init__(numero)

    def render__juros(self, taxa):
        self.creditar(self.get_saldo() * taxa)
        
