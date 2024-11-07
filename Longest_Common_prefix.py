def longest_common_prefix(strs):
    if not strs:
        return ""
    length_str=len(strs[0])
    for i in range(length_str):  # Loop through the first string's characters
        char = strs[0][i]
        for s in strs[1:]:
            # If index exceeds length or characters don't match, return the prefix found so far
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]


# Example Usage
strings = ["flower", "flow", "flowing"]
print("Longest Common Prefix:", longest_common_prefix(strings))