def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

# Example usage:
decimal_number = 25
print(f"Binary of {decimal_number} is: {decimal_to_binary(decimal_number)}")
