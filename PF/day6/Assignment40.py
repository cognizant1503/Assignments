#PF-Assgn-40
def is_palindrome(word):
    word=word.upper()
    if len(word)<=1:
        return True
    elif word[0]==word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
result=is_palindrome("stocks")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
