# Given n unique integers, number k (1<=k<=n) and target.
#
# Find all possible k integers where their sum is target.

# 样例
# 给出[1,2,3,4]，k=2， target=5，返回 [[1,4],[2,3]]

"""
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

def test(A, k, targer,tmp):
    # write your code here
    for x in range(len(A)):
        test()

def kSumII(A, k, targer):
    # write your code here
    for x in range(len(A)):
        if k == 1 and A[x] == targer:
            return targer
        else:
            print(kSumII(A[x+1:],k-1,targer - A[x]))

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7]
    k = 3
    targer = 7
    print(kSumII(A, k, targer))