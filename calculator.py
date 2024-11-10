class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        abs_b = b if b >= 0 else -b  # Absolute value of b
        for _ in range(abs_b):  # Loop abs(b) times, not abs(b) + 1
            result = self.add(result, a)
        if b < 0:  # If b is negative, invert the result
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = 0
        abs_a, abs_b = abs(a), abs(b)  # Work with absolute values
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
            result += 1
        if (a < 0) != (b < 0):  # Ensure correct sign of result
            result = -result
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot take modulo by zero")
        abs_a, abs_b = abs(a), abs(b)  # Use absolute values for calculation
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
        return abs_a if a >= 0 else -abs_a  # Return remainder with the correct sign


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))