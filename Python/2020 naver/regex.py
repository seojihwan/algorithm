import re
new_id = 'Abcde123'
n = new_id.lower()
n = ''.join(re.findall("[a-z]|[0-9]|-|_|[.]", n))
print(n)
