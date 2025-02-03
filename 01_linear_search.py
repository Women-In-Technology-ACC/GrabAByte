# Linear Search

# A linear search is a basic algorithm that sequentially checks 
# each element in a list until the desired value is found or the
# list ends.

#################################################################

# SET VARIABLES
# the array we are searching
array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# the value we are searching for
target = 70

# the index of the target value
result = -1



# THE LOOP 
# loop through the array, checking each element to see if it matches
# the target value, if it does, set the result to the index 
for index in range(len(array)):
  print(f"Interation {index} | Value: {array[index]}")
  if array[index] == target:
    print("Element found!")
    result = index



# PRINT RESULTS
# check the value of result to see if it is an index or if it is -1
if result != -1:
  print("Element found at index: ", result)
else:
  print("Element is not in the array!")



#################################################################
# O NOTATION - Linear Time O(n)

# A linear time O Notation calculates the sum of the max interations
# it would take to complete

# For a linear search, it would be as if the desired value is in the
# last spot in the array. It would have to iterate through the entire
# array to find it.


# # UNCOMMENT HERE DOWN
# # Initialize the sum variable
# total_sum = 0

# # Loop through the array and add 1 for each iteration
# for element in array:
#   total_sum += 1
#   print("Iteration: ", total_sum)


# # PRINT RESULTS
# print("The total iterations are: ", total_sum)

