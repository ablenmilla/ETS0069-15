# set method
1. add() Method

The add() method is used to add a single element to a set. If the element already exists in the set, it won't be added again because sets do not allow duplicates.



# clear() Method

The clear() method removes all elements from a set, leaving it empty. It does not delete the set itself, just clears its contents.

# copy() Method

The copy() method creates a shallow copy of a set. This means it makes a new set with the same elements, but it's a separate object in memory. Changing one will not affect the other.



# difference
The difference() method returns a new set containing elements that are only in the first set and not in the other(s). It does not modify the original set.

# difference_update
The difference_update() method removes the elements found in another set from the original set. It updates the original set directly and returns None.

 # discard

The discard() method removes a specific element from the set if it exists. If the element is not present, it does nothing (no error is raised).



# intersection
Description:
The intersection() method returns a new set with elements that are common to both sets. It does not modify the original sets.




# intersection_update
Description:
The intersection_update() method modifies the original set by keeping only elements that are common with another set. It doesn't return anything.


# isdisjoint
Description:
The isdisjoint() method checks whether two sets have no elements in common. It returns True if they are completely separate, and False if they share any item.

# issubset
The issubset() method checks whether all the elements of the current set are present in another set. It returns True if every item in the first set also exists in the second set. This is useful when you want to confirm if one set is completely contained within another. A set is always a subset of itself.

# issuperset
The issuperset() method is the opposite of issubset(). It checks if the current set contains all the elements of another set. If the current set has every item that the other set has (and possibly more), it returns True. Just like with subsets, a set is always a superset of itself.

# pop
The pop() method removes and returns a random element from the set. Since sets do not maintain order, you cannot choose or predict which item will be removed. If the set is empty, calling pop() will cause an error. This method is useful when you want to gradually empty a set by removing elements one at a time.


# remove
The remove() method is used to delete a specific element from a set. If the element is not present, it raises a KeyError.


#  symmetric_difference

The symmetric_difference() method returns a new set with elements that are in either of the sets, but not in both. It does not change the original sets.

#  symmetric_difference_update

The symmetric_difference_update() method updates the original set with the symmetric difference — that means it keeps only the elements unique to each set and removes the common ones.