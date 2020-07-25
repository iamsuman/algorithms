def sum_finding_dfs(nums, target):
    frontier = [(0, [])]
    while frontier:
        partial_sum, nums_so_far = frontier.pop()
        if partial_sum == target:
            yield nums_so_far
            continue
        if partial_sum > target:
            continue

        for num in nums:
            if not nums_so_far or num >= nums_so_far[-1]:
                frontier.append((partial_sum + num, nums_so_far + [num]))


class Solution():
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        unique_nums = list(set(A))
        unique_nums.sort(reverse=True)
        return list(sum_finding_dfs(unique_nums, B))

a = Solution()
print(a.combinationSum([2,3,6,7], 7))
