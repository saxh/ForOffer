def Power(a, exp):
    if a == 0 and exp <= 0:
        return 0
    res = 1
    for i in range(abs(exp)):
        res *= a

    if exp < 0:
        return 1 / res
    else:
        return res


if __name__ == '__main__':
    print(Power(2, -3))
