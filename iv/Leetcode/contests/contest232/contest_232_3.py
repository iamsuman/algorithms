import heapq
from heapq import heapify


class Solution:
    def maxAverageRatio(self, classes: list, extraStudents: int) -> float:
        h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
        heapify(h)
        while extraStudents:
            v, a, b = heapq.heappop(h)
            a, b = a + 1, b + 1
            heapq.heappush(h, (-(a + 1) / (b + 1) + a / b, a, b))
            extraStudents -= 1
        return sum(a / b for v, a, b in h) / len(h)

    def maxAverageRatio2(self, classes: list, extraStudents: int) -> float:

        while extraStudents > 0:
            extraStudents -= 1
            res = []
            for i in range(len(classes)):
                x = classes[i][0] + 1
                y = classes[i][1] + 1
                # print(x,y)
                classes[i] = [x,y]
                # print(classes)
                res.append([self.avgratio(classes), classes[:]])
                classes[i] = [x - 1, y - 1]

            res.sort(reverse=True)
            classes = res[0][1]
            # print(res)
        return self.avgratio(classes)

    def avgratio(self, classes):
        per = 0
        for i, j in classes:
            per += float(i) / float(j)
        return per/len(classes)


classes = [[1,2],[3,5],[2,2]]; extraStudents = 2
classes = [[2,4],[3,9],[4,5],[2,10]]; extraStudents = 4
classes = [[547,616],[419,932],[121,677],[285,303],[255,388],[573,768],[5,983],[195,542],[450,593],[22,32],[643,997],[249,621],[267,856],[178,212],[152,292],[206,556],[280,319],[600,776],[257,853],[458,700],[811,882],[829,876],[173,997],[366,559],[431,503],[125,877],[214,788],[585,901],[210,393],[291,831],[111,926],[25,827],[121,583],[14,766],[304,559],[691,989],[742,780],[665,997],[77,140],[383,513],[587,825],[319,448],[516,694],[366,777],[332,542],[1,127],[453,736],[359,461],[313,553],[348,409],[749,802],[586,700],[116,505],[664,940],[387,392],[209,571],[4,285],[613,651],[740,903],[757,850],[524,746],[204,946],[473,616],[530,855],[419,960],[730,763],[313,720],[175,461],[635,685],[203,544],[369,539],[4,695],[399,594],[437,994],[345,415],[637,882],[599,998]]
extraStudents = 5554
# .5, .33..8, .2
c = [[3,5],[4,10],[4,5],[3,11]]
s = Solution()
print(s.maxAverageRatio(classes, extraStudents))
print(s.maxAverageRatio2(classes, extraStudents))
# print(s.avgratio(c))

