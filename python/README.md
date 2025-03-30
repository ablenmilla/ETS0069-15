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




 # str.index
  The str.index() method works similarly to str.find() by searching for a specified substring within a string and returning the index of its first occurrence. However, unlike str.find(), if the substring is not found, str.index() raises a ValueError, making it useful when you need to ensure the substring exists rather than handling missing values silently. It also supports optional start and end parameters to restrict the search within a specific range, making it ideal for text parsing and extraction tasks


# str.startswith

The str.startswith() method checks whether a string begins with a specified prefix and returns True if it does and False otherwise. This method is useful for validating input formats, such as checking if a file name starts with a specific prefix or if a web address begins with "https". It also supports optional start and end parameters, allowing for more precise checks within a portion of the string rather than the entire text.



# str.endswith
The str.endswith() method functions similarly to str.startswith(), but it checks whether a string ends with a specific suffix. It returns True if the string ends with the given substring and False otherwise. This method is commonly used in file handling, such as verifying if a file has a particular extension like .txt or .csv, and also supports optional start and end parameters for more controlled substring matching. 




# str.count
The str.count() method counts the number of times a specified substring appears in a string and returns the count as an integer. This method is useful for analyzing text, such as counting word occurrences in a document or detecting repeated characters. It also accepts optional start and end parameters, allowing for substring counting within a specific range.





# str.replace()
The str.replace() method replaces all occurrences of a specified substring with another substring and returns the modified string. This method is commonly used in text processing tasks, such as correcting typos, formatting data, or filtering unwanted words. It also accepts an optional third argument that limits the number of replacements.




# str.strip()
The str.strip() method removes any leading and trailing whitespace (spaces, tabs, or newline characters) from a string. This is useful for cleaning user input, removing accidental spaces from data, or preparing text for further processing. If a specific set of characters is provided as an argument, str.strip() removes only those characters from both ends of the string





# str.lstrip

The lstrip() method returns a copy of the string with leading whitespace removed. You can also specify a set of characters to remove from the beginning of the string.








# str.rstrip

The rstrip() method returns a copy of the string with trailing whitespace removed. Like lstrip(), you can specify a set of characters to remove from the end of the string.



# str.split

The split() method divides a string into a list of substrings based on a specified separator. If no separator is provided, it splits on any whitespace by default.





# str.join
The str.join() method is used to merge elements of a list or tuple into a single string, placing the specified separator between them


# str.isalpha
The str.isalpha() method checks if all characters in a string are letters. If the string contains numbers, spaces, or symbols, it returns False. 

# str.isdigit
The str.isdigit() method checks if a string contains only numeric digits. If the string includes letters, spaces, or special characters, it returns False

 
# str.isalnum
The isalnum() method checks whether a string consists only of alphabetic letters and digits, without any spaces or special characters. If all characters are alphanumeric, it returns True; otherwise, it returns False. This method is useful for validating user input, such as usernames or passwords that should contain only letters and numbers.



# str.isspace
The isspace() method determines if a string is made up entirely of whitespace characters, such as spaces, tabs, or newlines. If every character in the string is a whitespace character, it returns True; otherwise, it returns False. This method is commonly used to check for empty input or to validate formatting in text processing.






# str.format
The format() method is used for inserting values into a string by replacing placeholders {} with specified arguments. It supports both positional and keyword-based formatting, allowing for dynamic and readable text generation. This method is widely used for displaying messages, formatting reports, and constructing complex strings efficiently.









