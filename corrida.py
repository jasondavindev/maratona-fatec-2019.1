def list_int(e):
  return list(map(lambda x: int(x), e))

def ordena_por_id(e):
  return e[0]

qtd = int(input())

carros = []

for i in range(qtd):
  # [id, tempo]
  carros.append(list_int(input().split()))

tamanho, voltas = list_int(input().split())

carros_ord = sorted(carros, key=ordena_por_id)

for i in carros_ord:
  print(i[0], tamanho * voltas // i[1])