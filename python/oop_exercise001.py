#Crie uma classe chamada Musica com os seguintes atributos 
#e crie 3 objetos definindo cada atributo..

class Musica:

    nome = ''
    artista = ''
    duracao = int

song1 = Musica()
song1.nome = 'Pra você dar o nome'
song1.artista = '5 a seco'
song1.duracao = 240

song2 = Musica()
song2.nome = 'Saudade boa'
song2.artista = 'Tiago Iorc'
song2.duracao = 180

song3 = Musica()
song3.nome = 'Bandolins'
song3.artista = 'Oswaldo Montenegro'
song3.duracao = 107

print(f'Nome da musica é {song3.nome} - nome do artista é {song3.artista} - e dura {song3.duracao}')