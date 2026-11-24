class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):

                a = num[:i]
                b = num[i:j]

                if (len(a) > 1 and a[0] == '0'):
                    continue

                if (len(b) > 1 and b[0] == '0'):
                    continue

                x, y = int(a), int(b)
                k = j

                while k < n:
                    total = str(x + y)

                    if not num.startswith(total, k):
                        break

                    k += len(total)
                    x, y = y, x + y

                if k == n:
                    return True

        return False