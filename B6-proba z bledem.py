#Zliczać 4 do listy

values = []
value = int(input('Podaj liczbę: '))
for i in value:
    if i % 4 == 0:
        values.append(i)
print(values)
