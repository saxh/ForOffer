def fun1(A):
    tmp = A[0]
    count = 1

    for i in range(1, len(A)):
        if A[i] != tmp:
            if count == 1:
                tmp = A[i]
            else:
                count -= 1
        else:
            count += 1
    return tmp


def fun2(A):
    mid = len(A) // 2
    start = 0
    end = len(A) - 1
    index = partition(A, start, end)
    while index != mid:
        if index > mid:
            end = index - 1
            index = partition(A, start, end)
        else:
            start = index + 1
            index = partition(A, start, end)
    return A[mid]


def partition(A, start, end):
    x = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1


if __name__ == '__main__':
    print(fun2([1, 4, 3, 1, 1, 4, 1, 4, 4, 4, 4]))
