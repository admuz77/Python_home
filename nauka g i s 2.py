class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

# Służy do podanie wszystkich (uwzględnionych niżej) informacji o danym obiekcie, wywołam to później np poleceniem: print(pracownik_3)

    def __repr__(self):
        return self.imie + ' ' + self.nazwisko + ' ' + str(self.pensja)

        self.wszyscy = ['lalalala']

# dekoratory dla imienia
    @property
    def imie(self):
        return self.__imie

    @imie.getter
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, noweimie):
        self.__imie = noweimie
        self.mamnaimie = 'Mam na imię {}'.format(self.imie)

# dekoratory dla nazwiska
    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.getter
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, nowenazwisko):
        self.__nazwisko = nowenazwisko
        self.mamnanazwisko = 'Mam na nazwisko {}'.format(self.nazwisko)

# dekoratory dla pensji
    @property
    def pensja(self):
        return self.__pensja

    @pensja.getter
    def pensja(self):
        return str(self.__pensja)

    @pensja.setter
    def pensja(self, newvalue):
        self.__pensja = newvalue
        self.zarabiam = 'Nazywam się {} i zarabiam {} zł.'.format(self.imie, self.pensja)



    def dodaj_pracownika(self, pracownik):
        self.wszyscy.append(pracownik)

    def wyswietl_wszystkich_pracownikow(self):
        print(self.wszyscy)

# # lista pracowników
#     @property
#     def lista(self):
#         self.wszyscy = []
#
#     @lista.getter
#     def lista(self):
#         return self.__lista
#
#     @lista.setter
#     def lista(self, nowalista):
#         self.__lista = nowalista
#         self.lista = 'Lista pracownikow {}'.format(self.lista)


pracownik = Pracownik("Leopold", "Wanatowicz", 4000)
# pracownik.pensja = pracownik.pensja + 1
print(pracownik)
print(pracownik.mamnaimie)
print(pracownik.mamnanazwisko)
print(pracownik.zarabiam)

pracownik_2 = Pracownik("Janusz", "Fąferski", 3900)
print(pracownik_2)
print(pracownik_2.mamnaimie)
print(pracownik_2.mamnanazwisko)
print(pracownik_2.zarabiam)

pracownik_3 = Pracownik("Stefan", "Pająk", 3700)
print(pracownik_3)
print(pracownik_3.mamnaimie)
print(pracownik_3.mamnanazwisko)
print(pracownik_3.zarabiam)


print(pracownik_3)

print(Pracownik.wyswietl_wszystkich_pracownikow)