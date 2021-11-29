#Program sprawdzający czy słowe jest palindromem (czytane od tyłu brzmi tak samo)
word = str(input("Wpisz słowo: "))
reverse_word = (word[::-1])
print (reverse_word)
if reverse_word == word:
    print("To jest palindrom")
else:
    print(f'{word} nie jest palindromem')
