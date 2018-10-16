
def coin(n):
    num_list = [0, 0, 0, 0]
    while n > 0:
        if n // 25 > 0:
            num_list[0] += n // 25
            n = n % 25
        elif n // 10 > 0:
            num_list[1] += n // 10
            n = n % 10
        elif n // 5 > 0:
            num_list[2] += n // 5
            n = n % 5
        else:
            num_list[3] += n
            n = n % 1
    return num_list


if __name__ == '__main__':
    print(coin(58))