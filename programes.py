# reverse the words in the sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reverse_words = words[::-1]
    reversed_sen = ' '.join(reverse_words)
    return reversed_sen


print(reverse_sentence("my name is vishwanath"))
# o/p -->> vishwanath is name my
# ---------------------------------------------------------------------------------------------------

# reverse the sentence
sentence = "vishwanath is name my"
reversed_sentence = sentence[::-1]
print(reversed_sentence)


#o/p --> ym eman si htanawhsiv
# -------------------------------------------------------------------------------------------------------


# charecter count
def char_count(s):
    return len(s)


count = char_count("Hello world from ChatGPT")
print(count)
#o/p --> 25
# --------------------------------------------------------------------------------------------------------

# word count -- u can use this for chare count in sentence by commenting c - execute

import re
from collections import Counter


def word_count(a):
    b = re.sub(r'[^a-zA-Z0-9\s]', '', a).lower()
    c = b.split()
    d = Counter(c)
    return d


s = "Hello"
counts = word_count(s)
print(counts)

# O/P -- Counter({'o': 10, ' ': 10, 'e': 8, 'l': 7, 'r': 5, 'h': 4, 'w': 3, 'n': 3, 'm': 3, 't': 3, 'd': 2, 'y': 2, 'p': 2, 'g': 2, 'v': 1, 'c': 1, 'f': 1, 'a': 1, 'i': 1})

# -------------------------------------------------------------------------------------------------
# index of each character
# Sample string
string = "hello"
char_index = {}
for index, char in enumerate(string):
    print(f'{index} = {char}')
# o/p H=0
#     I=1
# --------------------------------------------------------------------------------------------------
# word position
sentence = "it is my name"
word = "name"
words = sentence.split()
found = False
for index, c_word in enumerate(words):
    if c_word == word:
        print(f'the word {c_word} is at position {index}')
        found = True
        break
if not found:
    print("word not found")
# ------------------------------------------------------------------------------------------------------
# Index of required character
si = "hellow"
index_of_o = si.index("o")
print("Index of character o:", index_of_o)


# o/p -->>   Index of character o: 4
# -------------------------------------------------------------------------------------------------------
# duplicate charecter count
def duplicate_char(s):
    seen_char = set()
    duplicate_char = set()
    for char in s:
        if char in seen_char:
            duplicate_char.add(char)
        else:
            seen_char.add(char)
    return len(duplicate_char)


print(duplicate_char("aakjkjdjsdjjj"))


# o/p-->> 4
# ------------------------------------------------------------------------------------------------------------
# duplicate words count

def duplicate_words(s):
    words = s.split()
    seen_words = set()
    duplicate_words = set()
    for word in words:
        if word in seen_words:
            duplicate_words.add(word)
        else:
            seen_words.add(word)
    return len(duplicate_words)


print("No of duplicate words are : ", duplicate_words("this this is to to"))


# o/p -->> No of duplicate words are :  2

# duplicate words no and count
def duplicate_words(s):
    words = s.split()
    seen_words = set()
    duplicate_words = set()
    word_count = {}

    for word in words:
        if word in seen_words:
            duplicate_words.add(word)
            word_count[word] = word_count.get(word, 0) + 1
        else:
            seen_words.add(word)
            word_count[word] = 1
    duplicate_count = {word: count for word, count in word_count.items() if word in duplicate_words}
    # duplicate_count = {word: count for word, count in word_count.items() if word in duplicate_words}

    return duplicate_count


print(duplicate_words("is is the the"))


# {'is': 2, 'the': 2}

# duplicate chareter and count
def duplicate_words(s):
    words = list(s)
    seen_words = set()
    duplicate_words = set()
    word_count = {}

    for word in words:
        if word == ' ':  # it will not count spaces
            continue
        if word in seen_words:
            duplicate_words.add(word)
            word_count[word] = word_count.get(word, 0) + 1
        else:
            seen_words.add(word)
            word_count[word] = 1
    duplicate_count = {word: count for word, count in word_count.items() if word in duplicate_words}
    # duplicate_count = {word: count for word, count in word_count.items() if word in duplicate_words}

    return duplicate_count


print(duplicate_words("is is the the"))

# Palindrome or not
import re


def palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]


phrase = "A man, a plan, a canal, Panama!"
if palindrome(phrase):
    print(f'"{phrase}" is a palindrome')
else:
    print(f'"{phrase}" is not a palindrome')


# Factorial of number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = 10
result = factorial(num)
print(f'Factorial of {num} is {result}')


# o/p -->> Factorial of 10 is 3628800

# largest num
def largest_num(num):
    largest = num[0]
    for no in num:
        if no > largest:
            largest = no
    return largest


num = [1, 2, 3, 4, 5]
print(largest_num(num))


# using set
def largest_num(num):
    num_set = set(num)  # Convert list to set to remove duplicates
    largest = max(num_set)  # Use built-in max() function to find the largest number
    return largest


num = [1, 2, 3, 4, 5]
print(largest_num(num))


# Write a Python program to count the frequency of each element
def frequency(number):
    frequency = {}
    for num in number:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(frequency(num))

# O/p -->> {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

#Convert caps to small and small to caps
# using swapcase()
String = "Vishwanath V"
swapped_string = string.swapcase(string)
print(swapped_string)

# Using if else
string = "Vishwanath V"
swapped_string = ""

for char in string:
    if char.islower():
        swapped_string += char.upper()
    elif char.isupper():
        swapped_string += char.lower()
    else:
        swapped_string += char  # Keeps non-alphabetic characters as they are

print(swapped_string)

# O/P -->> vISHwANATH v

# Using append

string = "Vishwanath V"
swapped_string_list = []

for char in string:
    if char.islower():
        swapped_string_list.append(char.upper())
    elif char.isupper():
        swapped_string_list.append(char.lower())
    else:
        swapped_string_list.append(char)

swapped_string = ''.join(swapped_string_list)
print(swapped_string)

# 1st letter of the sentence
string = "my name is vishwa"
swapped_string_list = ""
in_word = False
for char in string:
    if char.isalpha():
        if not in_word:
            swapped_string_list += char.upper()
            in_word = True
        else:
            swapped_string_list += char
    else:
        swapped_string_list += char
        in_word = False  # if this flag removed then My name is vishwa
print(swapped_string_list)

# O/P -->> My Name Is Vishwa

#conert to aplha for 1st letter

string = "my name is vishwa"
swapped_string = ""

if string:  # Check if the string is not empty
    if string[0].isalpha():  # Check if the first character is alphabetic
        swapped_string = string[0].upper() + string[1:]
    else:
        swapped_string = string  # If the first character is not alphabetic, keep the string unchanged
else:
    swapped_string = string  # If the string is empty, just return it as is

print(swapped_string)


# sort the number
def sort_in_place(numbers):
    numbers.sort()
    return numbers


numbers = [5, 2, 9, 1, 5, 6]
print(sort_in_place(numbers))

# O/P -->> [1, 2, 5, 5, 6, 9]
