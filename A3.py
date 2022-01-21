# n = int(input('Podaj liczbę by otrzymać jej silnię: '))
# def silnia(n): return n*silnia(n-1) if n > 1 else 1
# print(silnia(n))

def silnia_r(n):
    # if n in (0,1):
    # if n <=1 :
    # if n == 0 or n ==1:
    if n <=1:
        return 1
    elif n > 1:
        return n * silnia_r(n-1)

print(silnia_r(5))