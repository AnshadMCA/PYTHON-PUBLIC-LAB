def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    num_digits = len(digits)
    return sum(digit ** num_digits for digit in digits) == number
