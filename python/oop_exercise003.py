#Construtor

class Restaurant:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurant('Praça','Gourmet') 
restaurante_pizza = Restaurant('Domino`s Pizza', 'Fast Food')

print(restaurante_pizza)
#mostra onde está localizado na memória

print(dir(restaurante_pizza))
#o dir mostra todos os métodos que contem/ja vem quando definimos a classe

print(vars(restaurante_praca))
#vars é uma forma de mostrar em forma de texto (dicionário).