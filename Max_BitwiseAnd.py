
def largestCombination(candidates: list[int]) -> int:
    max_count = 0
    # Iterate over each bit position (0 through 31 for typical integer range)
    for bit in range(32):  # Assuming integers are up to 32 bits
        count = 0
        for candidate in candidates:
            # Check if the current bit is set (i.e., if candidate & (1 << bit) is non-zero)
            if candidate & (1 << bit):
                count += 1
        # Update max_count if this bit position has more numbers with this bit set
        max_count = max(max_count, count)

    return max_count


# array=[16,17,71,62,12,24,14]
array=[84,40,66,44,91,90,1,14,73,51,47,35,18,46,18,65,55,18,16,45,43,58,90,92,91,43,44,76,85,72,24,89,60,94,81,90,86,79,84,41,41,28,44]

print(largestCombination(array))
