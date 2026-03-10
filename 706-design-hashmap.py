class MyHashMap:

    def __init__(self):
        self.size= 1000
        self.table=[[] for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index= key% self.size
        for i, values in enumerate(self.table[index]):
            if values[0]==key:
                self.table[index][i][1]=value
                return
        self.table[index].append([key, value])
    def get(self, key: int) -> int:
        index = key% self.size
        for values in self.table[index]:
            if values[0]==key:
                return values[1]
        return -1

    def remove(self, key: int) -> None:
        index = key%self.size
        for i, values in enumerate(self.table[index]):
            if values[0]==key:
                self.table[index].pop(i)
                return