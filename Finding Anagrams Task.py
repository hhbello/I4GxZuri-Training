# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    # [assignment] Add your code here
    word = input("Type first Word here: ")
    anagram = input("Type second word here: ")

    if(sorted(word) == sorted(anagram)):
        print(sorted(word), sorted(anagram))
        return True
    return False

print(find_anagram())
