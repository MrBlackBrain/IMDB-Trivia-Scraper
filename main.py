from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import csv  # Import the csv module
import os

# Create the 'output' directory if it does not exist
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

options = Options()
options.headless = True  # Run in headless mode

# Set up the web driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define the URL of the IMDb fan favorites page
url = "https://www.imdb.com/what-to-watch/fan-favorites/"

# Navigate to the page
print("Navigating to URL...")
driver.get(url)
print("URL navigated.")

# Wait for the dynamic content to load
time.sleep(10)  # Adjust the sleep time as necessary

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Example selector to get the movie titles - Update this selector based on actual page content
movie_elements = soup.find_all('a', class_='ipc-poster-card__title')

# Extract the names and IDs of the movies
movies_info = []
for movie_element in movie_elements[:10]:  # Limit the results to top 10 movies
    movie_title = movie_element.get_text(strip=True)
    movie_link = movie_element['href']
    movie_id = movie_link.split('/')[2]
    movies_info.append({'title': movie_title, 'id': movie_id})

# Print or process the list of movies
for movie in movies_info:
    print(f"Movie Title: {movie['title']}, Movie ID: {movie['id']}")

# Close the browser when done
driver.quit()

# Now write the movies information to a CSV file
with open(os.path.join(output_dir, 'movies.csv'), 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'id']  # Define the column names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header row
    for movie in movies_info:
        writer.writerow(movie)  # Write movie data

# Confirm the CSV has been written
print("Movies have been written to `output/movies.csv`")