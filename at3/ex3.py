name = input() # recebe o nome do dono da lista
n = int(input()) # recebe a quantidade de filmes na lista
movies_and_ratings = [] # lista para armazenar os filmes e suas respectivas notas

# recebe n filmes e notas
for _ in range(n):
    movie_and_rating = input().split(' - ') # transforma a string recebida numa lista contendo o nome e a nota
    movie_and_rating[1] = float(movie_and_rating[1]) # converte a nota de str para float
    movies_and_ratings.append(movie_and_rating) # insere o par na lista de filmes e notas

# o primeiro for loop limita, a cada iteração, o segundo loop a ir até o i-ésimo último item da lista geral, pois os 
# ítens posteriores a ele já foram ordenados
for i in range(len(movies_and_ratings)):
    # este loop cria um ponteiro que vai do primeiro ao penúltimo item da lista limitada pelo loop superior, com o
    # objetivo de ordenar o restante da lista que não foi ordenado ainda, "borbulhando" os ítens com as menores notas,
    # neste caso, para o fim da lista, sendo o i-ésimo último item da lista, ao fim de cada iteração, o item de menor
    # nota encontrado no intervalo da lista limitada
    for j in range(len(movies_and_ratings) - 1 - i):
        # checa se a nota do j-ésimo item da lista é menor que a do item seguinte, se for, faz uma troca de posições
        # entre eles, sendo o principal mecanismo do algoritmo, o responsável pelo "borbulhamento", levando o item de
        # menor nota até a i-ésima posição
        if movies_and_ratings[j][1] < movies_and_ratings[j + 1][1]:
            temp = movies_and_ratings[j + 1] # guarda o par seguinte ao j-ésimo item temporariamente
            movies_and_ratings[j + 1] = movies_and_ratings[j] # coloca o j-ésimo item na posição seguinte
            movies_and_ratings[j] = temp # coloca o item guardado temporariamente na j-ésima posição

print(f'Os filmes sugeridos por {name} são:')

# imprime a lista ordenada
for i in movies_and_ratings:
    print(f'{i[0]} - {i[1]}')