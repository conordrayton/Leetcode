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




# s=Solution()
# x=Solution.divide(s,7,3)
# print(x)



# def divide(dividend: int, divisor: int) -> int:
#
#     remainder=dividend
#     remainder=dividend<<1
#     # dividendbit = '{:064b}'.format(dividend)
#     # divisorbit = '{:064b}'.format(divisor)
#     upper_remainder=remainder>>32
#     lower_remainder=remainder & 0xffffffff
#     n=0
#     while n<32:
#         upper_remainder=remainder>>32
#         lower_remainder=remainder & 0xffffffff

#
#
#         upper_remainder=upper_remainder-divisor
#         remainder=(upper_remainder<<32)+lower_remainder
#         if remainder >=0:
#             (remainder<<1)+1
#
#         else:
#             upper_remainder=upper_remainder+divisor
#             remainder=(upper_remainder<<32)+lower_remainder
#             print('{:064b}'.format(remainder))
#             remainder=remainder<<1
#             print('{:064b}'.format(remainder))
#
#         n+=1
#     upper_remainder>>1
#     remainder=(upper_remainder<<32)+lower_remainder
#     return lower_remainder



def divide(dividend: int, divisor: int) -> int:
    divisor_upper=divisor<<32
    print('{:064b}'.format(divisor_upper))
    divisor_lower=0& 0xffffffff
    print('{:064b}'.format(divisor_lower))
    divisor=divisor_upper+divisor_lower
    print('{:064b}'.format(divisor))

    #
    # quotient=0
    # remainder=dividend
    # n=0
    # while n!=65:
    #     remainder=remainder-divisor
    #     if remainder >=0:
    #         quotient=(quotient<<1)+1
    #         print('{:064b}'.format(quotient))
    #     else:
    #         remainder=remainder+divisor
    #         quotient=(quotient<<1)
    #         print('{:064b}'.format(quotient))
    #     divisor=divisor>>1
    #     print('{:064b}'.format(divisor))
    #     n+=1
    # return quotient











# div=100
# x='{:064b}'.format(div)
# print(x)
# uppdiv=div>>32
# print('{:064b}'.format(uppdiv))
# lowerdiv=div & 0xffffffff
# print('{:064b}'.format(lowerdiv))

x=divide(7,2)
print(x)


stop=timeit.default_timer()
print('Time: ',stop-start)


















#this ones straight up dogshit
# def divide(dividend: int, divisor: int) -> int:
#     output=0
#     dividendbool=False
#     divisorbool=False
#     if dividend <=0:
#         dividendbool=True
#         dividend *=-1
#     if divisor <=0:
#         divisorbool=True
#         divisor *= -1
#     result=dividend-divisor
#     while result>=0:
#         result-=divisor
#         output+=1
#
#     if (dividendbool==False and divisorbool==False) or (dividendbool==True and divisorbool==True):
#         return output
#     else:
#         return output*-1
#
#
# x=divide(-3000000000,-4)
# print(x)
#
