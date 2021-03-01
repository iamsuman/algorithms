
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list, id: int) -> int:
        emap = {e.id: e for e in employees}
        # print(emap)
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(sid) for sid in employee.subordinates))
        return dfs(id)

    def getImportance2(self, employees: list, id: int) -> int:
        res = 0
        imp = {}
        sub = {}
        empids = []
        for emp in employees:
            imp[emp.id] = emp.importance
            sub[emp.id] = emp.subordinates
            if emp.id == id:
                empids.append(emp.id)
                empids.extend(emp.subordinates)

        for empid in empids:
            for subid in sub[empid]:
                if subid not in empids:
                    empids.append(subid)

        # print(empids)
        # print(imp)
        for empid in empids:
            res += imp[empid]
        return res


employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]; id = 1
employees = [Employee(1,5,[2,3]), Employee(2, 3, []), Employee(3, 3, [])]; id = 1

# employees = [[1,5,[2,3]],[2,3,[4]],[3,4,[]],[4,1,[]]]; id = 1
employees = [Employee(1,5,[2,3]), Employee(2,3,[4]), Employee(3,4,[]), Employee(4,1,[])]; id = 1
employees = [Employee(1,5,[2,3]), Employee(2,3,[4]), Employee(3,4,[]), Employee(4,1,[5]), Employee(5,1,[])]; id = 1

s = Solution()
print(s.getImportance(employees, id))
print(s.getImportance2(employees, id))


