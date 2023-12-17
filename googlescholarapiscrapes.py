# googlescholarapiscrapes.py

from serpapi import GoogleSearch

def extract_info_from_results(results):
    extracted_data = []

    # Check if 'organic_results' key is present in the response
    if 'organic_results' in results:
        for result in results['organic_results']:
            publication_info = result.get('publication_info', {})
            authors = publication_info.get('authors', [])

            # Join author names into a single string
            authors_str = ', '.join([author['name'] for author in authors])

            # Extract publication year from the summary
            summary = publication_info.get('summary', '')
            summary_parts = [part for part in summary.split(' ') if part.isdigit()]
            publication_year = min([int(part) for part in summary_parts]) if summary_parts else None

            # Retrieve abstract directly from the result if available
            abstract = result.get('snippet', '')

            # Replace newline characters with HTML line breaks
            abstract = abstract.replace('\n', '<br>')

            item = {
                'Document Title': result.get('title', ''),
                'Authors': authors_str,
                'Publication Year': publication_year,
                'Link': result.get('link', ''),
                'Abstract': f"Abstract Keywords: " + abstract,
            }
            extracted_data.append(item)
    else:
        print("Error: 'organic_results' not found in the response.")
        print("Response:", results)

    return extracted_data

def scrape_google_scholar(conference, keywords):
    serpapi_api_key = "YOUR_SERPAPI_KEY"  # Replace with your actual SerpAPI key

    search_query = f'{", ".join(keywords)} : {conference}'  # Include the conference name in the query
    params = {
        'engine': 'google_scholar',
        'q': search_query,
        'hl': 'en',
        'num': '5',
        'as_ylo': '2018',
        'similar': True,
        'api_key': serpapi_api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    formatted_data = extract_info_from_results(results)
    return formatted_data

def scrape_google_scholar_from_app(conference, keywords):
    # Modified function to be called from the app
    serpapi_api_key = "711a48b7d71a612832076d19c921023795916f9669da361ef7e016d6f021f8f3"  # Replace with your actual SerpAPI key

    search_query = f'{", ".join(keywords)} : {conference}'  # Include the conference name in the query
    params = {
        'engine': 'google_scholar',
        'q': search_query,
        'hl': 'en',
        'num': '5',
        'as_ylo': '2018',
        'similar': True,
        'api_key': serpapi_api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    formatted_data = extract_info_from_results(results)
    return formatted_data
