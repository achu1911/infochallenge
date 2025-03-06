import pandas as pd
import os
from jurisdiction_tuples import get_county  # Import the helper function from tuples.py


print("Current working directory:", os.getcwd())
# Define file paths
folder_path = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\csv_files\weekdays'
input_file = 'December_04_2024.csv'
input_file_path = os.path.join(folder_path, input_file)

# Load the CSV file
df = pd.read_csv(input_file_path)

# Ensure the CSV has a 'Station Name' column
if 'Station Name' not in df.columns:
    raise ValueError(f"'Station Name' column not found in {input_file}")

# Create a new column 'County' by applying the get_county function to each station name
df['County'] = df['Station Name'].apply(get_county)

# Optionally, sort the DataFrame by 'County' and then by 'Station Name'
df_sorted = df.sort_values(by=['County', 'Station Name'])

# Define output file path for the new CSV file
output_file = 'grouped_by_county_December_04_2024.csv'
output_file_path = os.path.join(folder_path, output_file)

# Write the sorted DataFrame to the new CSV file
df_sorted.to_csv(output_file_path, index=False)
print(f"New CSV file with stations grouped by county saved to: {output_file_path}")
