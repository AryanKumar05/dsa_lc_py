class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_linear(nums, 0, n - 2), self.rob_linear(nums, 1, n - 1))

    def rob_linear(self, nums: list[int], start: int, end: int) -> int:
        if start == end:
            return nums[start]
        length = end - start + 1
        dp = [0] * length
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start + 1])
        for i in range(2, length):
            # Either skip this house or rob it and add best from two back
            dp[i] = max(dp[i - 1], nums[start + i] + dp[i - 2])
        return dp[length - 1]