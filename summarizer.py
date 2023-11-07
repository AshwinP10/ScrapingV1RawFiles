from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Sample input text to be summarized
input_text = """
This is a sample input text that you want to summarize. It contains multiple sentences.
You can use this code to perform extractive summarization without Gensim.
The approach used here ranks sentences based on word frequency.
"""

# Tokenize the input text into sentences
sentences = sent_tokenize(input_text)

# Tokenize the input text into words
words = word_tokenize(input_text)

# Calculate word frequency using Counter
word_frequencies = Counter(words)

# Rank sentences based on word frequency
sentence_scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence):
        if word in word_frequencies:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]

# Get the number of sentences you want in the summary (e.g., 2 sentences)
num_sentences_in_summary = 2

# Select the top sentences with the highest scores to create the summary
summary_sentences = [sentence for sentence, score in sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences_in_summary]]

# Combine the selected sentences to create the summary
summary = ' '.join(summary_sentences)

# Print the summary
print("Summary:")
print(summary)