#Lista de exercicios

#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
#Crie uma instância dessa classe e atribua valores aos seus atributos.
#implementando:
class Carro:
    def __init__(self, modelo='', cor='', ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
#instanciando:
carro1 = Carro(modelo='Fiat uno',cor='vermelho',ano=2013)
carro2 = Carro(modelo='chevrolet celta',cor='preto',ano=2024)
print(vars(carro1))
print(vars(carro2))
print()
#Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo 
#e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self,nome='',categoria='',cidade='',instagram='',avaliacao=0,ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.avaliacao =avaliacao
        self.ativo = ativo
        self.instagram = instagram
        self.cidade = cidade
    def __str__(self) -> str:
        return f'{self.nome} | {self.categoria} | {self.avaliacao} | {self.instagram} | {self.cidade} | {self.ativo}'
#instanciando:
restaurante1 = Restaurante()
restaurante2 = Restaurante(nome='cantina italiana',categoria='italiano',cidade='sao paulo', avaliacao=9, ativo=True)
restaurante3 = Restaurante(nome='Vacaria',categoria='churrascaria', avaliacao=8)
print(restaurante1)
print(restaurante2)
print(restaurante3)
print()

#Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como
#parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.


#Adicione um método especial __str__ à classe Restaurante para que, 
#ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. 
#Exiba essa mensagem para uma instância de restaurante.



#Crie uma classe chamada Cliente e pense em 4 atributos. 
#Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos 
#através de um método construtor.
class cliente:
    def __init__(self,nome='',email='',telefone=0):
        self.nome = nome
        self.email = email
        self.telefone = telefone
cliente1 = cliente(nome='Sara',email='Sara123@gmail.com',telefone=98664332)
print(vars(cliente1))
print()