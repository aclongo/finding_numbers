# Finding Numbers in a Haystack
# A program that can read through and parse a file with text and numbers. It will extract all the numbers in the file and compute the sum of the numbers.
import re

print('FINDING NUMBERS IN A HAYSTACK')
while True:
    try:
        fname = input('Enter the file name you would like to extract numbers from: ')
        # Open the file and create a file handle for reading through it
        fhand = open(fname)
        break
    # Prevent program from crashing if user enters a bad file name
    except FileNotFoundError:
        print('File not found. Try again.')
        continue

# Start counters for the current line number, how many numbers were found, and the sum of all the numbers
sum = 0
count = 0
line_count = 0

# Read through each line in the file
for line in fhand:
    # Make a list of all numbers in the current line
    numbers = re.findall('[0-9]+', line)
    # Increase the line counter
    line_count += 1
    # Only continue with lists that actually contain numbers
    if numbers:
        print(f'In line number {line_count}, I found the following number(s): {numbers}')
        # Read through each number in the current line list
        for number in numbers:
            # Increase the number count
            count += 1
            # Add the current number to the sum
            sum += int(number)

print(f'I found a total of {count} numbers in this file.')
print(f'The sum of all the numbers in this file is {sum}.')