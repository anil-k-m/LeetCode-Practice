class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        # Iterate through list usinng index and increment index when a element is removed
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)