#given array and a target sum return the indices of the two
#that give said sum
#soln correct memory better than 65.57%
#but runtime only better than 5%




# def TwoSum(nums: list[int], target: int) -> list[int]:
#     value1=0
#     value2=0
#     returnlist=[]
#     for index,number in enumerate(nums):
#         value1=number
#         for indexj,numberj in enumerate(nums):
#             if indexj == index:
#                 continue
#             value2=numberj
#             if value1+value2 == target:
#                 returnlist.append(index)
#                 returnlist.append(indexj)
#                 return returnlist


#try again but for faster runtime
#making a dictionary
# runtime faster than 96.11%
#memory 41.01%


def TwoSum(nums: list[int], target: int) -> list[int]:
    dictionary={}
    for index,value in enumerate(nums):
        dictionary[value]=index
    for i,num in enumerate(nums):
        potentialMatch=target-num
        if potentialMatch in dictionary:
            key=dictionary[potentialMatch]
            if i == key:
                continue

            return [dictionary[potentialMatch],i]

#for this one i create a dictionary where the keys are the values
#of the list and the values of the dictionary are just the index position
#go through the list of nums and have a potential match be the current value
# minus the target value
# search the dictionary if the potential match (key exists)
# however if the value returned is equal to the current iteration of i
# skip over as you can have matching indexes
#otherwise return the value and current iteration of i
# results in speed faster than 96.11% but memory less than 41.01%













numbers=[3,2,4]
piss=TwoSum(numbers,6)
print(piss)





