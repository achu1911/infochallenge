import pandas as pd
import os

weekdays_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\cleaned_data\cleaned_weekdays'
weekends_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\cleaned_data\cleaned_weekends'
combined_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\cleaned_data\combined'

combined_weekdays_folder = os.path.join(combined_folder, 'combined_weekdays')
combined_weekends_folder = os.path.join(combined_folder, 'combined_weekends')

# Paths for the combined files 
combined_weekdays_path = os.path.join(combined_weekdays_folder, 'combined_weekdays.csv')
combined_weekends_path = os.path.join(combined_weekends_folder, 'combined_weekends.csv')

# Function to combine CSV files from a folder
def combine_csv_files(folder_path, combined_file_path):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # List to hold DF 
    dfs = []

    for file_name in csv_files:
        file_path = os.path.join(folder_path, file_name)

        df = pd.read_csv(file_path)
        dfs.append(df)

    # Combine all DataFrames into one
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv(combined_file_path, index=False)

    print(f"Combined CSV saved to: {combined_file_path}")

# Saving in weekdays 
combine_csv_files(weekdays_folder, combined_weekdays_path)

# Saving in weekends
combine_csv_files(weekends_folder, combined_weekends_path)
