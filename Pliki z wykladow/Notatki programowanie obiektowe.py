# a = 5
# print(dir(a))

# Tworzenie klasy
# Klasa jest SZABLONEM
class Czlowiek:
    gatunek = "homo sapiens"
    def __init__(self, imie="Adam"):
        print("Metoda inicjalizacyjna działa!")
        print("Tworzę człowieka o imieniu", imie="Adam")
        self.imie = "Adam"
        adam.imie = "Adam"

    #dodajemy metodę, bo funkcja wewnątrz klasy to metoda
    def powiedz_hej(selfself):
        print("No hej!")

# Tworzę OBIEKT
# Instancję klasy Człowiek
adam = Czlowiek("Adam")  # self = adam
ewa = Czlowiek("Ewa")   # self = ewa     ## self odnosi się do konkretnego obiektu

print("Adam ma na imię", adam.imie)


# print(adam.gatunek)
# print((dir(adam)))
#
# print(ewa.gatunek)
# print((dir(ewa)))
#
# adam.powiedz_hej()
# ewa.powiedz_hej()
#
# print(dir(Czlowiek))
# print(dir(adam))
# print(dir(ewa))

