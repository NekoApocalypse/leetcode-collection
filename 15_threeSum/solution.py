class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        ans = []
        for i, n1 in enumerate(nums):
            if n1 > 0:
                break
            if i > 0 and n1 == nums[i - 1]:
                continue
            target = -n1
            ll = i + 1
            rr = len(nums) - 1
            while ll < rr:
                while ll < rr and nums[ll] + nums[rr] > target:
                    rr -= 1
                if ll < rr and nums[ll] + nums[rr] == target:
                    ans.append([n1, nums[ll], nums[rr]])
                cur = nums[ll]
                while ll < rr and nums[ll] == cur:
                    ll += 1
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
    