# This introduces using an f-string. The f stands for format
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

# You can compose complete messages with f strings
first_name = "ada"
last_name = "lovelace"
full_name = f"Hello, {first_name} {last_name}"

print(full_name)

# You can use f-strings to compose a message and then asign it to a variable
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Helllo, {full_name.title()}!"

print(message)