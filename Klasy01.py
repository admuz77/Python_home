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


class Zatrudnieni:
    def __init__(self):
        self.leopold_wanatowicz = Pracownik("Leopold", "Wanatowicz", 5000)
        self.janusz_faferski = Pracownik("Janusz", "Fąferski", 4500)
        self.jacek_pirog = Pracownik("Jacek", "Piróg", 4700)

        self.wszyscy = [self.leopold_wanatowicz, self.janusz_faferski, self.jacek_pirog]


    @property
    def dodaj_pracownika(self, pracownik):
        self.wszyscy.append(pracownik)

    @property
    def wyswietl_wszystkich_pracownikow(self):
        print(self.wszyscy)

modul_zatrudnieni = Zatrudnieni ()
nowy_pracownik = Pracownik("Stefan", "Pająk", 4500)
print(nowy_pracownik)
# Wyświetli pierwotną listę pracowników ponieważ nie jest jeszcze Stefan uwzględniony, trzeba użyć dodaj_pracownika
modul_zatrudnieni.wyswietl_wszystkich_pracownikow

# I tu wywala mi błąd, nie wiem dlaczego... nowy_pracownik w nawiasach też odpada
modul_zatrudnieni.dodaj_pracownika.nowy_pracownik

modul_zatrudnieni.wyswietl_wszystkich_pracownikow
