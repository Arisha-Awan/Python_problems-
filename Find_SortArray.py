# https://leetcode.com/problems/find-if-array-can-be-sorted/description/?envType=daily-question&envId=2024-11-06

def canSortArray(nums:list[int])->bool:
    length_arr = len(nums)
    from collections import defaultdict
    def count_set_bits(x):
        return bin(x).count('1')
    def isArraySorted(nums: list[int]) -> bool:
        is_sorted = False
        for i in range(length_arr - 1):
            if nums[i] <= nums[i + 1]:
                is_sorted = True
            else:
                return False
        return is_sorted
    if isArraySorted(nums):
        return True
    else:
        same_SetBit_list=defaultdict(list)
        for num in nums:
            no_of_setBits=count_set_bits(num)
            same_SetBit_list[no_of_setBits].append(num)
        num1=[]
        print(same_SetBit_list)
        for no_of_setBits in same_SetBit_list.keys():
            same_SetBit_list[no_of_setBits].sort()
            # for nums in same_SetBit_list[no_of_setBits]:
            #     num1.append(nums)
            #     print(num1)
            num1.extend(same_SetBit_list[no_of_setBits])
            print(num1)

        return isArraySorted(num1)
# def canSortArray(nums:list[int])->bool:
#
#     from collections import defaultdict
#     def count_set_bits(x):
#         return bin(x).count('1')
#
#     if nums==sorted(nums):
#         return True
#     else:
#         same_SetBit_list=defaultdict(list)
#         for num in nums:
#             no_of_setBits=count_set_bits(num)
#             same_SetBit_list[no_of_setBits].append(num)
#         for no_of_setBits in same_SetBit_list.keys():
#             same_SetBit_list[no_of_setBits].sort()
#         reconstructed_array = []
#         print(same_SetBit_list)
#         for num in nums:
#             print(num)
#             set_bit_count = count_set_bits(num)
#             # Pop the smallest element from the sorted group
#             reconstructed_array.append(same_SetBit_list[set_bit_count].pop(0))
#             print(reconstructed_array)
#
#         return reconstructed_array==sorted(nums)
#
#
#
#
#
#
#
#



array=[136,256,10]
# array=[1,2,3,4,5]
print(f"is string can be sorted {'yes' if canSortArray(array) else 'No'}")