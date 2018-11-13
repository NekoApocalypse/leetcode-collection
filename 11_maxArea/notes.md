# Solution Notes:

## 解法：

1. O(N) 扫描算法

从数组的两端开始扫描，并维护条件：

	L += 1 if and only if: num[L]<=num[R]

	R -= 1 if and only if: num[R]<num[L]

按照该条件进行扫描即可保证 (L, R) 区间缩小的情况下 min(num[L], num[R]) 保持递增。
