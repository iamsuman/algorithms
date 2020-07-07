class Merge():
    def merge_interval(self, intervals, newInterval):
        # [1,3],[6,9]
        # (4,9)
        final = []
        merge = False

        x, y = newInterval
        for a,b in intervals:

            if b < x:
                if not merge:
                    final.append([a,b])
                    merge = False
                else:
                    e = y
            elif a < x and x < b and b < y:
                if not merge:
                    merge = True
                    s = a
                    e = y
                else:
                    e = y
                    merge = False
            elif a < x and y < b:
                if not merge:
                    merge = False
                    s = a
                    e = b
                else:
                    e = b
                    merge = False
                    final.append([s, e])
            elif y < a:
                if not merge:
                    merge = False
                    s = x
                    e = y
                else:
                    e = y
                    final.append([s,e])
                    final.append([a,b])
                    merge = False

        return final

A = [[1,2],[3,5],[6,7],[8,10],[12,16]]
B = [4,9]
a = Merge()
final = a.merge_interval(A,B)
print(final)









