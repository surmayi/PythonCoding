# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        start,end = 0,1
        while reader.get(end)<target:
            start,end = end+1, end + (end-start+1)*2
        return self.search_helper(reader,target,start,end)
        
    def search_helper(self,reader,target,low,high):
        while low<=high:
            mid = low + (high-low)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)<target:
                low=mid+1
            else:
                high=mid-1
        return -1
