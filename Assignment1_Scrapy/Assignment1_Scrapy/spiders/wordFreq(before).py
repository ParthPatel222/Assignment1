import json
from collections import Counter
import re

with open('ksu1000.json', 'r') as json_file:
    data = json.loads(json_file.read())

word_counter = Counter()

for webpage in data:
    tokens = re.findall(r'\b\w+\b', webpage['body'].lower())

    word_counter.update(tokens)

print("Top 30 Words Before Removing Stopwords:")
print("rank  term        freq.    perc.")
print("------  --------  -------  -------")
for rank, (term, freq) in enumerate(word_counter.most_common(30), 1):
    percentage = (freq / len(data)) * 100
    print(f"     {rank}  {term:<10}  {freq}    {percentage:.3f}")
