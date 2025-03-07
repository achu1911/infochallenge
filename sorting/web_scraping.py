import requests
from bs4 import BeautifulSoup
import pandas as pd
import shutil

# Got some tips/tricks from link: https://realpython.com/beautiful-soup-web-scraper-python/ 
# Sending request to webpage 
url = 'https://en.wikipedia.org/wiki/List_of_Washington_Metro_stations#cite_note-stationlist-7'  
response = requests.get(url)

# Parse the page using BeautifulSoup
# BeautifulSoup is used for pasring HTML content and extracting data from the webpage. 
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with class 'wikitable sortable'
table = soup.find('table', {'class': 'wikitable sortable'})

# Extract station names and their jurisdcitions 
station_to_jurisdiction = []

# Loop through each row in the table 
for row in table.find_all('tr')[1:]:
    # Get all the columns (td)
    columns = row.find_all('td')
    
    if len(columns) > 3: 
        station_name = columns[0].get_text(strip=True)  # Station name is in the first column
        jurisdiction_name = columns[3].get_text(strip=True)  # Jurisdiction is in the fourth column

        # adding the station & jurisdiction to list 
        station_to_jurisdiction.append({'Station Name': station_name, 'Jurisdiction': jurisdiction_name})

# converting 
stations_df = pd.DataFrame(station_to_jurisdiction)

# saving a file 
csv_file_path = 'stations_with_jurisdictions.csv'
stations_df.to_csv(csv_file_path, index=False)

#Moving csv file 
destination_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\sorting'
shutil.move(csv_file_path, destination_folder)

print(stations_df.head())
