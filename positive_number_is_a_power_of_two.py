# Write a python program to check if a positive integer 
# value is a power of 2. (e.g 4 is a power of 2)

import math

number = int(input('Enter number: '))

def log_2(x):
    return (math.log10(x) / 
            math.log10(2));

# Function to check if function is a power of 2
def is_power_of_two(n):
    return (math.ceil(log_2(n)) == math.floor(log_2(n))); 


# Check if number is a positive integer.
if number < 0:
    print('Number is not a positive integer.')
else:
    if is_power_of_two(number):
        print('Number is a power of 2')
    else:
        print('Number is not a power of 2')