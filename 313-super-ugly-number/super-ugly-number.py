class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        ugly = [1] * n
        k = len(primes)

        idx = [0] * k
        val = primes[:]

        for i in range(1, n):
            mini = min(val)

            ugly[i] = mini

            for j in range(k):
                if val[j] == mini:
                    idx[j] += 1
                    val[j] = ugly[idx[j]] * primes[j]

        return ugly[n - 1]