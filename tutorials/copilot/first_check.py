def factorial(n):
    """Compute factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(4))  # Example usage