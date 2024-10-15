qtd_mochilas = int(input())

# Considerando n = qtd_mochilas, cria e armazena numa lista n mochilas, já
# contendo Lanterna e Omega 3 da top therm. As mochilas terão seus respectivos
# nomes e tamanhos listados no mesmo index em que elas estão armazenadas.
mochilas = [['Lanterna', 'Omega 3 da top therm'] for _ in range(qtd_mochilas)] 
nomes_mochilas = input().split()
tamanhos_mochilas = []

for _ in range(qtd_mochilas):
    tamanho_mochila = int(input())
    tamanhos_mochilas.append(tamanho_mochila)

qtd_itens = int(input())

for _ in range(qtd_itens):
    nome_item = input()
    mochila_item = int(input())
    
    # Se o tamanho atual da mochila for igual (ou maior, por precaução) que seu
    # tamanho máximo, ela está cheia.
    if len(mochilas[mochila_item]) >= tamanhos_mochilas[mochila_item]:
        print('Mochila cheia. Não vai dar para levar.')
        continue

    # Se ela não estiver cheia, há a adição do item na mochila.
    mochilas[mochila_item].append(nome_item)

while True:
    acao = input()

    if acao == 'Tirar da mochila':
        item = input()
        mochila = int(input())

        if item in mochilas[mochila]:
            mochilas[mochila].remove(item)
            print(f'{item} usado com sucesso da mochila {mochila}.')
        else:
            print(f'Você não tem {item} na mochila {mochila}.')
    elif acao == 'Guardar na mochila':
        item = input()
        mochila = int(input())

        # Novamente, se o tamanho atual da mochila for igual (ou maior, por 
        # precaução) que seu tamanho máximo, ela está cheia.
        if len(mochilas[mochila]) >= tamanhos_mochilas[mochila]:
            print(f'Mochila {mochila} cheia!')
        else:
            mochilas[mochila].append(item)
            print(f'{item} adicionado na mochila {mochila}.')
    elif acao == 'CHEGAMOS NO CIN!':
        break
    else:
        print('Ação inválida.')

for i in range(qtd_mochilas):
    print(f'Mochila de {nomes_mochilas[i]} chegou assim:')

    # Se a mochila não estiver vazia, seus ítens são listados.
    if mochilas[i]:
        print(*mochilas[i], sep='\n')