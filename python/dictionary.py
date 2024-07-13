#Crie um dicionário representando informações sobre uma pessoa como: nome, idade e cidade.
pessoa = {'nome':'Kesia', 'idade':25, 'cidade':'Porto'}
print(pessoa)


#Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.
pessoa['idade'] = 26
pessoa['profissão'] = 'Software Engineer'
del pessoa['cidade']
print(pessoa)


#Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros_quadrados = {x:x**2 for x in range(1,6)}
print(numeros_quadrados)


#Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
print(pessoa)
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário")
else:
    print("A chave 'nome' não existe no dicionário")


#Escreva um código que conte a frequência de cada 
#palavra em uma frase utilizando um dicionário.
frase = '''As coisas tangíveis
tornam-se insensíveis
à palma da mão.

Mas as coisas findas,
muito mais que lindas,
essas ficarão.'''
cont = {}
palavras = frase.split()
for i in palavras:
    cont[i] = cont.get(i,0) +1
print(cont)

