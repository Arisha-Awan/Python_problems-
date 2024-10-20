# If we want to return binary number string
def dec_to_Binary(num:int)->str:
    bin_num=""
    while num>0:
        rem=num%2
        bin_num=str(rem)+bin_num
        num=num//2
    return bin_num
# if we want to return binary number
def dec_to_binary(num: int) -> int:
    binary_num = 0  # Store the binary number as an integer
    place_value = 1  # Track the place value (1, 10, 100, etc.)

    while num > 0:
        rem = num % 2  # Get the remainder (0 or 1)
        binary_num += rem * place_value  # Add the binary digit at the correct place value
        place_value *= 10  # Move to the next place value
        num = num // 2  # Use integer division to update the number

    return binary_num



num=9
print(f"The binary of {num} is: {dec_to_Binary(num)}")

# Binary to decimal Convertion
def bin_to_decimal(bin_num:int)->int:
    dec_num=0
    pow=1 #2^0
    while(bin_num>0):
        rem=bin_num%10
        dec_num+=rem*pow
        bin_num//=10
        pow*=2
    return dec_num

bin_num=1100101
print(f"Binary number {bin_num} decimal is {bin_to_decimal(bin_num)}")

print(f"bitwise and of 6 and 10 :{6&10}")
print(f"bitwise or  of 6 and 10 :{6|10}")
print(f"bitwise xor of 6 and 10 :{6^10}") #same bit 0 diff bits 1
print(f"bitwise left-shift 10 by 2 :{10<<2}")
# Shift left by pushing zeros in from the right and let the leftmost bits fall off
# Formula:   a<<b==a*2^b
print(f"bitwise right-shift 10 by 2 :{10>>2}")
# Shift right by pushing copies of the leftmost bit in from the left, and let
# the rightmost bits fall off
# Formula:   a>>b==a//2^b
