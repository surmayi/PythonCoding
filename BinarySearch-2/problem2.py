class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high =0 ,len(nums)-1
        if nums[low]<=nums[high]:
            return nums[low]
        while low<high:
            mid = low +(high-low)//2
            if mid<high and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if mid>low and nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[low]<nums[mid]:
                low=mid+1
            else:
                high=mid-1
