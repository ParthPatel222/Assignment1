import json
from collections import Counter
import re

# Read the JSON file containing webpage data
with open('ksu1000.json', 'r') as json_file:
    data = json.loads(json_file.read())

# Initialize variables
total_tokens = 0
email_counter = Counter()
webpages_with_emails = 0

# Process each webpage in the collection
for webpage in data:
    # Tokenize the webpage by splitting on whitespace
    tokens = webpage['body'].strip().split()

    # Calculate the length of the webpage in tokens and add to total
    doc_len = len(tokens)
    total_tokens += doc_len

    email_pattern = r'[\w\.-]+@[\w\.-]+'
    emails = re.findall(email_pattern, webpage['body'])

    # If at least one email is found, increment counter
    if emails:
        webpages_with_emails += 1

    # Update the email_counter with the found emails
    email_counter.update(emails)

# average length of webpages in tokens
average_length = total_tokens / len(data)

# top ten most frequent email addresses
top_emails = email_counter.most_common(10)

# percentage of webpages that contain at least one email address
percentage_with_emails = (webpages_with_emails / len(data)) * 100

print(f"doc_len: {average_length:.3f}")
print("emails:")
for email, count in top_emails:
    print(f"\t('{email}', {count})")
print(f"perc: {percentage_with_emails:.3f}")
