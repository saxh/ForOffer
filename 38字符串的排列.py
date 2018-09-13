def permutation(index=0, str=[], tmp=[]):
    if index == len(str):
        # if str[1]+str[2]+str[3]
        print(tmp)
    for i in range(index, len(str)):
        tmp.append(str[i])
        print(tmp)
        str[index], str[i] = str[i], str[index]
        permutation(index + 1, str)
        str[index], str[i] = str[i], str[index]
        tmp.pop()


if __name__ == '__main__':
    permutation(str=list("abc"))
