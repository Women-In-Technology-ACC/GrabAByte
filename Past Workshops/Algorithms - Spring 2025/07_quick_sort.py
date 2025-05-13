# Quick Sort

# A quick sort algorithm selects a pivot element and partitions the
# array into elements less than and greater than the pivot element
# and recursively sorts the partitions

#################################################################

# FUNCTION TO QUICK SORT
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# SET VARIABLES
# the array to be sorted
array = [10, 7, 8, 9, 1, 5]

# CALL THE FUNCTION
sorted_array = quick_sort(array)

# PRINT RESULTS
print("Sorted array is:", sorted_array)