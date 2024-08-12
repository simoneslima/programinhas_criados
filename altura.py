print('Conversor de Metros e Centímetros para Pés e Polegadas:')
# Pergunta a altura do usuário em metros
altura = float(input('Qual é a sua altura em metros? '))

# Converte a altura de metros para pés
feet1 = 3.28084
altura_pes = altura * feet1

# Separa a parte inteira (pés) da parte decimal (polegadas)
pes = int(altura_pes)
polegadas = (altura_pes - pes) * 12

# Mostra o resultado
print("Sua altura é: {} pés e {:.1f} polegadas".format(pes, polegadas))



