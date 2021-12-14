# Konwersja stóp i cali na centymetry
# 1 ft = 12 cali
# 1 ft (angielska) = 30,480 cm
# 1 cm = 0,032808399 stopy

# /n to enter, czyli przejście do nowej linii
# daję użytkownikowi wybór czy chce przeliczać ft na cm, czy cm na ft
a = input("Wybierz jednostkę z której chcesz przeliczać:\nWpisz:\n'f' dla stopy lub \n'c' dla centymetrów\n")

# jeżeli użytkownik wybrał przeliczanie z ft na cm, to proszę o podanie wartości i podaję wynik
if a == 'f':
    x = float(input('Podaj ilość stóp, które chcesz zamienić na centymetry: '))
    result_x = x * 30.480
    print(f'{x} stóp to {result_x} centymetrów')
# jeżeli użytkownik wybrał przeliczanie z cm na ft, to proszę o podanie wartości i podaję wynik
elif a == 'c':
    y = float(input('Podaj ilość centymetrów, które chcesz zamienić na stopy: '))
    result_y = y * 0.032808399
    print(f'{y} centymetrów to {result_y} stóp')

# jeżeli użytkownik wpisał coś innego niż wybór ft lub cm komunikuję błąd i proszę o ponowne odpalenie programu.
# Możnaby jeszcze rozważyć zrobienie opcji z pętlą, by jeżeli zostało wprowadzone coś innego, by użytkownik wracał
# automatycznie do wyboru między cm a ft
else:
    print('Błąd przy wyborze. Wybierz f - dla stóp lub c dla centymetrów. Uruchom program ponownie.')

