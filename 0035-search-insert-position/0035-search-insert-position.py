class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1
        while start_index <= end_index:
            if nums[start_index] == target or nums[start_index] > target:
                return start_index
            elif nums[end_index] == target:
                return end_index
            elif nums[end_index] < target:
                return end_index + 1
            start_index += 1
            if start_index < end_index:
                end_index -= 1