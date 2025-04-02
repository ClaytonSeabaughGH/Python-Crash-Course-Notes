# 2-3 Use a variable to reprsent a name and print a message to that person
name = "Eric"
print(f'Hello {name}, would you like to learn some Python today?')

# 2-4 Use a variable to represent a person's name and then print that name in all cases
my_name = "clayton seabaugh"
print(my_name.title())
print(my_name.lower())
print(my_name.upper())

# 2-5 and 2-6 Find a quote, print the quote and name of author. 
author = "René Descartes"
quote = '"I think, therefore I am"'
print(f'{author} once said, {quote}')

# 2-7 Use a variable to represent a person's name with white space. Practice lstrip, rstrip, and strip
random_name = " Jerry "
print(random_name.lstrip())
print(f'Name: \t {random_name.rstrip()}')
print(f'Name: \n{random_name.strip()}')

# 2-8 Use removesuffix 
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))