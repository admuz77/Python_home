# pobranie funkcji do tworzenia wykresów
import matplotlib.pyplot as plt
import numpy as np

x = input("Wpisz dane dla osi x oddzielając je przecinkami: ")
# sprawdzam typx
print(type(x))
# zmiana na listęx
x_list = x.split(',')
# sprawdzam typ, czy str zmienił sie na listę
print(type(x_list))

# w np.array podaje się wartości, ja przyjmuję je z listy, uwaga "np." to nie "na przykład" :)
xpoints = np.array(x_list)

plt.plot(xpoints)
plt.show()









# # moje pierwsze podejście
# # pobranie funkcji
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = input("Wpisz dane dla osi x oddzielając je przecinkami: ")
# # sprawdzam typx
# print(type(x))
# # zmiana na listęX
# x_list = x.split(',')
#
# print(x_list)
#
# y = input("Wpisz dane dla osi y oddzielając je przecinkami: ")
# # sprawdzam typy
# print(type(y))
# # zmiana na listęX
# y_list = y.split(',')
#
# print(y_list)
#
# plt.plot(x_list, y_list)
# plt.show()
#
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()