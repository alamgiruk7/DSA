class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    
    def getHash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        
        return h % self.max

    def __setitem__(self, key, value):
        h = self.getHash(key)

        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.findSlot(key, h)
            self.arr[new_h] = (key, value)

    def __getitem__(self, key):
        h = self.getHash(key)
        prob_range = self.getProbRange(h)
        for i in prob_range:
            if self.arr[i] is None or self.arr[i][0] != key:
                continue
            if self.arr[i][0] == key:
                return self.arr[i][1]
        raise Exception("Item not in the list")

    def __delitem__(self, key):
        h = self.getHash(key)
        prob_range = self.getProbRange(h)
        for i in prob_range:
            if self.arr[i] is None or self.arr[i][0] != key:
                continue
            if self.arr[i][0] == key:
                self.arr[i] = None
                return
        raise Exception("Item not in the list")


    def findSlot(self, key, h):
        prob_range = self.getProbRange(h)
        for i in prob_range:
            if self.arr[i] is None:
                return i
            elif self.arr[i][0] == key:
                return i
        raise Exception("List is Full")

    def getProbRange(self, h):
        return [*range(h, len(self.arr))] + [*range(0, h)]

hashobj = Hashtable()

hashobj['march 6'] = 25
hashobj['march 6'] = 21
hashobj['march 17'] = 24
hashobj['march 7'] = 30
# print(hashobj['march 6'])
# print(hashobj['march 17'])
# print(hashobj['march 8'])
print(hashobj.arr)
# del hashobj['march 6']
# print(hashobj.arr)
# del hashobj['march 21']
# print(hashobj.arr)
