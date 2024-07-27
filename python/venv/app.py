import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' 
#ctrl b: fechar a aba
#ctrl j: fechar aba do terminal
#alt z: quebra a linha

response = requests.get(url)

#200 é que deu certo
#404 erro
if response.status_code == 200:
    dados_json = response.json()
    print(dados_json)
else:
    #não funciona
    print(f'O erro foi: {response.status_code}')