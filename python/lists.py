#criando listas
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ["nome1","nome2","nome3","nome4"]
ano_nascimento_e_ano_atual = [1998,2024]

#criando lista e usando um loop para percorrer os itens
for i in numeros:
    print(i)
print()
#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for i in range(1,11,2):
        soma_impares +=i
print(soma_impares)
print()

#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10,0,-1):
    print(i)
print()

#Solicite ao usuário um número e, em seguida, 
#utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input("Digite um número: "))
for i in range(0,11):
     print(i,"x",numero,"=",i*numero)
print()

# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.
sum = 0
try:
    for i in numeros:
        sum += i
    print("A soma dos elementos é igual a: ",sum)
except Exception as e:
     print("Ocorreu um erro: ",e)
print()

#Construa um código que calcule a média dos valores em uma lista. 
#Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
sum = 0
try:
    for i in numeros:
        sum += i
        media = sum/len(numeros)
    print("A media dos valores dessa lista é: ",media)
except ZeroDivisionError:
    print("A lista está vazia. Não é possivel calcular a média.")
except Exception as e:
    print("Ocorreu um erro: ",e)