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






# pop
The pop() method removes the specified key from a dictionary and returns its value. If the key is not found, it raises a KeyError unless a default value is provided.


# popitem
The popitem() method removes and returns the last inserted key-value pair from the dictionary. It's often used when you want to process and remove items one by one from the end.




#  setdefault
The setdefault() method returns the value of a key if it exists; if not, it adds the key with a default value you specify and then returns that value.



 # update

The update() method is used to update the contents of a dictionary with key-value pairs from another dictionary or an iterable of key-value pairs (like a list of tuples). If a key already exists, its value will be updated. If the key doesn’t exist, it will be added.


# values

The values() method returns a view object that displays a list of all the values in the dictionary. This is useful when you just want to work with the values and ignore the keys.