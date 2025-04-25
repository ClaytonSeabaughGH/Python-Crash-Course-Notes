# Setting a list permantly witht he sort method
# This sorts the list in alphabetical order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sort list in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

# Use sorted() to order a list without changing the original
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list")
print(cars)

print("\nHere is the sorted list.")
print(sorted(cars))

print("\nHere is the original list again")
print(cars)

# Use reverse() method on a list
print(cars)

cars.reverse()
print(cars)