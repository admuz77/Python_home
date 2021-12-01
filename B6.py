#Zliczać 4 do listy

from random import randint

how_many = int(input("Ile liczb wylosować? "))
list = []
for i in range(0, how_many):
    list.append(randint(0, 100))
print(list)

added = int(input("Jaką liczbę chcesz dodać? "))
if added == 4:
    list.append(added)
    print(f'{added} może zostać dodana do listy. Aktualna lista zawiera:')
    print (list)
elif added != 4:
    print (f'{added} nie może zostać dodana do listy. Aktualna lista zawiera:')
    print (list)
