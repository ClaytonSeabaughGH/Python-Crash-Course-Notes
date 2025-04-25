# Create a list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Use the append method to add to the list
motorcycles.append('ducati')
print(motorcycles)

# Fill an empty list using append method
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Add a new element using insert method
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Use del statement to remove an item from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# Remove an item using pop() method. This removes last item from list
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {last_owned}")
print(f"The first motorcycle I owned was a {first_owned}")

# Use remove method to remove a motorcycle from the list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# You can use the remove method to work with a variable
# The remove method only deletes the first occurence of the value. You have to use a loop if you want to remove all of the occurances
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)