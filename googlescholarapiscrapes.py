import csv
import os.path
from scholarly import scholarly
from nltk import sent_tokenize, word_tokenize
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
import heapq

# CSV file name
csv_file = 'gscholar.csv'

def summarize_text(text, num_sentences=2):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Calculate word frequency
    freq_dist = FreqDist(words)

    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in freq_dist.items():
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq
                else:
                    sentence_scores[sentence] = freq

    # Get the summary by selecting the top sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = TreebankWordDetokenizer().detokenize(summary_sentences)

    return summary

def write_to_csv(data):
    # Check if CSV file exists
    file_exists = os.path.isfile(csv_file)

    # Open CSV file in append mode
    with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Document Title', 'Authors', 'Publication Year', 'PDF Link', 'Implementation?', 'Abstract Summary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if the file is newly created
        if not file_exists:
            writer.writeheader()

        # Check for duplicates before writing
        if not is_duplicate(data):
            writer.writerow(data)

def is_duplicate(data):
    # Check if the document title already exists in the CSV file
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Document Title'] == data['Document Title']:
                return True

    return False

# Your code to retrieve and process Google Scholar results
# Replace the following comments with your actual code

def retrieve_google_scholar_data(keywords, conferences, num_results=10, summary_sentences=2):
    # Your code to fetch Google Scholar results using keywords and conferences
    # For example, using the scholarly library

    # Iterate through the results and process each paper
    for result in scholarly.search_pubs(' '.join(keywords)):
        # Extract relevant information from the result
        document_title = result.bib['title']
        authors = ', '.join(result.bib['author'])
        publication_year = result.bib.get('year', '')
        pdf_link = result.bib.get('url', '')
        # Add more fields as needed

        # Check if the paper meets your criteria (e.g., conference)
        if 'conference' in result.bib:
            conference = result.bib['conference']
            if conference.lower() in conferences:
                # Retrieve the abstract
                abstract = result.bib.get('abstract', '')
                
                # Summarize the abstract
                summarized_abstract = summarize_text(abstract, num_sentences=summary_sentences)

                # Create a dictionary with the data
                result_data = {
                    'Document Title': document_title,
                    'Authors': authors,
                    'Publication Year': publication_year,
                    'PDF Link': pdf_link,
                    'Implementation?': '',  # Add your implementation check logic
                    'Abstract Summary': summarized_abstract
                }

                # Write the data to CSV
                write_to_csv(result_data)

# Example usage:
keywords = ['multi-agent', 'social navigation', 'dynamic environments', 'crowds']
conferences = ['IROS', 'AAAI', 'ICRA']
retrieve_google_scholar_data(keywords, conferences, num_results=10, summary_sentences=2)

