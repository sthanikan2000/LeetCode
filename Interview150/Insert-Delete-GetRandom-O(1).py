import random
class RandomizedSet:

    def __init__(self):
        self.val_to_ind = {}
        self.ind_to_val = {}
        self.available=[]
        
    def insert(self, val: int) -> bool:
        # print(self.val_to_ind)
        if self.val_to_ind.get(val) != None:
            return False
        if self.available:
            self.val_to_ind[val] = self.available.pop()
        else:
            self.val_to_ind[val] = len(self.val_to_ind)
        self.ind_to_val[self.val_to_ind[val]] = val
        return True

    def remove(self, val: int) -> bool:
        if self.val_to_ind.get(val) == None:
            return False
        x  = self.val_to_ind.get(val)
        self.ind_to_val[x] = None
        self.available.append(x)
        self.val_to_ind.pop(val)
        return True

    def getRandom(self) -> int:
        x = random.randint(0, len(self.val_to_ind)-1)
        return list(self.val_to_ind.keys())[x]
        # print(self.ind_to_val, self.val_to_ind)
        # x = self.ind_to_val[random.randint(0, len(self.ind_to_val)-1)]
        # while x == None:
        #     x = self.ind_to_val[random.randint(0, len(self.val_to_ind)-1)]
        # return x
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()