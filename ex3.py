"""Faça a soma do carrinho usando list comprehension"""

carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 50))

total = sum([float(y) for x, y in carrinho])
print(total)