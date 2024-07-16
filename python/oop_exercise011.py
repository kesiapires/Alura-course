#Crie uma nova classe chamada Pessoa com atributos como nome, 
#idade e profissão. Adicione um método especial __str__ para
#imprimir uma representação em string da pessoa. 
#Implemente também um método de instância chamado aniversario que 
#aumenta a idade da pessoa em um ano. 
#Por fim, adicione uma propriedade chamada saudacao 
#que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.


class Pessoa:
    
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    def __str__(self):
        print(f'{"Nome".ljust(25)} | {"Idade".ljust(25)} | {"Profissão".ljust(25)}')
        return f'{self.nome.ljust(25)} | {self.idade.ljust(25)} | {self.profissao.ljust(25)}'
    
    #propriedade
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá sou {self.nome}!'
        
    #metodo de instância
    def aniversario(self):
        self.idade +=1
    
pessoa1 = Pessoa(nome='Kesia',idade=26,profissao='Engenheira de software')
print(pessoa1.saudacao)