even_numbers = [i for i in range(101) if i % 2 == 0] # All even numbers from 0 to 100
# print(even_numbers)

# every number between 0 and 100 divisible by 7
every_seven = [i for i in range(101) if i % 7 == 0] 
# print(every_seven)

new_list = []

# Get every number that is in BOTH lists
unique_set = set(even_numbers).intersection(set(every_seven))
# print(unique_set)

# Make a new list
# For each number common in both lists,
# Each number should NOT BE WITH DECIMAL (just integers)
new_list = [int(i / 2) for i in unique_set]


# Print the new list SORTED from highest to lowest
new_list.sort(reverse=True)


print(new_list)