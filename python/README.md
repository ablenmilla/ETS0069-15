# STRING METHODS
# str.lower Method
The str.lower method returns a copy of the original string with all uppercase characters converted to lowercase. This method does not alter the original string but returns a new string where all the alphabetic characters are lowercase.


# str.upper Method
The str.upper method returns a copy of the original string with all lowercase characters converted to uppercase. Like lower(), this method does not modify the original string but instead returns a new string with all alphabetic characters in uppercase.


# str.title Method
The str.title method converts the first character of each word in the string to uppercase and the rest of the characters in the word to lowercase. It treats any non-alphabetic character (like spaces or punctuation) as a word boundary.



# str.capitalize
The str.capitalize method returns a copy of the original string where the first character is converted to uppercase and all other characters are converted to lowercase. This method does not modify the original string; instead, it creates a new string with the changes.



# str.swapcase
The str.capitalize() method is used to format text by converting the first character of a string to uppercase while making all other characters lowercase. This is particularly useful for ensuring proper capitalization in sentences, names, and titles. However, if the first character is not a letter, it remains unchanged. Additionally, it does not affect other words in the string, so only the very first letter gets capitalized, making it different from str.title().
 

 # str.swapcase
 The str.swapcase() method transforms a string by reversing the case of each letter, converting uppercase characters to lowercase and vice versa. This method is useful in situations where you need to toggle case formatting, such as handling text-based encryption, debugging case-sensitive inputs, or simply altering text for stylistic purposes. It works on all alphabetic characters but does not change numbers, punctuation, or spaces.


 # str.find
 The str.find() method searches for a specified substring within a string and returns the index of its first occurrence. If the substring is not found, it returns -1, indicating that the search was unsuccessful. Unlike str.index(), which raises an error if the substring is absent, str.find() safely handles missing values. This method also supports optional start and end parameters, allowing users to search within a specific portion of the string. It is commonly used in text processing tasks, such as locating keywords in a document or extracting specific data from a larger text.
