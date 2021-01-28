class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        # Time Complexity: l1 * l2 * x where x is avg string length
        res = {}
        summ = len(list1) + len(list2)
        dlist1 = {}
        for i in range(len(list1)):
            dlist1[list1[i]] = i

        for j in range(len(list2)):
            if dlist1.get(list2[j]) is not None:
                id1 = dlist1[list2[j]]
                if id1 + j == summ:
                    res[id1 + j].append(list2[j])
                elif id1 + j < summ:
                    summ = id1 + j
                    res[id1 + j] = [list2[j]]
        # print(res)
        return res[summ]

    def findRestaurant2(self, list1: list, list2: list) -> list:
        # Time Complexity: l1 * l2 * x where x is avg string length
        res = {}
        summ = len(list1) + len(list2)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j == summ:
                        res[i+j].append(list1[i])
                    elif i + j < summ:
                        summ = i + j
                        res[i + j] = [list1[i]]
                    break
        # print(res)
        return res[summ]


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]; list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]; list2 = ["KFC","Shogun","Burger King"]
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]; list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]; list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# list1 = ["KFC"]; list2 = ["KFC"]
s = Solution()
print(s.findRestaurant(list1, list2))



