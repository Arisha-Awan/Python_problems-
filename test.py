class Solution(object):
    def canSortArray(self, nums):

        length_arr = len(nums)
        if length_arr==1:
            return True
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
            same_SetBit_list = defaultdict(list)
            for num in nums:
                no_of_setBits = count_set_bits(num)
                same_SetBit_list[no_of_setBits].append(num)
            num1 = []
            for no_of_setBits in same_SetBit_list.keys():
                same_SetBit_list[no_of_setBits].sort()
                for nums in same_SetBit_list[no_of_setBits]:
                    num1.append(nums)

            return isArraySorted(num1)