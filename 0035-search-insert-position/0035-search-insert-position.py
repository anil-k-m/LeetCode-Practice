class Solution:

    def divideAndSearch(self, lb: int, ub: int, nums: List[int], target: int) -> int:
        if lb == ub or lb + 1 == ub:
            if nums[lb] == target or nums[lb] > target:
                return lb
            elif nums[ub] == target:
                return ub
            elif nums[ub] < target:
                return ub + 1
        mid = (lb + ub)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.divideAndSearch(lb, mid-1, nums, target)
        else:
            return self.divideAndSearch(mid + 1, ub, nums, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        return self.divideAndSearch(lb, ub, nums, target)
    