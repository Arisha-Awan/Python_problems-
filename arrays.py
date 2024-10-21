import sys

# Measure size of an integer
# print(sys.getsizeof(42))
byte_array = bytes([65, 66, 67])
list = [65, 66, 67]
byte_array = bytearray([65, 66, 255])
byte_array[0] = 89
print(byte_array)
print(f"the size of the byte array is:{sys.getsizeof(byte_array)}")
print(f"the size of the array is:{sys.getsizeof(list)}")

# Creating a bytearray from a string
byte_array = bytearray(b"Hello")
print(byte_array)  # Output: bytearray(b'Hello')

# Modifying the bytearray
byte_array[0] = 74  # ASCII for 'J'
print(byte_array)
