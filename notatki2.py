import matplotlib.pyplot as plt
import numpy as np

x = input("Wpisz dane dla osi x oddzielając je przecinkami: ")
# sprawdzam typx
print(type(x))
# zmiana na listęX
x_list = x.split(',')
# sprawdzam typ, czy str zmienił sie na listę
print(type(x_list))

# w np.array podaje się wartości, ja przyjmuję je z listy
xpoints = np.array(x_list)

plt.plot(xpoints)
plt.show()