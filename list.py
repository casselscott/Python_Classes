import random

# Step 1: Generate a random list of 10 integers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]
print("Random List:", random_list)

# Step 2: Find and print the maximum and minimum values in the list
max_value = max(random_list)
min_value = min(random_list)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)

# Step 3: Reverse the list and print it
random_list.reverse()
print("Reversed List:", random_list)

# Step 4: Convert the list to a tuple and print it
random_tuple = tuple(random_list)
print("Tuple:", random_tuple)

# Step 5: Check if a specific number is in the list and print a message
specific_number = 50
if specific_number in random_list:
    print(f"{specific_number} is in the list.")
else:
    print(f"{specific_number} is not in the list.")
