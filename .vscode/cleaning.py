import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\csv_files\weekdays\December_04_2024.csv')

# Extract station names, remove duplicates by converting to a set, and sort alphabetically
station_names = sorted(list(set(df['Station Name'].tolist())))

# Print the number of unique station names
print(f'Total unique stations: {len(station_names)}')

# Print the station names vertically (unique and sorted)
for station in station_names:
    print(station)

# A total of 98 stations 


# Defining regional mapping
region_map = {

}

# Clean and prepare your data as shown previously
df['Avg Daily Entries'] = df['Avg Daily Entries'].replace({'K': '', ',': '', ' ': ''}, regex=True).astype(float)

