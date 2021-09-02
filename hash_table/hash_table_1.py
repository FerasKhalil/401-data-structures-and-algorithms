class HashTable :
    def __init__(self, size = 750):
        self.size = size
        self._buckets = [None] * self.size

    def hash(self,key:str)->int:
        value=0
        for x in key:
            value += ord(x) # ord () function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.
            print(ord(x))
        index = (value * 7) % self.size   
        # print(index)

if __name__ == "__main__":
    x=HashTable(34)
    x.hash("2222222222")

