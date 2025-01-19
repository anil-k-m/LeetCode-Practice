class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        # Iterate through the array
        for i, num in enumerate(nums):
            remain = target - num
            # Check if the remain exists
            if remain in nums_hash:
                return [nums_hash[remain], i]
            # Store the number and its index
            nums_hash[num] = i
        # Return an empty list if no solution
        return []