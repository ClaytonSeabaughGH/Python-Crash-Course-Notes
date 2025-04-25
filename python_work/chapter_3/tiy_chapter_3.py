# 3.1: Store names of friends in a list
names = ['Zach', 'Rachel', 'Cassie']

# Print each person's name by accessing each element
print(names[0])
print(names[1])
print(names[2])

# Create a greeting for people in the list
first_message = (f"Nice to meet you {names}. My name is Clayton!")
print(first_message)

# 3-4 Make a list that has people you would like to invite to dinner. use the list to print a message to each person
message1 = (f"{names[0]}, you are cordially invited to dinner on April 21st")
message2 = (f"{names[1]}, you are cordially invited to dinner on April 21st")
message3 = (f"{names[2]}, you are cordially invited to dinner on April 21st")
print(message1)
print(message2)
print(message3)


# 3-5 
print('Jeffery')
names.remove('Cassie')
names.append('Jeffery')
message1 = (f"{names[0]}, you are cordially invited to dinner on April 21st")
message2 = (f"{names[1]}, you are cordially invited to dinner on April 21st")
message3 = (f"{names[2]}, you are cordially invited to dinner on April 21st")

print(names)
print(message1,message2,message3)
# 3-6
print()

names.insert(0,'Cassie')
names.insert(3,'Nyx')
names.append('Carissa')
print(names)

# 3-7
# New message I only have space for two people
sorry_message = (f"{names.pop()}, I am so sorry I can only have 2 people for dinner")

print(sorry_message)
print(sorry_message)

del names[0]
del names[1]
print(names)