def rotateStr(s:str,goal:str)->bool:
    if len(s) != len(goal):
        return False
    length_str=len(s)
    count=0
    while(count<length_str):
        s = s[1:]+s[0]
        if s==goal:
            return True
        count=count+1
    return False

# Easy Way
def rotate_string(s: str, goal: str) -> bool:
    # Check if lengths are the same and if goal is a substring of s + s
    return len(s) == len(goal) and goal in (s + s)


# Example Usage
s="abcde"
goal = "cdeab"
print(f"is string  is  RotatingStr {'yes' if rotateStr(s,goal) else 'NO'}")

s="abcde"
goal = "cdeab"
goal = "abced"
print(f"is string  is  RotatingStr {'yes' if rotateStr(s,goal) else 'NO'}")

print(s)