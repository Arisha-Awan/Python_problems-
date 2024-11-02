def isCircularSentence(sentence: str) -> bool:
    if not sentence[0] == sentence[-1]:
        return False
    words_list = sentence.split(" ")
    # if not words_list[0][0]==words_list[-1][-1]:
    #     return False
    for word, next_word in zip(words_list, words_list[1:]):
        if not word[-1] == next_word[0]:
            return False
    return True


sentence = "leetcode exercises sound delightful"
print(f"is circular {isCircularSentence(sentence)}")

# sentence.split(" ") will split the string specifically at each single space (" ").
list = "hello    world".split(" ")  # Output: ['hello', '', '', 'world']
print(list)
# sentence.split() (with no argument) will split on any whitespace (spaces, tabs, or newlines)
# and also automatically handle multiple consecutive spaces by treating them as a single separator.
# This avoids empty strings in the result. For example:
list = "hello    world".split()
print(list)
