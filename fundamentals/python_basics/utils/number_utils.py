def is_even(number: int) -> bool:
    """Return True if number is even.
    Examples:
        >>> is_even(24)
        True
        >>> is_even(51)
        False
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0

def is_prime(number: int) -> bool:
    """Return True if given integer is prime."""
    if not isinstance(number, int):
        raise TypeError('Input must be an integer')
    
    if number < 2:
        return False
   
    for i in range(2 , int(number ** 0.5) + 1):
        if number % i == 0: 
            return False 
        
    return True 

def reverse_number(number: int) -> int:
    """Return the reverse of given integer."""
    if not isinstance(number, int):
        raise TypeError("Input must be a integer")
    
    sign = -1 if number < 0 else 1
    number = abs(number)

    temp = number
    reversed_number = 0
    while temp > 0:
        reversed_number = reversed_number * 10 + (temp % 10)
        temp //= 10

    return reversed_number * sign 
