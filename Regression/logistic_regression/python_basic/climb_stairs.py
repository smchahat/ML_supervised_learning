#leetcode 70

class Solution:
    def climbStairs(self, n: int) -> int:

        def steps(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            

            return steps(n-1) + steps(n-2)

        val = steps(n)

        return n
        