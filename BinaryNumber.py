# If we want to return binary number string
def dec_to_Binary(num:int):
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