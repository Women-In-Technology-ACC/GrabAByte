# Binary Search

# A binary search is an efficient algorithm for finding a target
# value within a sorted array by repeatedly dividing the search
# interval in half

#################################################################

# SET VARIABLES
# the array we are searching (MUST BE IN ORDER!)
array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# the value we are searching for
target = 70

# set the start and end of the search range
start = 0
end = len(array) - 1

# the index of the target value
result = -1


# THE LOOP
# divide the array in half and check if the middle element
# matches
while start <= end:
  mid = (start + end) // 2
  if array[mid] == target:
    result = mid
    break
  elif array[mid] < target:
    start = mid + 1
  else:
    end = mid - 1

# PRINT RESULTS
if result != -1:
  print("Element found at index: ", result)
else:
  print("Element is not in the array!")



#################################################################
# O NOTATION - Logarithmic Time O(log n)

# Logarithmic time O notation calculates how many times we can 
# divide the problem in half before we reach a single element


# # UNCOMMENT HERE DOWN
# #initialize the iterations count
# iterations = 0

# # get the lenght of the array
# # n = len(array)
# n = 1000

# # Divide by 2 repeatedly until we reach 1
# while n > 1:
#   n = n // 2
#   iterations += 1
#   print("Iterations: ", iterations)


# # PRINT RESULTS
# print("The total iterations are: ", iterations)