# app.py

from flask import Flask, request, render_template
import scrapingsel
import googlescholarapiscrapes  # Import the googlescholarapiscrapes module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    conference = request.form.get('conference')
    keywords = request.form.get('keywords').split(',')

    # Check if the conference is recognized by scrapingsel.py
    if conference in ["CVPR", "IROS", "ICRA"]:
        results = scrapingsel.scrape_papers(conference, keywords)
    else:
        # Call the googlescholarapiscrapes.py module
        results = googlescholarapiscrapes.scrape_google_scholar_from_app(conference, keywords)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

