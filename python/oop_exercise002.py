class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Cantina Italiana'

#Atribua o valor 'Italiana' ao atributo categoria 
#da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'

#Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(f'O nome do restaurante é: {restaurante_praca.nome}')

#Verifique o valor inicial do atributo ativo para a instância restaurante_praca 
#e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está inativo')

#Acesse o valor do atributo de classe categoria diretamente da classe Restaurante 
#e armazene em uma variável chamada categoria.
categoria = restaurante_praca.categoria

#Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

#Crie uma nova instância da classe Restaurante chamada restaurante_pizza 
#com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

#Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante_pizza.categoria)

#Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
print()
#Imprima no console o nome e a categoria da instância restaurante_pizza e restaurante_praca.
print(f'''Nome: {restaurante_pizza.nome}
Categoria: {restaurante_pizza.categoria}

Nome: {restaurante_praca.nome}
Categoria: {restaurante_praca.categoria}''')
