class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        total_len = nums1_len + nums2_len
        i,j=0,0
        while i<nums1_len and j<nums2_len:
            if nums1[i]<nums2[j]:
                merged_nums.append(nums1[i])
                i+=1
            else:
                merged_nums.append(nums2[j])
                j+=1
        if i<nums1_len:
            merged_nums.extend(nums1[i:])
        if j<nums2_len:
            merged_nums.extend(nums2[j:])
        if total_len%2==0:
            return (merged_nums[total_len//2 - 1] + merged_nums[total_len//2])/2
        else:
            return merged_nums[total_len//2]
            
        