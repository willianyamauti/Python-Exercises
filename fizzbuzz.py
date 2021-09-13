""""

coutn the numbers from 1 to x

if n % 3 == 0 - print fizz
if n % 5 == 0 - print buzz
if n % 3 == 0 and n % 5 == 0 - print fizz buzz
else print n


"""

while True:
    range_n = input('Escolha o tamanho do fizzbuzz: ')

    if not range_n.isnumeric() or int(range_n) < 0:
        print('Invalido! digite um numero inteiro!')
        continue

    range_n = int(range_n)
    for n in range(1, range_n):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)
