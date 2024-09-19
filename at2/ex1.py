n = int(input())
pts_sheldon = pts_raj = 0

for i in range(n):
    escolha_sheldon = input()
    escolha_raj = input()

    if escolha_sheldon == escolha_raj:
        continue

    if escolha_sheldon == 'lagarto':
        if escolha_raj == 'spock':
            pts_sheldon += 1
        elif escolha_raj == 'tesoura':
            pts_raj += 1
    elif escolha_sheldon == 'spock':
        if escolha_raj == 'tesoura':
            pts_sheldon += 1
        elif escolha_raj == 'lagarto':
            pts_raj += 1
    elif escolha_sheldon == 'tesoura':
        if escolha_raj == 'lagarto':
            pts_sheldon += 1
        elif escolha_raj == 'spock':
            pts_raj += 1

if pts_sheldon > pts_raj:
    print("BAZINGA! EU SOU O SENHOR DA SALA!")
elif pts_sheldon < pts_raj:
    print("ENGOLE ESSA, SHELDON!")
else:
    print("Oh não, precisamos de outra rodada.")