import pandas as pd
import os
from jurisdiction_data import virginia_data, maryland_data, dc_data  # Import data from the separate file


os.chdir(r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\csv_files\sorting')


# Combine all the regional data into one list for easy lookup
all_data = list(virginia_data) + list(maryland_data) + list(dc_data)

def normalize_station_name(station_name):
    """
    Normalize the station name by:
    - Removing extra spaces.
    - Replacing 'Avenue' with 'Ave'.
    - Standardizing hyphens to a single dash.
    """
    # Remove extra spaces, replace 'Avenue' with 'Ave', and standardize hyphens
    return station_name.strip().replace(" Avenue", " Ave").replace("–", "-").replace("-", "-").lower()

def get_county(station_name):
    """
    Given a station name, returns the county/district it belongs to.
    If not found, returns 'Unknown'.
    """
    station_name_clean = normalize_station_name(station_name)  # Normalize input station name

    for county, stations in all_data:
        for station, _ in stations:  # Unpack only the station name
            station_clean = normalize_station_name(station)  # Normalize stored station names

            if station_name_clean == station_clean:
                return county  # Return the matched county

    return "Unknown"  # Return "Unknown" if no match is found


# Define file paths
folder_path = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\csv_files\weekdays'
input_file = 'December_04_2024.csv'
input_file_path = os.path.join(folder_path, input_file)

# Load the CSV file
df = pd.read_csv(input_file_path)

# Fill in the 'Jurisdiction' column based on the 'Station Name' values
df['Jurisdiction'] = df['Station Name'].apply(get_county)

# Sort the DataFrame by 'Station Name' alphabetically
df_sorted = df.sort_values(by='Station Name', ascending=True)

# Save the updated and sorted CSV file
output_file = 'December_04_2024_sorted.csv'
output_file_path = os.path.join(folder_path, output_file)
df_sorted.to_csv(output_file_path, index=False)

print(f"Updated and sorted CSV file saved at: {output_file_path}")

# Check if data is correctly sorted and assigned
print(df_sorted.head())


