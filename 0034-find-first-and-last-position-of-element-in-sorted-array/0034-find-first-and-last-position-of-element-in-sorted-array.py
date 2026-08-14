class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        # --- First Binary Search: Find Leftmost Index ---
        low1, high1 = 0, len(nums)
        while low1 < high1:
            mid = low1 + (high1 - low1) // 2  
            if nums[mid] < target:
                low1 = mid + 1
            else:
                high1 = mid

        # Check if target was even found + out of bound check
        if low1 >= len(nums) or nums[low1] != target:
            return [-1, -1]

        # --- Second Binary Search: Find Rightmost Index ---
        low2, high2 = 0, len(nums)
        while low2 < high2:
            mid = low2 + (high2 - low2) // 2  
            if nums[mid] <= target:
                low2 = mid + 1
            else:
                high2 = mid

        low2 = low2 - 1

        # Safely verify right bound
        if low2 < 0 or nums[low2] != target:
            low2 = -1

        return [low1, low2]