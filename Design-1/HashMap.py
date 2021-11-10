# Designing HashMap

class LinkedList:
    def __init__(self):
        self.lis=[]
        
    def put(self,key,val):
        for ind,v in enumerate(self.lis):
            if self.lis[ind][0]==key:
                self.lis[ind]= (key,val)
                return
        self.lis.append((key,val))
        
    def get(self,key):
        for k,v in self.lis:
            if k==key:
                return v
        return -1
    
    def delete(self,key):
        for ind,val in enumerate(self.lis):
            if self.lis[ind][0]==key:
                del self.lis[ind]
                return
        
            
                
        

class MyHashMap:

    def __init__(self):
        self.maxLen = 1000
        self.hashmap=[LinkedList() for i in range(self.maxLen)]
        
    def getHash(self,key):
        return key%self.maxLen
        

    def put(self, key: int, value: int) -> None:
        h = self.getHash(key)
        self.hashmap[h].put(key,value)        
        

    def get(self, key: int) -> int:
        h = self.getHash(key)        
        return self.hashmap[h].get(key)

    def remove(self, key: int) -> None:
        h=self.getHash(key)
        self.hashmap[h].delete(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
