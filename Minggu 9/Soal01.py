def is_anagram(a, b):
    return sorted(re.sub(r'\W+', '', a.lower())) == sorted(re.sub(r'\W+', '', b.lower()))

import re

print(is_anagram('mata','atma'))
print(is_anagram('mata', 'tama'))
print(is_anagram('mata', 'makan'))