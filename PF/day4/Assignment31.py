#PF-Assgn-31
def check_palindrome(word):
    reverse_word=word[::-1]
    status=False
    
    if(reverse_word==word):
        status=True
    else:
        status=False
    return status

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")