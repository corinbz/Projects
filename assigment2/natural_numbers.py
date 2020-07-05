# Find the sum of all the multiples of 3 or 5 below 1000.

# Generate a list of all multiples of 3 or 5
multiples = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
print(sum(multiples))