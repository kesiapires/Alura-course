#Crie um Arquivo Main (main.py): Crie um arquivo 
#chamado main.py no mesmo diretório que suas classes.

#Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. 
#Em seguida, crie três instâncias de Carro e Moto com 
#diferentes marcas, modelos, quantidade de portas e tipos.
from carros import Carro
from motos import Moto

carro1 = Carro('fiat', 'uno',4)
carro2 = Carro('mercedes', 'benz',2)
carro3 = Carro("Ford", "Fusion", 4)

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto('Honda', 'xre','esportiva')

#Exiba as Informações: Para cada instância, imprima no console as 
#informações utilizando o método str.

print(carro1)
print(carro2)
print(carro3)
print()
print(moto1)
print(moto2)
print(moto3)