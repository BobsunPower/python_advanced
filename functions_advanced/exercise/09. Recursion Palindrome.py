def palindrome(txt, i):
    if txt == txt[::-1]:
        return f"{txt} is a palindrome"
    else:
        return f"{txt} is not a palindrome"
