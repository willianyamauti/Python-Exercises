from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

memoria = [scissors, paper, rock]

while True:

    opcao = input(f'O que você escolhe? Digite 0 para tesouras, 1 para papel, 2 para pedra.\n')
    if not opcao.isnumeric() or int(opcao) > 2 or int(opcao) < 0:
        print(f'Opção invalida digite de acordo com as instruções.\n'
              f'Tente novamente!!!')
        continue
    opcao = int(opcao)

    opcao_computador = randint(0, 2)

    print(f'{memoria[opcao]}\n'
          f'\n O Computador escolhe:\n\n'
          f'{memoria[opcao_computador]}\n')

    if opcao == opcao_computador:
        print('Empate!\n')
        continue
    else:
        if (opcao - opcao_computador) % 3 == 1:
            print('Voce perdeu!\n')
        else:
            print('Voce ganhou!\n')
