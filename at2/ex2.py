n = bazingas = 0

while True:
    if input() == 'Fim do Show!':
        break
    
    if input() == 'BAZINGA!':
        bazingas += 1
    
    n += 1

taxa_bazingas = bazingas / n * 100

if taxa_bazingas > 60:
    print("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")
elif 40 <= taxa_bazingas <= 60:
    print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")
else:
    print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")