class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        def backtrack(start, part, total):
            if len(part) == k:
                if total == n:
                    ans.append(part[:])
                return
            for i in range(start, 10):
                if total + i > n:
                    break
                backtrack(i + 1, part + [i], total + i) 

        backtrack(1, [], 0)
        return ans