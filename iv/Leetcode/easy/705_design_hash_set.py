class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def add(self, key: int) -> None:
        if key in self.set:
            pass
        else:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.set:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))
