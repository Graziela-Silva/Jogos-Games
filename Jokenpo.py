import random
print('*'*25)
print('Vamos jogar jokenpô!!')
opcoes = ['Pedra','Papel','Tesoura']
computador = random.choice(opcoes).lower()
usuario = str(input('Sua escolha: ')).lower().strip()

while usuario != 'pedra' and usuario != 'papel' and usuario != 'tesoura':
    print('No jokenpô as opções de escolha são apenas: Pedra, Papel ou Tesoura')
    usuario = str(input('Escolha uma opção válida: ')).lower()
if computador == usuario:
    print('\nPensamos igual!! \nO jogo deu Empate!')
    print(f'Eu escolhi: {computador} \nVocê escolheu: {usuario}')
elif computador == 'pedra' and usuario == 'tesoura':
    print('\nHAHAHA!! Eu venci!!')
    print(f'Eu escolhi: {computador} \nVocê escolheu: {usuario}')
elif computador == 'tesoura' and usuario == 'papel':
    print('\nHAHAHA!! Eu venci!!')
    print(f'Eu escolhi: {computador} \nVocê escolheu: {usuario}')
elif computador == 'papel' and usuario == 'pedra':
    print('\nHAHAHA!! Eu venci!!')
    print(f'Eu escolhi: {computador} \nVocê escolheu: {usuario}')
elif computador == 'pedra' and usuario == 'papel':
    print('\nParabéns!! Você venceu!!')
    print(f'Eu escolhi: {computador} \nVocê escolheu: {usuario}')
elif computador == 'papel' and usuario == 'tesoura':
    print('\nParabéns!! Você venceu!!')
    print(f'Eu escolhi: {computador} \nVocê escolheu: {usuario}')
else:
    print('\nParabéns!! Você venceu!!')
    print(f'Eu escolhi: {computador} \nVocê escolheu: {usuario}')