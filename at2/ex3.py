temperatura = 30
fome = True
internet = 0

while True:
    entrada = input()

    if entrada == 'parar':
        break

    if entrada == 'ir para o grad':
        temperatura -= 5
        internet += 300
    elif entrada == 'sair para a rua':
        temperatura += 5
    elif entrada == 'comer uma quentinha':
        fome = False
    elif entrada == 'conectar no wifi':
        internet += 100
    else:
        print('Entrada inválida')

if temperatura >= 30:
    print('A temperatura aqui não está agradável')

if temperatura <= 25:
    print('Agora sim, está aconchegante')

if fome:
    print('Meu corpo precisa de comida')

if internet < 100:
    print('Essa conexão está horrível')

if not fome and temperatura <= 25 and internet >= 300:
    print('Finalmente um lugar preciso para mim!')
    