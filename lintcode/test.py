def toHex(num):
    # Write your code here
    global flag
    res = []
    int2char = {0: '0',
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                10: 'a',
                11: 'b',
                12: 'c',
                13: 'd',
                14: 'e',
                15: 'f',
                }
    if num < 0:
        flag = False
        a = -num
    else:
        flag = True
        a = num
    while True:
        res.insert(0, a % 2)
        a = a // 2
        if not a:
            break
    if not flag:
        lens = len(res)
        for x in range(32 - lens):
            res.insert(0, 0)
        res = list(map(lambda x: 1 if x == 0 else 0, res))
        lens = len(res) - 1
        while lens >= 0:
            res[lens] += 1
            if res[lens] == 1 or lens == 0:
                break
            res[lens] = 0
            lens -= 1
        if res[0] == 2:
            res.insert(0, 1)

    for x in range(0 if len(res) % 4 == 0 else 4 - len(res) % 4):
        res.insert(0, 0)
    print(res)
    lenth = len(res)
    rtu = []
    while lenth > 0:
        temp = res[lenth - 4 if lenth >= 4 else 0:lenth]
        print(temp)
        tem = 0
        for x in range(len(temp))[::-1]:
            tem += pow(2, 3 - x) * temp[x]
            # print(x)
        # print(tem)
        rtu.insert(0, tem)
        lenth -= 4
    # print(rtu)
    return ''.join(list(map(lambda x: int2char[x], rtu)))


if __name__ == '__main__':
    print(toHex(-1))
    # print(16/5)
    # print([1,2,3,4][:3:1])
