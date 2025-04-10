# dictionary methods

# clear
The clear() method removes all items from a dictionary, leaving it empty. It doesn't delete the dictionary itself, just erases all key-value pairs inside it.

# copy
The copy() method creates a shallow copy of the dictionary, meaning changes to the copied dictionary won’t affect the original (unless it contains nested objects like lists or other dictionaries).

# fromkeys
The fromkeys() method creates a new dictionary using a given sequence of keys, assigning the same specified value to each key in the new dictionary.




# get
The get() method is used to safely access the value of a specified key in a dictionary. If the key exists, it returns the corresponding value; if the key is missing, it returns None by default instead of causing an error like using square brackets would. You can also provide a custom default value to return when the key is not found, which makes your code safer and more flexible.


# items
The items() method returns a view object that contains all key-value pairs in the dictionary as tuples. This is especially useful when looping through a dictionary using a for loop, as it allows you to access both the key and the value at the same time. It can also be converted to a list if needed for other operations.


# keys
The keys() method returns a view object that contains all the keys in the dictionary. This is useful for checking what keys are present or looping through just the keys. Although it looks like a list, it is a special view object that reflects changes in the dictionary.