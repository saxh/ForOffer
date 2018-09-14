from functools import cmp_to_key


def fun(A=[]):
    A.sort(key=cmp_to_key(mycmp))
    print("".join(A))


def mycmp(x, y):
    if x + y > y + x:
        return 1
    elif x == y:
        return 0
    else:
        return -1


if __name__ == '__main__':
    fun(["3", "32", "321"])
    # print("311" > "32")
