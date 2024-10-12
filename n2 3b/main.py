fase = 0
bazinga_retrocede = True
avancou_na_ultima = False

while True:
    i = input()

    if i == 'É o fim da Estrada pra Sheldon Cooper':
        break
    if i == 'Ganhar o Nobel' and fase == 5:
        fase += 1
        break
    
    if i == 'Bazinga' and not avancou_na_ultima:
        bazinga_retrocede = False
    elif i == 'Bazinga' and bazinga_retrocede:
        fase -= 1
    elif i == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or\
         i == 'Leonard seu anão covarde' or\
         i == 'Tu é muito burro Raj':
        print('Não xingue seus amigos Sheldon!')
    elif (i == 'Começou a Trabalhar na Caltech' and fase == 0) or\
         (i == 'Trabalho sobre a String Theory' and fase == 1) or\
         (i == 'Ganhar o Chancellor de ciência' and fase == 2) or\
         (i == 'Pensar na Teoria de Cooper-Hofstader' and fase == 3) or\
         (i == 'Criou a Super Assimetria' and fase == 4):
        fase += 1
        avancou_na_ultima = True
        continue

    avancou_na_ultima = False   

if fase == 0:
    print('Que potencial desperdiçado...')
elif 1 <= fase <= 2:
    print('Tão perto, mas tão longe')
elif 3 <= fase <= 4:
    print('Não desista Sheldon, você ainda têm muito para alcançar!')
elif fase == 5:
    print('Nãoooooo, esse momento ia ser seu Sheldon')
elif fase == 6:
    print('Você conseguiu Sheldon, o Nobel é seu!!!')