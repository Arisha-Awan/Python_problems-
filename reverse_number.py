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

# 1-For n = 16 (binary: 10000):
# =>n−1=15 (binary: 01111)
# =>10000 & 01111 = 00000 (True)
#
# 2-For n = 18 (binary: 10010):
# =>n−1=17 (binary: 10001)
# =>10010 & 10001 = 10000 (False)
# This method is efficient and checks if a number is a power of 2 in constant time 𝑂(1).
# ==>Explanation
#  n&(n−1)=0 is true, where & is the bitwise AND operator. This works because subtracting
#  1 from a power of 2 flips all bits after the rightmost set bit to 1, and that bit itself to 0.
#  Taking the AND of 𝑛 n and 𝑛 − 1 n−1 will yield 0 if 𝑛 n is a power of 2.