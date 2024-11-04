from collections import Counter
import re

text = "This test string is only for test. This test is only for test."
# Simple word tokenizer
words = re.findall(r'\w+', text.lower())
word_counts = Counter(words)
print(word_counts)
# Output: Counter({'test': 3, 'this': 2, 'is': 2, 'a': 2, 'only': 1})

print("\n---------------------------------------------------\n")

from collections import Counter

numbers_list = [14, 54, 68, 54, 79, 45, 68, 14]
item_counter = Counter(numbers_list)
duplicates = [number for number, count in item_counter.items() if count > 1]
print(duplicates)
# Duplicate numbers - [14, 54, 68]

print("\n---------------------------------------------------\n")
from collections import Counter

def check_anagrams(str_1, str_2):
    return Counter(str_1.replace(" ", "").lower()) == Counter(str_2.replace(" ", "").lower())

print(check_anagrams("listen", "silent"))  # Output: True
print(check_anagrams("Hello", "World"))    # Output: False

print("\n---------------------------------------------------\n")
from collections import Counter
import matplotlib.pyplot as plt

numbers_list = [14, 54, 68, 54, 34, 23, 79, 45, 68, 14, 54, 14, 54]
numbers_counter = Counter(numbers_list)

plt.bar(numbers_counter.keys(), numbers_counter.values())
plt.xlabel('Numbers')
plt.ylabel('Count')
plt.title('Numbers Histogram')
plt.show()

