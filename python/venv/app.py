import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' 
#ctrl b: fechar a aba
#ctrl j: fechar aba do terminal
#alt z: quebra a linha

response = requests.get(url)

#200 é que deu certo
#404 erro
print(response)
if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })    
else:
    #não funciona
    print(f'O erro foi: {response.status_code}')
print(dados_restaurante['McDonald’s'])