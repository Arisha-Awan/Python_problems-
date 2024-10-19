def dec_to_Binary(num:int):
    bin_num=""
    while num>0:
        rem=num%2
        bin_num=str(rem)+bin_num
        num=num//2
    return bin_num


num=9
print(f"The binary of {num} is: {dec_to_Binary(num)}")