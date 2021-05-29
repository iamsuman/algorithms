class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        # TODO: review dequeue()
        self.requests.append(t)
        # print(self.requests)
        index = -1
        for i in range(len(self.requests)):
            if t - self.requests[i] > 3000:
                self.requests[i] = -1
                index = i
        # print(self.requests)
        # print(index)
        if index != -1:
            self.requests = self.requests[index+1:]
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))

