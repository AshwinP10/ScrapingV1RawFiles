from flask import Flask, request, jsonify, render_template
import scrapingsel  # This is your scraping module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # You will create this HTML file for input

@app.route('/scrape', methods=['POST'])
def scrape():
 # Retrieve form data
    conference = request.form['conference']
    keywords = request.form['keywords'].split(',')
    sort_preference = request.form['sort']

    # Call the scraping function with the sort preference
    results = scrapingsel.scrape_papers(conference, keywords, sort_preference)

    # Render your template with results
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True) 