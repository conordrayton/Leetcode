#give a roman numeral return the integer
# I =1 V=5 X=10 L=50
# C=100 D=500 M=1000


#faster than 5.02% and 84.08% less than memory

# roman_dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,
#                   "D":500,"M":1000,"IV":4,"IX":9,"XL":40,
#                   "XC":90,"CD":400,"CM":900}

# def romanToInt(s: str) -> int:
#     num =0
#     for i,value in enumerate(s[::-1]):
#         previous_value=" "
#         possible_value=" "
#         if i!=0:
#             past_index=len(s)-i
#             previous_value=value+s[past_index]
#         if i!=(len(s)-1):
#             index=len(s)-2-i
#             possible_value=s[index]+value
#
#         if previous_value in roman_dictionary:
#             continue
#         if possible_value in roman_dictionary:
#             num+=roman_dictionary[possible_value]
#         else:
#             num+= roman_dictionary[value]
#     return num


#one below is only 10% faster and 84% better memory management
# def romanToInt(s: str) -> int:
#     num =0
#     i=0
#     while i <= (len(s)-1): #going through the string s
#         possible_value=" "
#         if i!=(len(s)-1):
#             #as long as not the last index of string theres a possible
#             #value consisting of two chars ie IV or CM
#             possible_value=s[i]+s[i+1]
#         if possible_value in roman_dictionary:
#             num+=roman_dictionary[possible_value]
#             #if this possible value is in the dictionary add its value
#             i+=2
#             #increase i by two to skip over the chars
#             continue
#         else:
#             num+= roman_dictionary[s[i]]
#             #otherwise just increase by the single char
#         i+=1 # increment i
#     return num


#this ones worse but really good memory management
# def romanToInt(s: str) -> int:
#     num =0
#     i=0
#     while i <= (len(s)-1): #going through the string s
#         if i!=(len(s)-1) and (s[i]+s[i+1] in roman_dictionary):
#             num+=roman_dictionary[s[i]+s[i+1]]
#             i+=2
#         else:
#             num+=roman_dictionary[s[i]]
#             i+=1
#     return num




def romanToInt(s: str) -> int:
    num =0
    i=0
    roman_dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,
                      "D":500,"M":1000,"IV":4,"IX":9,"XL":40,
                      "XC":90,"CD":400,"CM":900}

    while i < len(s): #going through the string s
        if i+1<len(s) and (s[i]+s[i+1] in roman_dictionary):
            num+=roman_dictionary[s[i]+s[i+1]]
            i+=2
        else:
            num+=roman_dictionary[s[i]]
            i+=1
    return num




x="LVIII"

y=print(romanToInt(x))


#possible recursive function