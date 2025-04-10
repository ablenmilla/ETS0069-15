filename = "document.txt"
print(filename.endswith(".txt"))  # Output: True
print(filename.endswith(".csv"))  # Output: False
print(filename.endswith("ment", 0, 7))  # Output: False (checks only "documen")
