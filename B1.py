numbers = input("Wpisz liczby oddzielając je przecinkami: ")
#sprawdzam typ
print(type(numbers))
#zmiana na listę
numbers_list = numbers.split(',')
print(numbers_list)
#zmiana na tuplę
print(tuple(numbers_list))

