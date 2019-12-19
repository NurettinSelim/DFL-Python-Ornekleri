##
## *
## * *
## * * *
## * *
## *
#Yukarıdaki şekli sayıdan bağımsız bir şekilde oluşturma


def doku(sayi):
    for i in range(0,sayi):
        for k in range(0,i):
            print("*", end=" ")
        print()
    for i in range(sayi,0,-1):
        for k in range(0,i):
            print("*", end=" ")
        print()

doku(5)