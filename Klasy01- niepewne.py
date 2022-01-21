# Zadanie 1
# Napisz klasę Pracownik posiadającą następujące atrybuty:
# - imię
# - nazwisko
# - pensja
# Stwórz gettery oraz settery do każdego z atrybutów.
# Stwórz 3 instancje tej klasy oraz sprawdź poprawność
# zaimplementowanych metod.


# Tworzę klasę
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

        self.wszyscy = []

# Metoda specjalna reprezentation. Służy do podanie wszystkich (uwzględnionych niżej) informacji o danym obiekcie,
# wywołam to później np poleceniem: print(pracownik)

    def __repr__(self):
        return self.imie + ' ' + self.nazwisko + ' ' + str(self.pensja)

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
    def pensja(self, nowapensja):
        self.__pensja = nowapensja
        self.zarabiam = 'Nazywam się {} i zarabiam {} zł.'.format(self.imie, self.pensja)

    @property
    def dodaj_pracownika(self, pracownik):
        self.wszyscy.append(pracownik)

    @property
    def wyswietl_wszystkich_pracownikow(self):
        print(self.wszyscy)


leopold_wanatowicz = Pracownik("Leopold", "Wanatowicz", 5000)
janusz_faferski = Pracownik("Janusz", "Fąferski", 4500)
jacek_pirog = Pracownik("Jacek", "Piróg", 4700)

print(leopold_wanatowicz)
print(leopold_wanatowicz.mamnaimie)
print(leopold_wanatowicz.mamnanazwisko)
print(leopold_wanatowicz.zarabiam)
print("\n")

# # Tu mi się krzaczy
# leopold_wanatowicz.dodaj_pracownika

print(janusz_faferski)
print(janusz_faferski.mamnaimie)
print(janusz_faferski.mamnanazwisko)
print(janusz_faferski.zarabiam)
print("\n")

print(jacek_pirog)
print(jacek_pirog.mamnaimie)
print(jacek_pirog.mamnanazwisko)
print(jacek_pirog.zarabiam)

