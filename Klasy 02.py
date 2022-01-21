# Stwórz 2 klasy dziedziczące po klasie Pracownik:
# - Informatyk
# - Ksiegowy
# Informatyk powinien posiadać metodę programuj(), która będzie
# wyświetlała napis „programuję...”.
# Księgowy natomiast powinien posiadać umiejętność wyliczenia rocznej
# pensji innego pracownika.
# Stwórz instancję każdej z klas i sprawdź poprawność
# zaimplementowanych metod.



class Pracownik:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        self.workers_list = []

    def add_worker(self, worker):
        self.workers_list.append(worker)

# W klasie Informatyk robię metodę zwracającą "Programuję"
class Informatyk (Pracownik):
    def say(self):
        return 'Programuję!'


class Ksiegowy (Pracownik):

    def count_annual_salary(self):
        cost = 0
        for worker in self.workers_list:
            cost += worker.salary *12
        return cost

johny = Informatyk('Johny', 5000)
print(johny.name)
print(johny.salary)
print(johny.say())
johny.add_worker(johny)
print("\n")

james = Ksiegowy('James', 4000)
print('Imię księgowego: ', james.name)
print('Zarabia: ', james.salary)
# James, który umie obliczać roczną pensję pracowników musi dodać siebie samego do listy pracowników i wtedy
# obliczy swoją roczną pensję
james.add_worker(james)
print('{} obliczył, że {} zarabia rocznie: '.format(james.name, james.name), james.count_annual_salary())
print("\n")

lech = Ksiegowy('Lech', 6000)
print('Imię księgowego: ', lech.name)
print('Zarabia: ', lech.salary)
# Lech, który umie obliczać roczną pensję pracowników musi dodać johnego do listy pracowników i wtedy
# obliczy jego roczną pensję
lech.add_worker(johny)
print('{} obliczył, że {} zarabia rocznie: '.format(lech.name, johny.name), lech.count_annual_salary())
print("\n")
