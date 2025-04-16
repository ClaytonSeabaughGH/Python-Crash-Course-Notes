# Create a list of bicycles
bicycles =  ['trek', 'cannondale', 'redline', 'specialized']

# Indexes start at 0 not 1
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

# If you do negatives then it starts from the back of the list 
print(bicycles[-1])

# Print a message using a list
message = (f"My first bicycle was a {bicycles[0].title()}.")
print(message)