empate, vitoria = list(map(lambda x: int(x), input().split()))
rodadas = int(input())
pontos = int(input())

vitorias = pontos // vitoria
empates = (pontos % vitoria) // empate
derrotas = rodadas - (vitorias + empates)

print(vitorias, 'vitoria(s)')
print(empates, 'empate(s)')
print(derrotas, 'derrota(s)')