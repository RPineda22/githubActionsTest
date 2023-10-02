def add(x: float, y: float) -> float:
    """
    Perform addition of two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The result of addition.
    """
    return x + y

def subtract(x: float, y: float) -> float:
    """
    Perform subtraction of two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The result of subtraction.
    """
    return x - y

def multiply(x: float, y: float) -> float:
    """
    Perform multiplication of two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The result of multiplication.
    """
    return x * y

def divide(x: float, y: float) -> float:
    """
    Perform division of two numbers.

    Args:
        x (float): The dividend.
        y (float): The divisor.

    Returns:
        float: The result of division.
    """
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

# Example usage:
num1 = 14
num2 = 15

result_addition = add(num1, num2)
result_subtraction = subtract(num1, num2)
result_multiplication = multiply(num1, num2)
result_division = divide(num1, num2)

print(f"Addition: {num1} + {num2} = {result_addition}")
print(f"Subtraction: {num1} - {num2} = {result_subtraction}")
print(f"Multiplication: {num1} * {num2} = {result_multiplication}")
print(f"Division: {num1} / {num2} = {result_division}")
