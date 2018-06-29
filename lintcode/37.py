
def reverseInteger( number):
    res = 0
    while number:
        res = res * 10+(number%10)
        number=int(number/10)
    return res


if __name__ == '__main__':
    print(reverseInteger(100001))
