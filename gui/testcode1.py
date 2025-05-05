# Get user input for the number of elements
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store the array elements
my_array = []

# Use a for loop to read the array elements
for i in range(n):
    element = int(input())
    my_array.append(element)

# Display each element one by one
print("Array elements:")
for element in my_array:
    print(element)
