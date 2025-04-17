class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        start_ind = 0
        end_ind = len(nums) - 1
        while start_ind < end_ind:
            if nums[start_ind] == val:
                if nums[end_ind] != val:
                    nums[start_ind], nums[end_ind] = nums[end_ind], nums[start_ind]
                    start_ind += 1
                end_ind -= 1
            else:
                start_ind += 1
        if nums[start_ind] == val:
            return start_ind
        return start_ind + 1