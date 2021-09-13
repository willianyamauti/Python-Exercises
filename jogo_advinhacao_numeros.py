from random import randint

logo = """
  ___      _       _       _                    _   _                                
 / _ \    | |     (_)     | |                  | \ | |                               
/ /_\ \ __| |_   ___ _ __ | |__   ___    ___   |  \| |_   _ _ __ ___   ___ _ __ ___  
|  _  |/ _` \ \ / / | '_ \| '_ \ / _ \  / _ \  | . ` | | | | '_ ` _ \ / _ \ '__/ _ \ 
| | | | (_| |\ V /| | | | | | | |  __/ | (_) | | |\  | |_| | | | | | |  __/ | | (_) |
\_| |_/\__,_| \_/ |_|_| |_|_| |_|\___|  \___/  \_| \_/\__,_|_| |_| |_|\___|_|  \___/ 

"""

def escolher_numero():
    numero_secreto = randint(1, 100)
    return numero_secreto

def conferir_palpite(resposta, input_usuario):
    if resposta == input_usuario:
        return True
    else:
        return False

def escolher_dificuldade(nivel):
    while nivel != 'facil' and nivel != 'dificil':
        print("Opcao invalida! escolha entre facil ou dificil.")
        nivel = input('escolha entre "facil"(10 tentativas) ou "dificil"(5 tentativas): ')

    chances = DIFICULDADE[nivel]

    return chances


DIFICULDADE = {
    'facil': 10,
    'dificil': 5,
    }


print(logo)
secreto = escolher_numero()
print(f'Bem vindo ao jogo de advinhação de numeros!!!!\n'
      f'estou pensando em um numero entre 1 e 100.')
nvl = input('escolha entre "facil"(10 tentativas) ou "dificil"(5 tentativas): ')
tentativas_restantes = escolher_dificuldade(nvl)
while tentativas_restantes > 0:
    print(f'Você tem {tentativas_restantes} chances de advinhar o numero.')
    palpite = int(input('Tente a sorte: '))
    tentativas_restantes -= 1
    if conferir_palpite(secreto, palpite):
        print(f'Você acertou! Parabens, você gastou {DIFICULDADE[nvl] - tentativas_restantes} tentativas !!!\n'
              f'Fim de jogo')
        quit()
    else:
        if palpite > secreto:
            print(f'Muito alto!\n'
                  f'Tente de novo.\n')
        else:
            print(f'Muito baixo!\n'
                  f'Tente de novo.\n')

print(f'Você Perdeu! O numero era: {secreto}\n'
              f'Fim de jogo')


