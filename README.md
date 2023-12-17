# Research Paper Scraper

## Overview

This project provides a web-based tool for scraping research papers from academic conferences. It supports two scraping methods: one using Selenium for specific conferences (CVPR, IROS, ICRA) and the other using the SerpAPI library for a more generic Google Scholar search.

## Features

- **Web Scraping Methods:**
  - **Selenium Scraping:** Customized scraping for specific conferences.
  - **Google Scholar API Scraping:** Generic search using SerpAPI for more flexibility.

- **Abstract Summarization:**
  - Utilizes natural language processing to summarize abstracts for easier understanding.

- **Web Interface:**
  - Provides a user-friendly web interface using Flask.

## How to Use

1. Clone the repository:

   git clone https://github.com/..........

2. Install everything - could require some different versions than what I have listed in the requirements.txt file

You can add or modify versions based on your preferences or requirements. To create this file, you can run the following command in your terminal:

pip freeze > requirements.txt

This command will generate a requirements.txt file with the current versions of the installed packages in your Python environment. 
You can then review and modify it as needed.

pip install -r requirements.txt

3. Run the Flask web application: python app.py

4. Access the web interface in your browser at http://127.0.0.1:5000/. This will be running on a WSGI webserver

5. Enter the conference and keywords, then click "Scrape Papers."

6. Future Considerations: Improve Website Layout, Allow for more customization/variety of results.

This webapp was developed by Ashwin Prakash as an introductory project for the UT Austin Autonomous Mobile Robots Laboratory.