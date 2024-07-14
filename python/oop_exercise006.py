#No Python, a criação de classes é uma parte essencial da programação orientada a objetos. 
#Abaixo, temos um exemplo de uma classe chamada Musica 
#que representa informações sobre uma música, como nome, artista e duração:

#class Musica:
#nome = ''
#artista = ''
#duracao = int

#Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, 
#aproveitando a sintaxe simplificada do Python.


class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao 

musica1 = Musica(nome='seja para mim',artista='maneva',duracao=120)
musica2 = Musica(nome='drão',artista='gilberto gil')
musica3 = Musica(nome='pra você dar o nome')

print(vars(musica3))