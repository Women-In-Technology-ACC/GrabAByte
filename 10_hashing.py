# Hashing

# A hashing algorithm is a technique to map data to a fixed-size 
# table (hash table) for fast data retrieval using a hash function.

#################################################################


# FUNCTION TO HASH VALUES
def hash_function(key, size):
    return hash(key) % size

# SET VARIABLES
# the size of the hash table and the key to hash
table_size = 10
key = "Hello"

# CALL THE FUNCTION
hashed_value = hash_function(key, table_size)

# PRINT RESULTS
print(f"The hashed value for '{key}' is:", hashed_value)


#################################################################
# O NOTATION - Constant Time O(1)

# Constant Time O notation represents an algorithm that takes the
# same amount of time not matter how large the input is


# # UNCOMMENT HERE DOWN
# # Initialize iterations sum variable
# iterations = 1       # ALWAYS 1 OPERATION

# # PRINT RESULTS
# print("The total iterations are: ", iterations)