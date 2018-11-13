class Solution:
    def intToRoman(self, num):
        symbols_list = [
            ["M", "M", "M"],
            ["C", "D", "M"],
            ["X", "L", "C"],
            ["I", "V", "X"]
        ]
        pown_list = [1000, 100, 10, 1]
        def digitToRoman(digit, symbols):
            if digit < 4:
                return symbols[0] * digit
            elif digit == 4:
                return symbols[0] + symbols[1]
            elif digit < 9:
                return symbols[1] + (symbols[0] * (digit - 5))
            else:
                return symbols[0] + symbols[2]

        buffer = ""
        for pown, symbols in zip(pown_list, symbols_list):
            buffer += digitToRoman(num // pown, symbols)
            num %= pown
        return buffer


def test():
    sol = Solution()
    cases = [3, 4, 5, 9, 58, 1994]
    for case in cases:
        print(case)
        print(sol.intToRoman(case))


if __name__ == '__main__':
    test()
    
