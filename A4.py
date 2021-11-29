h = int(input('Podaj wysokość choinki: '))
for height in range(0,h+1):
    print (" "*(h-height)+"*"*(height*2-1))
