# Create an empty list to store formatted numbers.
numbers = []

# Iterate through numbers from 0 to 999 (exclusive).
for num in range(1000):
    # Convert the number to a string and fill with zeros to make it three digits long.
    num = str(num).zfill(3)

# Print the last formatted number (outside the loop, indentation issue).
print(num)

# Append the last formatted number to the 'numbers' list.
numbers.append(num)