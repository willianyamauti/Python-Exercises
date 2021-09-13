"""

validador de numero primos, para um  numero ser considerado primo deve ser divisivel apenas por 1 ou ele mesmo
sendo assim numeros primos não sao composto de produtos de outros numeros

"""

def checar_primo(numero):
    if numero % 2 == 0 and numero != 2:     #evita calcular numeros pares desnecessariamente
        return False
    elif numero == 2:
        return True
    for i in range(3, numero):
        if numero % i == 0:
            return False
    return True


numero = input('Digite o numero desejado: ')
if not numero.isdigit() or int(numero) < 1:
    print('Numero invalido, digite um numero inteiro maior que 1')
numero = int(numero)
print(f'O numero {numero} é primo!' if checar_primo(numero) else
      f'O numero {numero} não é primo!')
