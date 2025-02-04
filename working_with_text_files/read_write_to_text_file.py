content = """First Text

Second text"""
with open('file1.txt', 'w') as f:
    f.write(content)

with open('file1.txt', 'r') as f:
    read_in_content = f.read()

print(content)