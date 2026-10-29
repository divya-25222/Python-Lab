#If a text is given and we reshuffle the text will it be plaindrome

def check_palindrome(text):
    dict = {}
    odd = even = 0
    for i in text:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i]+1
    for a in dict.values():
        if a % 2 != 0:
            odd = odd+1
    return odd <=1


    

text = input("Enter the text: ")
if check_palindrome(text) : 
    print('Palindrome')
else : 
    print('Not a Palindrome')
