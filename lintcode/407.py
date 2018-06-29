class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # # write your code here
        # tmp = 0
        # for i in digits:
        #     print(i)
        #     tmp = tmp * 10 + i
        # tmp += 1
        # print(tmp)
        # res = []
        # while tmp >= 10:
        #     res.insert(0,tmp%10)
        #     tmp = int((tmp - tmp%10)/10)
        #
        # res.insert(0,tmp)
        #
        # return res
        for i in range(len(digits))[::-1]:
            print(i)
            if digits[i] == 9:
                digits[i] = 0
                continue
            else:
                digits[i] += 1
                break
        print(digits)
        if digits[0] == 0:
            # digits[0] = 0
            digits.insert(0,1)
        return digits

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,0,0,0,0]))