def minChange(s:str)->int:
    count=0
    length=len(s)
    for i in range(0,length,2):
        if s[i]!=s[i+1]:
            count=count+1
    return count
s="0101"
print(minChange(s))
