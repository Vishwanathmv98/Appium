# f = open('C:\\12\\myfile.txt', 'w')
# f.write("This is the first line\n")
# f.write("This is secound line")
# f.close()

# f = open('C:\\12\\myfile.txt', 'r')
# print(f.readlines())
# f.close()

# f = open('C:\\12\\myfile.txt', 'a')
# f.write("\nThis is the third line\n")
# f.write("This is fourth line")
# f.close()

# f = open('C:\\12\\myfile.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# Specify the file path
file_path = 'C:\\12\\myfile.txt'
old_word = "This"
new_word = "in"

# Open the file in read mode
f = open(file_path, 'r')
content = f.read()  # Read the entire content of the file
f.close()  # Close the file after reading

# Replace the word
modified_content = content.replace(old_word, new_word)

# Open the file in write mode to overwrite the existing content
f = open(file_path, 'w')
f.write(modified_content)  # Write the modified content back to the file
f.close()  # Close the file after writing

import re

# Open the file in read mode
f = open('C:\\12\\myfile.txt', 'r')
content = f.read()  # Read the entire content of the file
f.close()  # Close the file after reading

# Replace the word case-insensitively
modified_content = re.sub(re.escape(old_word), new_word, content, flags=re.IGNORECASE)  # replace old word and new word

# Write the modified content back to the file
f = open('C:\\12\\myfile.txt', 'w')
f.write(modified_content)  # Write the modified content back to the file
f.close()  # Close the file after writing
