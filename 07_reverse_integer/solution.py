import math

class Solution:
    def reverse(self, x):
        if x == 0:
            return 0
        neg = False
        if x < 0:
            x = -x
            neg = True
        np = 10 ** (math.floor(math.log(x, 10)))
        ans = 0
        cur  = 1
        while np:
            ans += cur * (x // np)
           x = x % np
            np = np // 10
            cur *= 10
        if neg:
            ans = -ans
        return 0 if ans > 2**31-1 or ans < -2**31 else ans


def test():
    sol = Solution()
    case = -2146473548
    print(case)
    print(sol.reverse(case))
    case = 0
    print(case)
    print(sol.reverse(case))


if __name__ == '__main__':
    test()
    
