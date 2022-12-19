# In this assignment, you will recreate Python dictionaries from scratch using data structure called hash table.
# Dictionaries in Python are used to store key-value pairs.
# Keys are used to store and retrieve values. For example, here's a dictionary for storing and retrieving phone numbers using people's names.
# phone_numbers = {
#   'Aakash' : '9489484949',
#   'Hemanth' : '9595949494',
#   'Siddhant' : '9231325312'
# }
# phone_numbers
# Your objective in this assignment is to implement a HashTable class which supports the following operations:
#
# Insert: Insert a new key-value pair
# Find: Find the value associated with a key
# Update: Update the value associated with a key
# List: List all the keys stored in the hash table
MAX_HASH_TABLE_SIZE = 4096


class HashTable:

    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        index = get_index(self.data_list, key)
        self.data_list[index] = (key,value)

    def find(self, key):
        """Find the value associated with a key"""
        index = get_index(self.data_list, key)
        keyvalue = self.data_list[index]
        if keyvalue is None:
            return None
        else:
            key, value = keyvalue
        return value

    def update(self, key, value):
        """Change the value associated with a key"""
        idx = get_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key,value)

    def list_all(self):
        """List all the keys"""
        pairs = [kv[0] for kv in self.data_list if kv is not None]
        return pairs


def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0

    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number
        # Take the remainder of the result with the size of the data list

    list_index = result % len(data_list)
    return list_index


# As you can see above, the value for the key listen was overwritten by the value for the key silent.
# Our hash table implementation is incomplete because it does not handle collisions correctly.
#
# To handle collisions we'll use a technique called linear probing.
# Here's how it works:
# While inserting a new key-value pair if the target index for a key is occupied by another key,
# then we try the next index, followed by the next and so on till we the closest empty location.
#
# While finding a key-value pair, we apply the same strategy, but instead of searching for an empty location,
# we look for a location which contains a key-value pair with the matching key.
#
# While updating a key-value pair, we apply the same strategy, but instead of searching for an empty location,
# we look for a location which contains a key-value pair with the matching key, and update its value.
#
# We'll define a function called get_valid_index, which starts searching the data list from the index determined
# by the hashing function get_index and returns the first index which is either empty or contains a key-value pair matching the given key.

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

# List of size MAX_HASH_TABLE_SIZE with all values None


