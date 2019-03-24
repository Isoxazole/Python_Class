
import math

def palindrome(word):
    takeOut = [",", "?", "!", "'", ".", "(", ")", " "]
    if type(word) is str:
        word = word.lower()
        for thing in takeOut:
            word = word.replace(thing , "")
        print(word)
        firstHalf = word[:round(len(word)/2)]
        secondHalf = word[math.floor(len(word)/2):]
        counter = 1
        isPalindrome = True
        for aWord in firstHalf:
            if aWord != secondHalf[-counter]:
                isPalindrome = False
                break
            else:
                counter += 1
        if isPalindrome:
            print("Yes, Palindrome!")
        else:
            print("No! Not Palindrome!")
    else:
        print("%s is not a string!" % (word))

palindrome("Eva, Can I Stab Bats In A Cave?")
