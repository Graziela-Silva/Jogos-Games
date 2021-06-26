#Jogo de adivinhação
import random
print('\033[33mTente adivinhar o número que estou pensando! \nDica: ele é inteiro e está entre 1 e 10')
num = random.randint(1,10)
cont = 0
op = 's'
while op != 'n':
    n = int(input('\033[35mEm qual número eu pensei? '))
    if n != num:
        cont +=1
        print('\n\033[31mHá! você errou!')
        print('Você teve: {} tentativas \nNúmero pensado: {} \nNúmero escolhido: {}'.format(cont,num,n))
    else:
        cont +=1
        print('\n\033[32mParabéns! você acertou')
        print('Você teve: {} tentativas \nNúmero pensado: {} \nNúmero escolhido: {}'.format(cont,num,n))
    print('\n\033[36mDeseja continuar?')
    op = str(input('[S] Sim: \n[N] Não: \nOpção escolhida: ')).lower()
    if op not in 'sn':
        print('\n\033[mOpção inválida, saindo...')
        op = 'n'