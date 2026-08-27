from random import randint

seu_nome = input('Olá, qual seu nome? ')

print(f'Okay! {seu_nome}, eu estou escolhendo um número de 1 até 10. Você consegue adivinhar? ')

numero_adivinhado = randint(1, 10)

numero_tentativa = 3

for tentativa in range(1, numero_tentativa + 1):

    numero_escolhido = int(input('Escolha um número: '))

    if numero_escolhido == numero_adivinhado:
        print(f'Você acertou em {tentativa} tentativa! O número era {numero_adivinhado}!')
        break

    elif numero_escolhido > numero_adivinhado:
        print('Escolha um número menor!')

    else:
        print('Escolha um número maior!')

else:
    print(f'Você não conseguiu acertar! O número era {numero_adivinhado}.')

print('Obrigado por jogar!')