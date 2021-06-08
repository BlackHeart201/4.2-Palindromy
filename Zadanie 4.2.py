def palindrome_checker(word: str):
    """
        Check palindrome based on typed word
    """
    return word == word[::-1]


type_your_word = "kajak"
result = palindrome_checker(type_your_word)
print(result)
