numbers = tuple(range(2000,3001))
#tworzę tuplę liczb podzielnych przez 7 z podanego zbioru
split7 = []
for i in numbers:
     if i % 7 ==0:
        split7.append(i)
#tworzę tuplę liczb niepodzielnych przez 5 ze zbioru tych podzielnych przez 7
split5 = []
for x in split7:
    if x % 5 > 0:
        split5.append(x)

print(split5)
# result = []
# for a in split7:
#     if a in split5:
#         result.append(a)
# print(result)
