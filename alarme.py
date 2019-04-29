entrada = input().split()
a = int(entrada[0])
b = int(entrada[a + 1])

dt_a = set(entrada[1:a+1])
dt_b = set(entrada[a + 2:])

intersection = list(dt_a.intersection(dt_b))

if len(intersection) >= 3:
  intersection.append('PERIGO')
else:
  intersection.append('OK')

print(' '.join(intersection))