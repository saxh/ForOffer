def fun(k, A=[]):
    tmp = [999999] * (k + 1)
    for i in range(len(A)):
        if tmp[1] > A[i]:
            tmp[1] = A[i]
            adjust(tmp, k)
    return sorted(tmp)[0:k]


def adjust(tmp, k):
    index = 1
    # big_index = 0
    while index * 2 <= k:
        if index * 2 + 1 <= k:
            if tmp[index * 2] > tmp[index * 2 + 1]:
                big_index = index * 2
            else:
                big_index = index * 2 + 1
            if tmp[big_index] > tmp[index]:
                tmp[index], tmp[big_index] = tmp[big_index], tmp[index]
                index = big_index
            else:
                break

        else:
            if tmp[index * 2] > tmp[index]:
                tmp[index], tmp[index * 2] = tmp[index * 2], tmp[index]
                index = index * 2
            else:
                break


if __name__ == '__main__':
    print(fun(5, [4, 5, 1, 6, 2, 7, 3, 8]))
