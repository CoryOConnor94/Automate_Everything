import re
from pathlib import Path

# Extract email addresses
# text = ' Hi there here is an email address to extract exa_mple@example.com and here is another anotherexample@ex_ample.com'
#
# email_pattern = re.compile('[^ ]+@[a-z]+.[a-z]+')
# matches = email_pattern.findall(text)
# print(matches)


# Extract URLs from file
# with open('urls.txt', 'r') as file:
#     urls = file.read()
#
# print(urls)
#
# url_pattern = re.compile('https?://(?:www.)?[^ \n]+\.[a-z]+')
# matches = url_pattern.findall(urls)
# print(matches)



# Extract IP addresses
# with open('ips.txt', 'r') as file:
#     ips = file.read()
#
# print(ips)
#
# ip_pattern = re.compile('[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}')
# matches = ip_pattern.findall(ips)
# print(matches)



# Filter filenames and extract only files from november 12th to november 20th
# root_dir = Path('files')
# file_names = root_dir.iterdir()
# file_name_strings = [file_name.name for file_name in file_names]
# # print(file_name_strings)
#
# filename_pattern = re.compile('nov[a-z]*-(?:[1-9]|1[0-9]|20).txt', re.IGNORECASE)
# matches = [filename for filename in file_name_strings if filename_pattern.findall(filename)]
# print(matches)


# Find all list items that contain the word Delhi

data=[
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com",
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants"
]
#
# pattern = re.compile('.*Delhi.*', re.IGNORECASE)
# matches = [match for match in data if pattern.findall(match)]
# print(matches)



# Find all lines containing word Delhi and email address

# pattern = re.compile('.*Delhi.*.@')
# matches = [match for match in data if pattern.findall(match)]
# print(matches)



# Find all lines containing delhi and phone number

# pattern = re.compile('.*Delhi.*[0]+[0-9]{4,10}')
# matches = [match for match in data if pattern.findall(match)]
# print(matches)


# Find all lines that contain the word delhi and have a phone number or an email address
data=[
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com",
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants"
]

pattern = re.compile('.*Delhi.*([0|+][0-9]{4,10}|.@)')
matches = [match for match in data if pattern.findall(match)]
print(matches)


# .        Matches any single character
# \        Escapes one of the meta characters to treat it as a regular character
# [...]    Matches a single character or a range that is contained within brackets. Order does not matter but without brackets order does matter
# +        Matches the preeceding element one or more times
# ?        Matches the preeceding element zero or one time
# *        Matches the preeceding element zero or more times
# {m,n}    Matches the preeceding element at least m and not more than n times
# ^        Matches the beginning of a line or string
# $        Matches the end of a line or string
# [^...]   Matches a single character or a range that is not contained within the brackets
# ?:...|..."Or" operator
# ()       Matches an optional expression