import json
from collections import Counter
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords

# Read the JSON file containing webpage data
with open('ksu1000.json', 'r') as json_file:
    webpages_data = json.loads(json_file.read())

# Initialize a Counter to count word frequencies
word_counter = Counter()

# Process each webpage in the collection
for webpage in webpages_data:
    # Tokenize the webpage content by splitting on whitespace and converting to lowercase
    tokens = re.findall(r'\b\w+\b', webpage['body'].lower())

    # Count word frequencies
    word_counter.update(tokens)

# Get the most common words and their frequencies
common_words = word_counter.most_common(30)

# Extract word frequencies and ranks
word_frequencies = [freq for word, freq in common_words]
ranks = list(range(1, len(common_words) + 1))

# Create a list of datapoints with the x and y coordinates
x = ranks
y = word_frequencies

# Create a scatter plot
plt.figure()
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.scatter(x, y)

# Save the plot as an image
plt.savefig('KSUWordFrequencies.png')

plt.show()
