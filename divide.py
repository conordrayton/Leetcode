# given two integers dividend and divisor divide 2 ints
# without using division multiplication and mod operator
#return the quotient / answer and truncate toward zero
#ie truncate(8.345)=8
#2^31 - 1 when division result overdlows

#this works leetcode just exceeds recursion limit

import timeit
start=timeit.default_timer()

class Solution:
    def divide(self,dividend: int, divisor: int) -> int:
        output=0
        dividendbool=False
        divisorbool=False
        if dividend <=0:
            dividendbool=True
            dividend *=-1
        if divisor <=0:
            divisorbool=True
            divisor *= -1
        result=dividend-divisor
        if result>=0:
            output+=1
            output+=Solution.divide(self,result,divisor)
        if -2147483649 >= output >= 2147483647: # test that it falls in appropriate region
            return 2147483647

        if (dividendbool==False and divisorbool==False) or (dividendbool==True and divisorbool==True):
            return output
        else:
            return output*-1


s=Solution()
x=Solution.divide(s,88,4)
print(x)


