# Napisz program fitness obliczający BMI. Robiliśmy na zajęciach, ale robię po swojemu
# BMI to masa [kg] dzielona przez kwadrat wzrostu [m]

h = float(input('Podaj swój wzrost (w metrach): '))
w = float(input('Ile ważysz (w kilogramach): '))

bmi  = w / (h**2)
print(f'Twoje BMI wynosi {bmi}.')