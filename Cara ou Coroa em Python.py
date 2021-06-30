import random
print('-='*15)
print('Vamos jogar cara ou coroa!')
opcoes = ['Cara','Coroa']
print('\nJogando a moeda...')
computador = random.choice(opcoes)
usuario = str(input('\nO que você acha que deu? ')).strip().capitalize()
while usuario != 'Cara' and usuario != 'Coroa':
    print('\nA resposta deve ser cara ou coroa')
    usuario = str(input('\nO que você acha que deu? ')).strip().capitalize()
if (usuario == computador):
    print('Parabens! você acertou')
    print(f'Você escolheu: {usuario} \nO sorteio também deu: {computador}')
else:
    print('Tente novamente!')
    print(f'Você escolheu: {usuario} \nO sorteio deu: {computador}')
    