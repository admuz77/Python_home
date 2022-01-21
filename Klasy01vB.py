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

# __repr__ to metoda specjala wbudowana w Py, zwraca reprezentację danego obiektu w postaci łańcucha znaków
    def __repr__(self):
        return self.imie + ' ' + self.nazwisko

# Tworzę klasę Zatrudnieni z konkretnymi obiektami(?) z "Podróży za jeden uśmiech" :)
class Zatrudnieni:
    def __init__(self):
        self.leopold_wanatowicz = Pracownik("Leopold", "Wanatowicz", 5000)
        self.janusz_faferski = Pracownik("Janusz", "Fąferski", 4500)
        self.jacek_pirog = Pracownik("Jacek", "Piróg", 4700)

        self.wszyscy = [self.leopold_wanatowicz, self.janusz_faferski, self.jacek_pirog]

    def wylicz_miesieczne_wydatki(self):
        wydatki = 0
        for pracownik in self.wszyscy:
            wydatki += pracownik.pensja
        return wydatki

    def dodaj_pracownika(self, pracownik):
        self.wszyscy.append(pracownik)

    def wyswietl_wszystkich_pracownikow(self):
        print(self.wszyscy)

modul_zatrudnieni = Zatrudnieni ()
nowy_pracownik = Pracownik("Stefan", "Pająk", 3000)
modul_zatrudnieni.wyswietl_wszystkich_pracownikow()
modul_zatrudnieni.dodaj_pracownika(nowy_pracownik)
modul_zatrudnieni.wyswietl_wszystkich_pracownikow()
