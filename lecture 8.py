def power(x, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return x * power(x, n - 1)

# Example usage
x = 2
n = 3
print(f"{x} raised to the power of {n} is: {power(x, n)}")
