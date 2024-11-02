import sys

# Measure size of an integer
print(f"size of expty list is: {sys.getsizeof([])}")
# byte_array = bytes([65, 66, 67])
# list = [65, 66, 67]
# byte_array = bytearray([65, 66, 255])
# byte_array[0] = 89
# print(byte_array)
# print(f"the size of the byte array is:{sys.getsizeof(byte_array)}")
# print(f"the size of the array is:{sys.getsizeof(list)}")
#
# # Creating a bytearray from a string
# byte_array = bytearray(b"Hello")
# print(byte_array)  # Output: bytearray(b'Hello')
#
# # Modifying the bytearray
# byte_array[0] = 74  # ASCII for 'J'
# print(byte_array)
# Memory view
# data=bytearray("Hello word",'utf-8')
data = bytearray(b"Hello word")
print(data[0])
print(f"this is data: {data}")
mv = memoryview(data)
print(f"memoryview of data is: {mv}")
print(
    f"data at the first byte by memoryview: {mv[0]}"
)  # Output: 72 (ASCII value of 'H')
# Slicing the memoryview (returns a new memoryview)
sub_mv = mv[0:5]
print(type(sub_mv))
print(sub_mv.tobytes())

b = "Hello, World!"
print(b[-5:-2])
