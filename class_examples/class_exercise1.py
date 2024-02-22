my_list = [
  "one",
  "two",
  "three"
]

new_dict = {}

# code goes here
for i, item in enumerate(my_list):
  upper_item = item.upper()
  new_dict[upper_item] = i + 1
  # new_dict = {i:upper_item for i in range(len(my_list))}

print(new_dict)
# {"ONE": 1, "TWO":2, "THREE":3}