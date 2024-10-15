name = input()
n1 = int(input())
meals1, notes1 = [], []

for _ in range(n1):
    meal, note = input().split('-')
    note = int(note)

    if meal in meals1:
        # Adquire o index da comida e sua respectiva nota anterior.
        index = meals1.index(meal)

        if notes1[index] < note:
            notes1[index] = note
            continue

        if notes1[index] > note:
            continue
        
        # Se a nota for igual, há a remoção da comida e da nota da lista para
        # que a readição ocorra em seguida, desta vez na posição correta.
        meals1.pop(index)
        notes1.pop(index)

    meals1.append(meal)
    notes1.append(note)

print(f'AVALIAÇÃO DE {name.upper()}:')
print(*notes1, sep=', ') # Exibe todas as notas da primeira rodada.

# Calcula a média aritmética inteira e a exibe.
print(f'Média inicial: {sum(notes1) // len(notes1)}')

n2 = int(input())
meals2, notes2 = [], []

for _ in range(n2):
    meal, note = input().split('-')
    note = int(note)

    meals2.append(meal)
    notes2.append(note)

# As listas gerais iniciam-se a partir de cópias do estado final das listas do 
# primeiro round.
all_meals, all_notes = meals1.copy(), notes1.copy()
retried_meals_and_note_differences = []

for i in range(len(meals2)):
    # Se a refeição não estava presente na lista do primeiro round, ela é
    # adicionada ao final da lista geral.
    if meals2[i] not in all_meals:
        all_meals.append(meals2[i])
        all_notes.append(notes2[i])
        continue
    
    # Caso ela estiver presente, primeiro adquire-se seu index na lista geral,
    # calcula-se a diferença entre a nota mais recente e a anterior, adiciona-
    # -se o nome da refeição repetida e sua respectiva diferença de
    # nota em forma de par a uma lista destes pares e, por fim, reatribui-se a
    # nota na posição da nota anterior.
    index = all_meals.index(meals2[i])
    note_difference = notes2[i] - all_notes[index]
    retried_meals_and_note_differences.append([meals2[i], note_difference])
    all_notes[index] = notes2[i]

print(*all_notes, sep=', ') # Exibe todas as notas da lista geral.

# Calcula a média aritmética inteira da lista geral e a exibe.
print(f'Média final: {sum(all_notes) // len(all_notes)}')

# Se a lista geral for maior que a lista do primeiro round, significa que novas
# refeições foram experimentadas no segundo round.
if len(all_meals) > len(meals1):
    print('Os potenciais novos sarros experimentados foram:')
    print(*all_meals[len(meals1):], sep=', ')

if retried_meals_and_note_differences:
    for i in retried_meals_and_note_differences:
        print(f'{i[0]}: {i[1]}')
else:
    print('Sem mudanças em receitas anteriores.')