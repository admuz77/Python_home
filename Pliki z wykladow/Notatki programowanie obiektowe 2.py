
# Tworzenie klasy
# Klasa jest SZABLONEM
class Czlowiek:
    gatunek = "homo sapiens"
    def __init__(self, imie, nazwisko):
        print("Jestem gatunku", self.gatunek)
        print("Tworzę człowieka o imieniu", imie)
        self.imie = imie
        self.nazwisko = nazwisko
        # adam.imie = "Adam"
        # ewa.imie = "Ewa

    def powiedz_hej(self):
        print("No hej. Jestem", self.imie)


# Tworzę OBIEKT
# INSTANCJĘ klasy Człowiek
adam = Czlowiek("Adam", "Pierwszy") # self = adam
ewa = Czlowiek("Ewa", "Pierwsza") # self = ewa

print("Adam ma na imię", adam.imie)
print("Ewa ma na imię", ewa.imie)

# print(adam.gatunek)
# print(ewa.gatunek)
#
# adam.powiedz_hej()
# ewa.powiedz_hej()
#
# print(dir(Czlowiek))
# print(dir(adam))
# print(dir(ewa))

adam.powiedz_hej()
ewa.powiedz_hej()