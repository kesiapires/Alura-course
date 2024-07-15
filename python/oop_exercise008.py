#property

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        #colocando o ativo como atributo privado '_'
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
    #erro de sintax    print(f'{'Nome do restaurante'.ljust(10)} | {'Categoria'.ljust(10)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            #using 'ljust' method
            print(f'{restaurante.nome.ljust(10)} | {restaurante.categoria.ljust(10)} | {restaurante.ativo}')
    #muda a forma que o atributo é lido
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
 
restaurante_praca = Restaurante('Praça','Gourmet') 
restaurante_pizza = Restaurante('Domino`s Pizza', 'Fast Food')

Restaurante.listar_restaurantes()


 