#Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto 
#que também herda de Veiculo. 
#Adicione um novo atributo chamado tipo ao construtor, 
#indicando se a moto é esportiva ou casual.
from veiculos import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca,modelo)
        self.tipo = tipo

#Implemente o Método Especial str na Classe Filha (Moto): 
#Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) 
#e inclua a informação sobre o tipo da moto.
    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Status: {status} | Tipo: {self.tipo}'