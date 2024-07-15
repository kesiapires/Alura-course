#Aprofundando em Propriedades
#colocar todos os atributos como privado

class Restaurante:
    restaurantes = []

    def __init__(self, _nome, _categoria):
        self._nome = _nome.title() #faz com que a primeira letra de cada palavra fique maiuscula
        self._categoria = _categoria.upper() #todas ficam maiusculas 
        #colocando o ativo como atributo privado '_'
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            #using 'ljust' method
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    #muda a forma que o atributo é lido
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
 
restaurante_praca = Restaurante('Praça','Gourmet') 
restaurante_pizza = Restaurante('Domino`s pizza', 'Fast Food')

Restaurante.listar_restaurantes()
print()
#Atalhos:
# f2 renomeia todos de uma só vez
