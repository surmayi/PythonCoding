class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result =[-1,-1]
        result[0] = self.search_helper(nums,target,True)
        if result[0]!=-1:
            result[1] = self.search_helper(nums,target,False)
        return result
    
    def search_helper(self,arr,target,isMin):
        low, high = 0, len(arr)-1
        foundAt=-1
        while low<=high:
            mid = low + (high-low)//2
            if arr[mid]<target:
                low=mid+1
            elif arr[mid]>target:
                high=mid-1
            else:
                foundAt=mid
                if isMin:
                    high=mid-1
                else:
                    low=mid+1
        return foundAt
