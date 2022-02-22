#sorted array and a target value return the index if target found
#otherwise return where it would be if inserted in order




# def searchInsert(nums: list[int], target: int) -> int:
#     numsdict=dict(zip(nums,range(len(nums))))
#     if target in numsdict:
#         return numsdict[target]
#     if target < nums[0]:
#         return 0
#     if target> nums[len(nums)-1]:
#         return len(nums)
#     else:
#         while True:
#             target-=1
#             if target in numsdict:
#                 return numsdict[target]+1


#make a dictionary of the list because its always faster
# if the target is less than smallest value must be 0
# if greater than larger must have an index of the size of list
# otherwise continuously subtract the target and see if its in the dictionary
# this is because now the target must be greater than something in the dictionary
#therefore subtract until you find it then the index must be one greater
#the zip function retusn a zip object which is an iterator of tuples
#where the first item of each passed iterator is paired together
#create a dict and then zip nums and range of numbers
#therefore nums is the key and basically index as value



#kinda shit should use a binary search tree
#binary search tree classic algorithm very fast
def searchInsert(nums: list[int], target: int) -> int:
    start=0
    end=len(nums)-1
    mid=0
    while start<=end:
        mid=(end+start)//2
        if target<nums[mid]:
            end=mid-1
        elif target> nums[mid]:
            start=mid+1
        else:
            return mid
    return end+1





nums=[1,3,5,6]
print(searchInsert(nums,4))






