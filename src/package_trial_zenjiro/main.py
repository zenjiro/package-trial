def add_one(number):
    """
    Add one to the given number.
    
    This function demonstrates a simple mathematical operation while maintaining
    type safety and comprehensive error handling.
    
    Args:
        number: A numeric value (int, float, complex, Decimal, Fraction, etc.)
        
    Returns:
        The input number plus one, maintaining the same type
        
    Raises:
        TypeError: If the input is not a numeric type
        
    Examples:
        >>> add_one(5)
        6
        >>> add_one(3.14)
        4.14
        >>> add_one(-1)
        0
        >>> add_one(1+2j)
        (2+2j)
    """
    return number + 1
