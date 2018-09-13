def PrintToMaxOfDigits(n):
    for i in range(1, 10 ** n):
        print(i, end=",")
if __name__ == '__main__':
    PrintToMaxOfDigits(3)