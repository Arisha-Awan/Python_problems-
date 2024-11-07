def zero_one(arr:list)->None:
    count_of_one=arr.count(1)
    arr=[1]*count_of_one+[0]*(len(arr)-count_of_one)
    return arr


array = [1,0,1,0,1,0,1,0,1]
print(f"arry after arranging {zero_one(array)}")
def check_anagrams(str1:str,str2:str)->bool:
    if len(str1)!=len(str2):
        return False
    return sorted(str1)==sorted(str2)

string_1 = "cat"
string_2 = "act"
print(f"{string_1 }")

def sort_single_pass(arr):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True
    return arr





# Example usage
array = [1, 4, 8, 3, 8, 3, 5, 0]
sorted_array =sort_single_pass(array)
print(sorted_array)
