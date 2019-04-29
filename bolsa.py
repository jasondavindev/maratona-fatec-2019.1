def list_int(e):
  return list(map(lambda x: int(x), e))

def ordena_por_lucro(e):
  return e[1]

tecido, qtd_min = list_int(input().split())

tecidos = []

for i in range(3):
  # [gasto, lucro]
  tecidos.append(list_int(input().split()))

rs = []

for i in tecidos:
  qtd = 0
  lucro = 0
  tmp_tecido = tecido

  j = 0

  if i[0] <= tmp_tecido:

    tmp_tecido -= i[0]
    qtd += 1
    lucro += i[1]

    while (j < len(tecidos)):
      if tecidos[j][0] <= tmp_tecido:
        tmp_tecido -= tecidos[j][0]
        qtd += 1
        lucro += tecidos[j][1]
        j = 0
      else:
        j += 1

    rs.append([qtd, (lucro + tmp_tecido)])

ordenado = sorted(rs, key=ordena_por_lucro, reverse=True)

sucesso = False

for i in ordenado:
  if i[0] >= qtd_min:
    sucesso = True
    print(i[1])
    break

if not sucesso:
  print("IMPOSSIVEL")