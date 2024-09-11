import re

filepath="C:\\12\\myfile.txt"
oldword="This"
newword="That"
with open(filepath, 'r') as f:
    content=f.read()
    modified_str = re.sub(oldword, newword, content, flags=re.IGNORECASE)
    with open(filepath, 'w') as f:
        f.write(modified_str)
        f.close()
