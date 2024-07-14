 #Métodos especiais

class Restaurant:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self) -> str:
        return f'{self.nome}| {self.categoria}'

restaurante_praca = Restaurant('Praça','Gourmet')
restaurante_pizza = Restaurant('Domino`s Pizza', 'Fast Food')

print(restaurante_pizza)
print(restaurante_praca)

#curiosidade: o self é um padrão do python, mas pode ser qualquer nome