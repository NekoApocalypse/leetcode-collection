class Solution:
    def romanToInt(self, s):
        def symbol_to_int(c):
            if c == "I":
                return 1
            elif c == "V":
                return 5
            elif c == "X":
                return 10
            elif c == "L":
                return 50
            elif c == "C":
                return 100
            elif c == "D":
                return 500
            elif c == "M":
                return 1000
        cur = 1
        ans = 0
        for c in reversed(s):
            digit = symbol_to_int(c)
            if digit >= cur:
                cur = digit
                ans += digit
            else:
                ans -= digit
        return ans


def test():
    sol = Solution()
    cases = [
        "III",
        "IV",
        "IX",
        "LVIII",
        "MCMXCIV"
    ]
    for case in cases:
        print(case)
        print(sol.romanToInt(case))


if __name__ == '__main__':
    test()
    
