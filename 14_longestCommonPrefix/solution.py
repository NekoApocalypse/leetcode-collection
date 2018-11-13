class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        ans = 0
        flag = True
        while flag:
            if ans < len(strs[0]):
                target = strs[0][ans]
            else:
                break
            for str in strs:
                if ans >= len(str) or str[ans] != target:
                    flag = False
                    break
            if flag:
                ans += 1
        return strs[0][:ans]


def test():
    sol = Solution()
    cases = [
        ["flower", "flow", "flight"],
        ["dog", "racer", "car"],
        ["di", "did", "didid"],
        []
    ]
    for case in cases:
        print(case)
        print(sol.longestCommonPrefix(case))


if __name__ == '__main__':
    test()
    
