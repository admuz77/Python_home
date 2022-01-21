# Napisz program sprawdzający, czy podana liczba jest liczbą pierwszą.
n = int(input("Podaj liczbę: "))

is_prime = True
value_sqtr = int(n ** 0.5)
for x in range (2,value_sqtr+1):
    if n % x == 0:
        is_prime = False
        print(f'{x} jest dzielnikiem')

if is_prime:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")


# # zadanie Zuzanny
# num = int(input("Wpisz liczbę: "))
# if num > 1:
# for i in range(2, num):
# if (num % i) == 0:
# print(num, "to nie jest liczba pierwsza")
# break
#
#  else:
# print(num, "to jest liczba pierwsza")
#
# else:
# print(num, "to nie jest liczba pierwsza, musi być większa od 1")