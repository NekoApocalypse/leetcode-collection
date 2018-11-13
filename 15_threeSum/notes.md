# Solution Notes:

## 解法：

1. 枚举 + Hash `O(N^2)`：

	任意枚举两个数 a，b，当 a <= -(a+b) <= b && a<b 时在 Hash 表中查找 -(a+b)。

注意： 完全枚举 a 和 b 会超时，优化方法是只在负数中枚举 a，只在正数中枚举 b。


2. 枚举 + 两端扫描`O(N^2)`：

对数组排序后从小到大枚举 a，然后在剩余部分两段扫描寻找 b+c = -a。

注意避免重复的情况。
