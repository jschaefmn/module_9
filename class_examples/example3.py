person = {
  "first_name": "Erik",
  "last_name": "Whiting",
  "age": 35
}

# popped_item = person.pop("first_name")

# print(person)
# print(popped_item)

# for key in person:
#   print(person[key])

person_list = []

for k in person:
  person_list.append(person.pop[k])

person.clear()
print(person_list) # [jake, schaefbauer, 24]
print(person) #{}