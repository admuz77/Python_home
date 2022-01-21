# Napisz program przyjmujący ciąg znaków i obliczający ile jest w nim liter, a ile liczb
text = input('Podaj ciąg znaków: ')
# Sprawdzam typ
print(type(text))
## użycie isnumeric (czy jest cyfrą), isspace, isalpha (czy jest literą)
## zrezygowałam z liczenia czy wycinania spacji
# sprawdzam długość ciągu znaków
print(len(text))

# sprawdzę czy występują cyfry (przez isnumeric?), jeśli tak, to przełożę je do pustego numbers,
# a resztę za pomocą isalpha do pustego letters i wszystko podliczę

numbers = 0
letters = 0
specials = 0

for char in text:
    if char.isnumeric():
        numbers += 1
    elif char.isalpha():
        letters += 1
    else:
        specials += 1

print('Ilość cyfr:', numbers, 'Ilość liter:', letters, "Ilość innych znaków:", specials)

# Yeeeeeah!