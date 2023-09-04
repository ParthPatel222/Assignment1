import json
import re
from collections import Counter
import matplotlib.pyplot as plt

with open('ksu1000.json', 'r') as json_file:
    webpages_data = json.loads(json_file.read())

word_counter = Counter()

for webpage in webpages_data:
    # Tokenize the webpage  by splitting on whitespace and converting to lowercase
    tokens = re.findall(r'\b\w+\b', webpage['body'].lower())

    # Count word frequencies
    word_counter.update(tokens)

# most common words and their frequencies
common_words = word_counter.most_common(30)

word_frequencies = [freq for word, freq in common_words]
ranks = list(range(1, len(common_words) + 1))

x = ranks  # x coordinate
y = word_frequencies  # y coordinate

# Create scatter plot
plt.figure()
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.scatter(x, y)

plt.savefig('KSUWordFrequencies.png')

plt.show()
