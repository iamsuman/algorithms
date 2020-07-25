phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

def num_to_alpha(A):
    res = ""
    for i in A:
        L = phone[i]
        for j in L:
            for k in L:
                if j == k:
                    continue
                print(j + k)

num_to_alpha("23")





