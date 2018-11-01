class Solution:
    def reverse(self, x):
        if x < 0:
            x = -x
            neg = True
        else:
            neg = False
        ans = int(str(x)[::-1])
        if neg:
            ans = -ans
        return 0 if ans > 2 ** 31 - 1 or ans < -2 ** 31 else ans

def test():
    sol = Solution()
    case = -123456
    print(case)
    print(sol.reverse(case))


if __name__ == "__main__":
    test()
