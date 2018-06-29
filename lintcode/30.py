# 描述
# Given a non-overlapping interval list which is sorted by start point.
#
# Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].
#
# Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].

def insert(intervals, newInterval):
    # write your code here
    if newInterval == []:
        return intervals
    tmp = []
    left = newInterval[0]
    right = newInterval[1]
    for i in intervals:
        if i[1] >= left >= i[0]:
            left = i[0]
        if i[1] >= right >= i[0]:
            right = i[1]
        for j in i:
            tmp.append(j)
    condition = lambda t: not (left <= t <= right)
    tmp = list(filter(condition, tmp))
    tmp.append(left)
    tmp.append(right)
    tmp.sort()
    res = []
    ind = 0
    while True:
        tl = tmp[ind]
        res.append((tmp[ind], tmp[ind + 1]))
        ind += 2
        if ind >= len(tmp) - 1:
            break
    return res


if __name__ == '__main__':
    a = [(1,3),(4,5),(7,9)]
    b = []
    print(insert(a,b))
