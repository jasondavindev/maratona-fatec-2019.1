import math

def get_comprimento(b1, b2):
  return math.sqrt((bolas[b1][0] - bolas[b2][0]) ** 2 + (bolas[b1][1] - bolas[b2][1]) ** 2)

qtd = int(input())
bolas = []

for i in range(qtd):
  bolas.append(list(map(lambda x: int(x), input().split())))

comprimento = 0

for i in range(0, qtd - 1):
  comprimento += get_comprimento(i, i + 1)

comprimento += get_comprimento(0, len(bolas) - 1)

print('%.2f' % comprimento)