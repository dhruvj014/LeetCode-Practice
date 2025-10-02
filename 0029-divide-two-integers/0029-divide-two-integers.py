class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == divisor):
            return 1
        sign = True
        if(dividend>=0 and divisor<0):
            sign = False
        if(dividend<0 and divisor>0):
            sign = False
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while(n>=d):
            ctr = 0
            while(n>= (d<<(ctr+1))):
                ctr+=1
            ans+=(1<<ctr)
            n = n - (d*(1<<ctr))

        ans = ans if sign else -ans

        # Clamp the result to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        return min(max(ans, INT_MIN), INT_MAX)