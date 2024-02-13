# IMDB Trivia Scraper

This Python project scrapes movie titles and IDs from IMDb's fan favorites page and then retrieves trivia for each movie using Selenium and BeautifulSoup. It saves the movie information to a CSV file.

## Prerequisites

- Python 3.x
- Selenium
- BeautifulSoup
- Chrome WebDriver
  - _Download the Chrome WebDriver from [here](https://chromedriver.chromium.org/downloads) and add it to your system's PATH._

## Installation

1. Clone the repo and navigate into the IMDB Trivia Scraper folder.

   ```bash
   $ git clone https://github.com/MrBlackBrain/IMDB-Trivia-Scraper.git
   $ cd IMDB-Trivia-Scraper/
   ```

2. Create and activate a virtual environment.

   ```bash
   $ python -m venv venv
   $ source venv/bin/activate
   or PS> venv\Scripts\activate
   ```

3. Install all dependencies.

   ```bash
   (venv) $ pip install -r requirements.txt
   ```

## Usage

1. Run `main.py` to scrape movie titles and IDs from IMDb's fan favorites page and save them to `output/movies.csv`.
2. Run `trivia.py` to fetch trivia for each movie from IMDb and save them to `output/trivia.csv`.

Note: if you are having trouble run the script using VsCode debugger

## Project Structure

- `main.py`: Scrapes movie titles and IDs.
- `trivia.py`: Fetches trivia for each movie.
- `output/movies.csv`: Contains movie titles and IDs.
- `output/trivia.csv`: Contains movie trivia.

## Note

- Adjust the sleep times in the scripts as necessary to ensure proper loading of web pages.
- Update the selectors in the scripts if IMDb's page structure changes.
