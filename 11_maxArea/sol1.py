class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        ans = 0
        min_height = 0
        while l < r:
            min_height = min(height[l], height[r])
            ans = max(
                ans,
                min_height * (r-l)
            )
            while(height[l] <= min_height and l < r):
                l += 1
            while(height[r] <= min_height and l < r):
                r -= 1
        return ans


def test():
    # case = [1, 1]
    case = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    print(case)
    print(sol.maxArea(case))


if __name__ == '__main__':
    test()
    
