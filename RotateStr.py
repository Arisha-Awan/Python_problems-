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

print("print the rotate string")
s="abcde"
goal = "cdeab"

s ="abcde"
goal = "abced"
print(rotateStr(s,goal))

print(s)