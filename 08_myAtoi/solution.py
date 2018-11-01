INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1

class Solution:
    def myAtoi(self, str):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        neg = False
        in_num = False
        limit = INT_MAX
        buf = 0
        str += '\n'
        for char in str:
            if not in_num:
                if char == ' ':
                    continue
                elif char == '-':
                    neg = True
                    limit += 1
                    in_num = True
                elif char == '+':
                    in_num = True
                elif char in numbers:
                    buf = int(char)
                    in_num = True
                else:
                    return 0
            else:
                if char in numbers:
                    buf = buf * 10 + int(char)
                    if buf >= limit:
                        return limit if not neg else -limit
                else:
                    return buf if not neg else -buf


def test():
    case_list = [
        '42',
        '           -42',
        '4444 munch munch',
        'words 112',
        '----32',
        '-99999999999999999999',
        '999999999999999999',
        ''
    ]
    sol = Solution()
    for case in case_list:
        print(case)
        print(sol.myAtoi(case))


if __name__ == '__main__':
    test()
    
