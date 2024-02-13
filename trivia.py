import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def read_movie_ids_and_titles_from_csv(file_path):
    movies = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            movies.append((row['id'], row['title']))  # Assuming there's a 'title' column in your CSV
    return movies


def fetch_trivia(movies):
    options = Options()
    options.headless = True  # Run in headless mode

    # Set up the web driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # List to hold trivia for each movie
    movies_trivia = []

    # Base URL for IMDb trivia pages
    base_trivia_url = "https://www.imdb.com/title/{}/trivia/"

    for movie_id, movie_title in movies:
        # Form the full trivia URL for the movie
        trivia_url = base_trivia_url.format(movie_id)

        # Navigate to the trivia page
        driver.get(trivia_url)

        # Wait for the dynamic content to load
        time.sleep(5)

        # Try to click the 'All' button to load all trivia items
        try:
            # Use the class name of the 'All' button to identify and click it
            all_button = driver.find_element(By.CLASS_NAME,"ipc-see-more__button")
            all_button.click()

            # Wait for the content to load after the click
            time.sleep(5)
        except Exception as e:
            print(f"Could not click 'All' button for {movie_id}. Exception: {e}")

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all trivia items - Update the selector if needed after inspecting the page
        trivia_elements = soup.find_all('div', class_='ipc-html-content-inner-div')
        
        # Extract the trivia text from each element
        trivia_items = [trivia_elem.get_text(strip=True) for trivia_elem in trivia_elements]
        
        # Each trivia item for a movie is a new row in the CSV
        for trivia in trivia_items:
            movies_trivia.append((movie_id, movie_title, trivia))

    # Close the browser when done
    driver.quit()

    return movies_trivia


if __name__ == "__main__":
    # Update the file path to the location of your output/movies.csv
    file_path = 'output/movies.csv'
    movies = read_movie_ids_and_titles_from_csv(file_path)
    
    # Get the trivia for each movie
    trivia = fetch_trivia(movies)

    # Write the trivia to a CSV file
    with open('output/trivia.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Movie ID', 'Movie Title', 'Trivia'])
        for trivia_row in trivia:
            writer.writerow(trivia_row)
    print("Trivia has been written to output/trivia.csv")