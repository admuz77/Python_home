class KontoBankowe:
    __stan = 0

    @property
    def stan_konta(self):
        return self.__stan

    @stan_konta.getter
    def stan_konta(self):
        return "Stan konta: " + str(self.__stan) + " zł"


# setter odpowiada za to co będzie dodane
    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan += value

konto = KontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)

konto.stan_konta = 100
print(konto.stan_konta)

konto.stan_konta = -150
print(konto.stan_konta)

#
# # Tworzę klasę
# class Pracownik:
#     def __init__(self, imie, nazwisko, pensja):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.pensja = pensja
#
#
# # __repr__ to metoda specjala wbudowana w Py, zwraca reprezentację danego obiektu w postaci łańcucha znaków
#     @property
#     def __repr__(self):
#         return self.imie + ' ' + self.nazwisko + ' zarabia ' + self.pensja
#
#
#
# pracownik_1 = Pracownik('Leopold', 'Wanatowicz', '5000')
#
# print(pracownik_1)