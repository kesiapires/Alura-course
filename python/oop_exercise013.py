#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, 
#autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo='',autor='',ano_publicacao=0):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponivel = True

#Na classe Livro, adicione um método especial str que retorna 
#uma mensagem formatada com o título, autor e ano de publicação do livro. 
#Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        print(f'{"Título".ljust(25)} | {"Autor".ljust(25)} | {"Ano de Publicação"}')
        return f'{self.titulo.ljust(25)} | {self.autor.ljust(25)} | {str(self.ano_publicacao).ljust(25)} '


#Adicione um método de instância chamado emprestar à classe Livro 
#que define o atributo disponivel como False. 
#Crie uma instância da classe, chame o método emprestar 
#e imprima se o livro está disponível ou não.
    def emprestar(self):
        self._disponivel = False



#Adicione um método estático chamado verificar_disponibilidade 
#à classe Livro que recebe um ano como parâmetro e retorna 
#uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis




livro1 =Livro('O pequeno príncipe', 'antonie',1943)
print(f'Antes de emprestar. Livro disponível? {livro1._disponivel}')
livro1.emprestar()
print(f'Depois de emprestar. Livro disponível? {livro1._disponivel}')
livro2 = Livro('a culpa é das estrelas', 'Jhon green', 2012)
print(livro1)
print(livro2)



#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.



#No arquivo biblioteca.py, empreste o livro chamando o 
#método emprestar e imprima se o livro está disponível ou não após o empréstimo.



#No arquivo biblioteca.py, utilize o método estático 
#verificar_disponibilidade para obter a lista de livros disponíveis 
#publicados em um ano específico.



#Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, 
#instancie dois objetos da classe Livro e 
#exiba a mensagem formatada utilizando o método str.



