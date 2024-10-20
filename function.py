# Write a Python function that takes a list
# of numbers as input and returns the sum of all even numbers in the list.

'''def sum_of_even_numbers(numbers):
    # Use reduce to calculate the sum of even numbers
    from functools import reduce

    # Filter even numbers from the list
    even_numbers = filter(lambda x: x % 2 == 0, numbers)

    # Use reduce to sum the even numbers
    total = reduce(lambda x, y: x + y, even_numbers)

    return total

numbers_list = [47, 11, 42, 13, 8, 20]
result = sum_of_even_numbers(numbers_list)
print(result)  # Output: 70
'''

#2. Create a Python function that accepts a string and returns the reverse of that string.

'''def reverse_string(s):
    # Reverse the string using slicing
    return s[::-1]

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: !dlroW ,olleH
'''



#3. Implement a Python function that takes a list of integers
# and returns a new list containing the squares of each number

'''def square_numbers(numbers):
    # Use list comprehension to create a new list with squares of each number
    squares = [x ** 2 for x in numbers]
    return squares

# Example usage
input_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_list)
print(squared_list)  # Output: [1, 4, 9, 16, 25]
'''

#4. Write a Python function that checks if a given number is prime or not from 1 to 200.

'''def is_prime(n):
    # Check if the number is within the valid range
    if n < 1 or n > 200:
        return "Number must be between 1 and 200."
    
    # Handle special cases for 1 and 2
    if n == 1:
        return False  # 1 is not a prime number
    if n == 2:
        return True   # 2 is a prime number

    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a factor, so it's not prime

    return True  # No factors found, so it's prime

# Example usage
number_to_check = 29
result = is_prime(number_to_check)
print(f"{number_to_check} is prime: {result}")  # Output: 29 is prime: True
'''


#5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of
#terms.

'''def fibonacci_generator(terms):
    a, b = 0, 1  # Starting values of the Fibonacci sequence
    for _ in range(terms):
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update to the next Fibonacci number

# Example usage
num_terms = 10
fibonacci_sequence = fibonacci_generator(num_terms)

print(f"Fibonacci sequence up to {num_terms} terms:")
for number in fibonacci_sequence:
    print(number)
'''


#6. Write a generator function in Python that yields the powers of 2 up to a given exponent.

'''def powers_of_two(exponent):
    for i in range(exponent + 1):
        yield 2 ** i  # Yield the power of 2 for the current exponent

# Example usage
max_exponent = 5
powers = powers_of_two(max_exponent)

for power in powers:
    print(power)
'''

#7 file read
# not covered in the video, i need to learn this from youtube

#8 9. Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.


''''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Formula for conversion

celsius_temperatures = [0, 20, 37, 100, -40]

fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))


print("Celsius temperatures:", celsius_temperatures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)
'''

#10. Create a Python program that uses `filter()` to remove all the vowels from a given string'

'''
def is_not_vowel(char):
    vowel = "aeiou"
    return char.lower() not in vowel 

input_string = "Vivek"

# Using filter to remove vowels
filtered = filter(is_not_vowel, input_string))

# joining 
filtered_string = ''.join(filtered)

# Displaying the result
print("Original string:", input_string)
print("String after removing vowels:", filtered_string)
'''

