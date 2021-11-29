n = int(input('Podaj liczbę by otrzymać jej silnię: '))
def silnia(n): return n*silnia(n-1) if n > 1 else 1
print(silnia(n))