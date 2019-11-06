list = [[" ", "|", " ", "|", " "],
        ["-", "|", "-", "|", "-"],
        [" ", "|", " ", "|", " "],
        ["-", "|", "-", "|", "-"],
        [" ", "|", " ", "|", " "]]

for z in list:
    print("".join(z))
print("____________________________________________")


def getFromX():
    while True:
        X = int(input("X: "))
        if 0 < X < 10:
            return X
            break
        else:
            print("Enter number between 1 to 9 DumpAss")


def getFromO():
    print("Enter number between 1 to 9: ")
    while True:
        O = int(input("O: "))
        if 0 < O < 10:
            return O
            break
        else:
            print("Enter number between 1 to 9 DumpAss")


# checks whether the input area contain " " or X,O
def isEmpty(a, b):
    if list[a][b] == " ":
        return True
    else:
        return False


def mappingForX(X):
    if X == 1 and isEmpty(0, 0):
        list[0][0] = "X"
    elif X == 2 and isEmpty(0, 2):
        list[0][2] = "X"
    elif X == 3 and isEmpty(0, 4):
        list[0][4] = "X"
    elif X == 4 and isEmpty(2, 0):
        list[2][0] = "X"
    elif X == 5 and isEmpty(2, 2):
        list[2][2] = "X"
    elif X == 6 and isEmpty(2, 4):
        list[2][4] = "X"
    elif X == 7 and isEmpty(4, 0):
        list[4][0] = "X"
    elif X == 8 and isEmpty(4, 2):
        list[4][2] = "X"
    elif X == 9 and isEmpty(4, 4):
        list[4][4] = "X"


def mappingForO(O):
    if O == 1 and isEmpty(0, 0):
        list[0][0] = "O"
    elif O == 2 and isEmpty(0, 2):
        list[0][2] = "O"
    elif O == 3 and isEmpty(0, 4):
        list[0][4] = "O"
    elif O == 4 and isEmpty(2, 0):
        list[2][0] = "O"
    elif O == 5 and isEmpty(2, 2):
        list[2][2] = "O"
    elif O == 6 and isEmpty(2, 4):
        list[2][4] = "O"
    elif O == 7 and isEmpty(4, 0):
        list[4][0] = "O"
    elif O == 8 and isEmpty(4, 2):
        list[4][2] = "O"
    elif O == 9 and isEmpty(4, 4):
        list[4][4] = "O"

def resultCheckForX():
    if list[0][0] is "X" and list[0][2] is "X" and list[0][4] is "X":
        print("X won the game")
        return True
    if list[2][0] is "X" and list[2][2] is "X" and list[2][4] is "X":
        print("X won the game")
        return True
    if list[4][0] is "X" and list[4][2] is "X" and list[4][4] is "X":
        print("X won the game")
        return True
    if list[0][0] is "X" and list[2][0] is "X" and list[4][0] is "X":
        print("X won the game")
        return True
    if list[0][2] is "X" and list[2][2] is "X" and list[4][2] is "X":
        print("X won the game")
        return True
    if list[0][4] is "X" and list[2][2] is "X" and list[4][2] is "X":
        print("X won the game")
        return True
    if list[0][4] is "X" and list[2][4] is "X" and list[4][4] is "X":
        print("X won the game")
        return True
    if list[0][0] is "X" and list[2][2] is "X" and list[4][4] is "X":
        print("X won the game")
        return True
    if list[0][4] is "X" and list[2][2] is "X" and list[4][0] is "X":
        print("X won the game")
        return True

def resultCheckForO():
    if list[0][0] is "O" and list[0][2] is "O" and list[0][4] is "O":
        print("O won the game")
        return True
    if list[2][0] is "O" and list[2][2] is "O" and list[2][4] is "O":
        print("O won the game")
        return True
    if list[4][0] is "O" and list[4][2] is "O" and list[4][4] is "O":
        print("O won the game")
        return True
    if list[0][0] is "O" and list[2][0] is "O" and list[4][0] is "O":
        print("O won the game")
        return True
    if list[0][2] is "O" and list[2][2] is "O" and list[4][2] is "O":
        print("O won the game")
        return True
    if list[0][4] is "O" and list[2][2] is "O" and list[4][2] is "O":
        print("O won the game")
        return True
    if list[0][4] is "O" and list[2][4] is "O" and list[4][4] is "O":
        print("O won the game")
        return True
    if list[0][0] is "O" and list[2][2] is "O" and list[4][4] is "O":
        print("O won the game")
        return True
    if list[0][4] is "O" and list[2][2] is "O" and list[4][0] is "O":
        print("O won the game")
        return True


# def resultCheckForX():
#     if (((list[0][0] and list[0][2] and list[0][4]) is "X") or
#             ((list[2][0] and list[2][2] and list[2][4]) is "X") or
#             ((list[4][0] and list[4][2] and list[4][4]) is "X") or
#             ((list[0][0] and list[2][0] and list[4][0]) is "X") or
#             ((list[0][2] and list[2][2] and list[4][2]) is "X") or
#             ((list[0][4] and list[2][4] and list[4][4]) is "X") or
#             ((list[0][0] and list[2][2] and list[4][4]) is "X") or
#             ((list[0][4] and list[2][2] and list[4][0]) is "X")):
#         print("X won the game !!!")
#         return True
#
#
# def resultCheckForO():
#     if ((list[0][0] and list[0][2] and list[0][4]) or
#             (list[2][0] and list[2][2] and list[2][4]) or
#             (list[4][0] and list[4][2] and list[4][4]) or
#             (list[0][0] and list[2][0] and list[4][0]) or
#             (list[0][2] and list[2][2] and list[4][2]) or
#             (list[0][4] and list[2][4] and list[4][4]) or
#             (list[0][0] and list[2][2] and list[4][4]) or
#             (list[0][4] and list[2][2] and list[4][0])) is "O":
#         print("O won the game !!!")
#         return True


count = 0
print("Enter number between 1 to 9: ")
while count <= 4:
    intX = getFromX()
    mappingForX(intX)
    for z in list:
        print("".join(z))
    print("____________________________________________")
    if resultCheckForX():
        break
    intO = getFromO()
    mappingForO(intO)
    for z in list:
        print("".join(z))
    print("____________________________________________")
    if resultCheckForO():
        break
    count += 1
