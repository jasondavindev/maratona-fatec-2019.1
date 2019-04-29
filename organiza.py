def ordena_por_digito(e):
  return int(e[-1])

qtd = int(input())

ids = input().split()

print(' '.join(sorted(ids, key=ordena_por_digito)))