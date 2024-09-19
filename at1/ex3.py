cidade1_nome = input()
cidade1_nota = float(input())
cidade1_distancia = int(input())

cidade2_nome = input()
cidade2_nota = float(input())
cidade2_distancia = int(input())

cidade3_nome = input()
cidade3_nota = float(input())
cidade3_distancia = int(input())

melhor_cidade_nome = None
melhor_cidade_nota = None
melhor_cidade_distancia = None

if cidade1_nota >= 4 and (melhor_cidade_nome is None or cidade1_distancia < melhor_cidade_distancia):
    melhor_cidade_nome = cidade1_nome
    melhor_cidade_nota = cidade1_nota
    melhor_cidade_distancia = cidade1_distancia

if cidade2_nota >= 4 and (melhor_cidade_nome is None or cidade2_distancia < melhor_cidade_distancia):
    melhor_cidade_nome = cidade2_nome
    melhor_cidade_nota = cidade2_nota
    melhor_cidade_distancia = cidade2_distancia

if cidade3_nota >= 4 and (melhor_cidade_nome is None or cidade3_distancia < melhor_cidade_distancia):
    melhor_cidade_nome = cidade3_nome
    melhor_cidade_nota = cidade3_nota
    melhor_cidade_distancia = cidade3_distancia

if melhor_cidade_nome is None:
    print("Nota mínima não atingida")
else:
    print(melhor_cidade_nome)