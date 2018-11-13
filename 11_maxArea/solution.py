class Solution:
    def maxArea(self, height):
        v_height = sorted(
            range(len(height)),
            key=lambda k: height[k],
            reverse=True
        )
        left_most = right_most = v_height[0]
        ans = 0
        for id in v_height:
            left_most = min(left_most, id)
            right_most = max(right_most, id)
            ans = max(ans, abs(id - left_most) * height[id])
            ans = max(ans, abs(id - right_most) * height[id])
        return ans


def test():
    # case = [1, 1]
    case = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    print(case)
    print(sol.maxArea(case))


if __name__ == '__main__':
    test()
    
