def palindrome_checker(word: str):
    return word == word[::-1]


type_your_word = "kajak"
result = palindrome_checker(type_your_word)
print(result)
