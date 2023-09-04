import json
from collections import Counter
import string
from nltk.corpus import stopwords

with open('ksu1000.json', 'r') as json_file:
    data = json.loads(json_file.read())

word_counter = Counter()

# set of stopwords from NLTK
stop_words = set(stopwords.words('english'))

# translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)

# Process each webpage in the collection
for webpage in data:
    content = webpage['body'].lower()
    content = content.translate(translator)
    tokens = content.split()

    # Remove stopwords and count word frequencies
    filtered_tokens = [token for token in tokens if token not in stop_words]
    word_counter.update(filtered_tokens)

print("Top 30 Words After Removing Stopwords and Punctuation:")
print("rank  term        freq.    perc.")
print("------  --------  -------  -------")

for rank, (term, freq) in enumerate(word_counter.most_common(30), 1):
    percentage = (freq / len(data)) * 100
    print(f"     {rank}  {term:<10}  {freq}    {percentage:.3f}")
