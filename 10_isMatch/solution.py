class Solution:
    def isMatch(self, s, p):
        def compare(a, b):
            return a == '.' or a == b
        s = '=' + s + '='
        p = '=' + p + '='
        n = len(s)
        m = len(p)
        flag = [0] * n
        flag[0] = 1
        cur = 1
        while cur < m:
            target = p[cur]
            if cur + 1 < m and p[cur + 1] == '*':
                cur += 1 
                new_flag = flag.copy()
                for id in range(1, n):
                    if new_flag[id-1] and compare(target, s[id]):
                        new_flag[id] = 1
            else:
                new_flag = [0] * n
                cnt = 0
                for id in range(1, n):
                    if flag[id-1] and compare(target, s[id]):
                        new_flag[id] = 1
                        cnt += 1
                if not cnt:
                    return False
            cur += 1
            flag = new_flag

        return True if flag[-1] else False


def test():
    cases = [
        ('aa', 'a*'),
        ('ab', '.*'),
        ('aab', 'c*a*b'),
        ('mississippi', 'mis*is*p*.')
    ]
    sol = Solution()
    for case in cases:
        print(*case)
        print(sol.isMatch(*case))


if __name__ == '__main__':
    test()
    
