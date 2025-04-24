# Approach:
# - Normalize text (remove punctuation, lowercase everything).
# - Tokenize and filter out stop words.
# - Use a dictionary to maintain frequency.
# - For prefix-based queries, use sorting + filtering based on prefix.

import re
from collections import defaultdict, Counter

# List of common stop words
STOP_WORDS = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'to', 'of', 'for', 'with', 'by', 'as', 'that'}

def preprocess_text(text):
    # Remove punctuation and make lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.lower().split()
    # Filter out stop words
    return [word for word in words if word not in STOP_WORDS]

def analyze_text(text):
    words = preprocess_text(text)
    frequency = Counter(words)
    return frequency

def query_top_k_words_with_prefix(frequency_dict, prefix, k):
    prefix = prefix.lower()
    filtered_words = [(word, freq) for word, freq in frequency_dict.items() if word.startswith(prefix)]
    # Sort by frequency (descending) then alphabetically
    filtered_words.sort(key=lambda x: (-x[1], x[0]))
    return filtered_words[:k]

# Example paragraph
paragraph = "The theory of relativity is one of the most remarkable theories in the history of physics."

# Analyze
freq_dict = analyze_text(paragraph)
print("Word Frequencies:", freq_dict)

# Query
top_words = query_top_k_words_with_prefix(freq_dict, 'th', 3)
print("Top 3 words with prefix 'th':", top_words)
