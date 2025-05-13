# Selection Sort

# Selection Sort divides the array into sorted and unsorted parts,
# then repeatedly selects the smallest element from the unsorted part
# and moves it to the sorted part.

#################################################################

# SET VARIABLES
# the array to be sorted
array = [64, 25, 12, 22, 11]

# THE LOOP
# find the smallest element and place it at the beginning
for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

# PRINT RESULTS
print("Sorted array is:", array)