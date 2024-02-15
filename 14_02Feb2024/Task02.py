"""palindrome using function"""


def palindrome(rev_name):
    name = input("Enter your name")
    for i in range(1, len(name) + 1):
        rev_name = rev_name + name[-i]
    if name == rev_name:
        print(f"{rev_name} is a palindrome")
    else:
        print(f"{rev_name} is Not a palindrome")
    return rev_name


palin = palindrome("")
print(palin)
