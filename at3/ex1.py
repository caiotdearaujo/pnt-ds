i = input() # variável para receber os suspeitos
suspeitos = i.split(",") # transforma os suspeitos recebidos no input acima, em lista

while True:
  # verifica se tem apenas um suspeito, se for verdade, o código irá parar.
  if len(suspeitos) == 1:
    nome_suspeito = suspeitos[0] # acessa o ultimo suspeito restante
    break
  
  acao = input()
  
  if acao == "Não encontrei nada no primeiro suspeito":
    suspeitos.pop(0) # retira o primeiro item da lista
  elif acao == "O último da lista está limpo":
    suspeitos.pop(-1) # retira o ultimo item da lista
  elif acao == "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita":
    # retira o elemento central da lista,
    # o meio da lista pode ser encontrado por len(suspeitos) // 2
    suspeitos.pop(len(suspeitos) // 2)
  elif acao == "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:":
    indice = int(input()) # recebe a posição do indivíduo
    suspeitos.pop(indice)
  elif acao == "Acho que temos mais uma opção a ser analisada…":
    suspeito = input()
    suspeitos.append(suspeito) # adiciona o suspeito recebido no input acima
  else:
    print("Isso não estava no combinado, a lista vai permanecer do mesmo jeito")
    
print(f"Acho que encontramos o suspeito. O seu nome é {nome_suspeito}, vamos salvar o Sam!")