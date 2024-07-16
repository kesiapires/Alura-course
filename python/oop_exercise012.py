#Crie uma classe chamada ContaBancaria com um construtor 
#que aceita os parâmetros titular e saldo. 
#Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self.titular = titular
        self.saldo = saldo 
        self._ativo = False
    
#Na classe ContaBancaria, adicione um método especial __str__ que retorna 
#uma mensagem formatada com o titular e o saldo da conta. 
#Crie duas instâncias da classe e imprima essas instâncias.

    def __str__(self):
        return f'O titular {self.titular} tem {self.saldo} na conta.'

#Adicione um método de classe chamado ativar_conta à classe ContaBancaria 
#que define o atributo ativo como True. 
#Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(self,conta):
        conta._ativo = True


titular1 = ContaBancaria(titular='David',saldo=3700)
print(f'Conta de {titular1.titular} está ativa? {titular1._ativo}')
ContaBancaria.ativar_conta(titular1)
print(f'Agora a conta de {titular1.titular} está ativa? {titular1._ativo}')
titular2 = ContaBancaria('Kesia',1000)
print(titular1)
print(titular2)


#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" 
#na criação de atributos. Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo


#Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


#Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
#Instancie 3 objetos desta classe e atribua valores aos seus atributos 
#através do método construtor.
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")



#Crie um método de classe para a conta ClienteBanco.
@classmethod
def criar_conta(cls, titular, saldo_inicial):
    conta = ContaBancariaPythonica(titular, saldo_inicial)
    return conta
# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")




