def reverse_number(num:int)->int:
    rev_num=0
    while(num>0):
        digit=num%10
        rev_num=rev_num*10+digit
        num=num//10
    return rev_num

num=521
print(f"reverse of {num} is: {reverse_number(num)}")

# we can also convert number into string in python easily and then reverse it
def reverse_num_str(num:int)->int:
    rev_num=str(num)
    rev_num=rev_num[::-1]
    return str(rev_num)
num=5881
print(f"reverse of {num} is: {reverse_number(num)}")

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Test cases
num=16
print(f"{num} is power of 2 {is_power_of_2(num)}")  # True
num=18
print(f"{num} is power of 2 {is_power_of_2(num)}")  # False


