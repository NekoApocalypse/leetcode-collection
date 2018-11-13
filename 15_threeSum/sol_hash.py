from collections import Counter

class Solution:
    def threeSum(self, nums):
        cnt = Counter(nums)
        pos = []
        neg = []
        for nu in cnt.keys():
            if nu > 0:
                pos.append(nu)
            elif nu < 0:
                neg.append(nu)
        ans = []
        if cnt[0] > 2:
            ans.append([0, 0, 0])
        for n1 in neg:
            for n2 in pos:
                target = -(n1 + n2)
                if n1 <= target and target <= n2:
                    if target == n1 or target == n2:
                        if cnt[target] > 1:
                            ans.append([n1, n2, target])
                    elif cnt[target] > 0:
                        ans.append([n1, n2, target])
        return ans


def test():
    sol = Solution()
    cases = [
        [-1, 0, 1, 2, -1, -4],
        [],
        [-1, 0, 0, 1, 1, 2, -1, -2, -4],
        [-1, 0, 0, 0, 1, 1, 2, -1, -2, -4]
    ]
    for case in cases:
        print(case)
        print(sol.threeSum(case))
        print('------------------')


if __name__ == '__main__':
    test()
    