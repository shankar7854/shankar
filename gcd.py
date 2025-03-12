def gcd(a, b):
    # Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Calculate LCM using the formula: LCM(a, b) = abs(a * b) / GCD(a, b)
    return abs(a * b) // gcd(a, b)

# Example usage:
result = lcm(12, 15)
print(result)  # This will print 60, the LCM of 12 and 15
