class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        return str(x) == str(x)[::-1]


def test():
    sol = Solution()


if __name__ == '__main__':
    test()
    
