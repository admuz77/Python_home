# # # #Definicja funkcji
# # # def sokowirowka(owoc):
# # #     print("Robię sok z ", owoc)
# # #     return "sok z " + owoc
# # #
# # # #Wywołanie funkcji
# # # sok = sokowirowka('jabłko')
# # #
# # # print(sok)
# #
# #
#
#
# #
# # a = 5
# #
# # def funkcja():
# #     a = 12
# #     b = 6
# #     print('Wartość a rowna się', a)
# #     print('Wartość b rowna się', b)
# #
# # funkcja()
# # print(a)
# # # ni da się wydrukować b bo jest tylko w funkcji zadeklarowane b, a poza funkcją nie istnieje
# #
#
#
# lista = [1, 2, 3]
# a = 5
#
# def zamien(lista):
#     lista [0] = 0
#     return lista
#
# def zamien2(a):
#     a = 0
#     return a
#
# zamien(lista)
# zamien2(a)
#
# print("a=", a)
# print("lista=", lista)



# # SŁOWNIKI
# en_to_es = {'cat' : 'gato', 'dog' : 'perro'}
#
# # lista nie moze byc typem w slowniku, bo jest niezmienna, ale krotka moze byc bo jest zmienna
# slownik = {'jeden': 1, 'dwa' : 2 }
# slownik2 = {'el1' : [1,2,3]}
#
# print(slownik2['el1'])
#
# print(en_to_es['cat'])
# en_to_es['mouse'] = 'el rato'
#
# print(en_to_es['mouse'])
# print(type(en_to_es))



# Tworzenie słownika
# klucz : wartość
en_to_es = {'cat' : 'gato', 'dog' : 'perro'}
# Pobranie elementu ze słownika
print(en_to_es['cat'])
# Dodanie nieistniejącego elementu
en_to_es['mouse'] = 'el rato'

# print(dir(dict))
# Wyświetl wartośći
print(en_to_es.values())
# Wyświetl klucze
print(en_to_es.keys())
# print(type(en_to_es))

#Wyświetl elementy
print(en_to_es.items())

print(en_to_es.get('mężczyzna'))
# Gdyby było tak to by zwróciło błąd: print(en_to_es.get['mężczyzna']), ten get powyżej jeśli brak mężczyzny w słowniku to zwraca "none", a jeśli jest coś w słowniku to to zwraca



for key in en_to_es:
    print(key)

print("Itemy: ", en_to_es.items())
for item in en_to_es.items():
    print("element", item, "typu", type(item))

# Iterowanie po parach klucz : wartość
for key, value in en_to_es.items():
    print(key, "->", value)

#sprawdzenie czy kot jest w słowniku przez in lub mozna czy nie ma jako not in
print('cat' in en_to_es)

print("Ile jest elementów w słowniku?", len(en_to_es))


# liczenie długości klucza, ale klucz jest mausem
print("klucz ->", key)
print("Ile jest elementów w słowniku?", len(key))