def is_palindrome(string: str) -> bool:
    """Return True if string is Palindrome"""
    if not isinstance(string, str):
        raise TypeError("Imput must be a string")
    
    string = string.lower().replace(" ", "")
    str_len = len(string)

    for i in range(str_len // 2):
        if string[i] != string[str_len - i - 1]:
            return False
        
    return True    

def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    if not isinstance(string, str):
        raise TypeError("Imput must be a string")
    
    vowels = set("aeiou")
    count = 0

    return sum(1 for char in string.lower() if char in vowels)
