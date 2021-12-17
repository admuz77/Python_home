# Robot porusza się po płaszczyźnie począwszy od punktu (0,0). Może się on poruszać do góry,
# na dół, w lewo oraz w prawo dla podanej liczby kroków. Napisz program obliczający odległość
# od punktu (0,0) po wykonaniu sekwencji kroków podanych z klawiatury. Program powinien zwracać
# liczbę całkowitą (zaokrągloną).

u = int(input('Ile kroków do góry: '))
d = int(input('Ile kroków w dół: '))
r = int(input('Ile kroków w prawo: '))
l = int(input('Ile kroków w lewo: '))

print(f'do góry: {u} \ndo dołu: {d} \nw prawo: {r} \nw lewo: {l}')

# odległość w osi y
d_minus = - (d)
result_y = u + d_minus
print(f'Odległość od osi y to {result_y}')

# odległość w osi x
l_minus = - (l)
result_x = r + l_minus
print(f'Odległość od osi x to {result_x}')

# Wyliczyć odległość od pkt 0,0 na podstawie obliczania długości boków trójkąta
# Najpierw zamieniamy wszystko na liczby bezwzględne przez funkcję abs

absolute_x = abs(result_x)
absolute_y = abs(result_y)

# Pierwiastek kwadratowy to potęgowanie do 1/2
distance = (absolute_x **2 + absolute_y **2)**1/2
print(int(distance))

