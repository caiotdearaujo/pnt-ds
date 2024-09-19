vilao1_nome = input()
vilao1_poder = int(input())
vilao1_local = int(input())
vilao1_destruicao = (vilao1_poder ** 2 * vilao1_local) / 2

vilao2_nome = input()
vilao2_poder = int(input())
vilao2_local = int(input())
vilao2_destruicao = (vilao2_poder ** 2 * vilao2_local) / 2

if vilao1_poder < 0 or vilao2_poder < 0:
    print("Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.")
elif vilao1_destruicao > vilao2_destruicao:
    print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao1_nome}.")
elif vilao1_destruicao < vilao2_destruicao:
    print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao2_nome}.")
elif vilao1_destruicao % 2:
    print("Vou chamar uns reforcos de outro universo... rsrs")
else:
    print("E quem disse que isso e problema meu? Vou chamar o senhor Stark.")
