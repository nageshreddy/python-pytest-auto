from collections import Counter

# Example list of numbers
numbers = [4, 2, 2, 8, 3, 3, 3, 1, 4, 2]

# Count occurrences
count = Counter(numbers)

# Print result
for number, freq in count.items():
    print(f"{number}: {freq}")
