person = {
  "first_name": "Erik",
  "last_name": "Whiting",
  "age": 35
}

person['shoe_size'] = 11

person.pop("shoe_size")

shoe_size = person.get('shoe_size', "I don't know")
print(f'Shoe size is {shoe_size}')

