from collections import defaultdict
def compressedString(word: str) -> str:
    length=len(word)
    count=1
    comp=[]
    for i in range(1,length):
        if word[i]==word[i-1] and count<9:
            count+=1
        else:
            comp.append(f"{count}{word[i-1]}")
            count=1
    comp.append(f"{count}{word[i - 1]}")
    return ''.join(comp)



word= "aaaaaaaaaaaaaabb"
output=compressedString(word)
print(output)