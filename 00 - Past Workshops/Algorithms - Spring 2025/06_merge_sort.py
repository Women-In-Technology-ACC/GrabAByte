# Merge Sort

# A merge sort algorithm splits an array into halves, sorts each 
# half and merges the sorted halves back together

#################################################################


# FUNCTION TO MERGE SORT
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

# SET VARIABLES
# the array to be sorted
array = [38, 27, 43, 3, 9, 82, 10]

# CALL THE FUNCTION
merge_sort(array)

# PRINT RESULTS
print("Sorted array is:", array)


#################################################################
# O NOTATION - Log-Linear Time O(n log n)

# Log-Linear Time o notation represents an algorithm that splits 
# the input and processes each element


# # UNCOMMENT HERE DOWN
# # Initialize the iterations sum variable
# iterations = 0

# # Get the length of the array
# n = len(array)
# log_n = 0

# # Calculate long n (how many times we can halve n before reaching 1)
# while n > 1:
#     n = n // 2
#     log_n += 1

# # Multiple log n by n to get O(n log n)
# iterations = n * log_n

# # PRINT RESULTS
# print("The total iterations are: ", iterations)