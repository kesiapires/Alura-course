# @classmethod

class Restaurante:
    restaurantes = []

    def __init__(self, _nome, _categoria):
        self._nome = _nome.title() 
        self._categoria = _categoria.upper() 
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alterar_estado(self):
        self._ativo = not self._ativo
 
