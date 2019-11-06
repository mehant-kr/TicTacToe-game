
def getfromx():
    print("Enter number beteen 1 to 9: ")
    while (True):
        X = int(input("X: "))
        if (X > 0 and X < 10):
            return X
            break
        else:
            print("Enter number between 1 to 9 DumpAss")


intX = getfromx()
print(intX)
