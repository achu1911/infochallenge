import pandas as pd
import os

weekday_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\csv_files\weekdays'
weekend_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\csv_files\weekends'
cleaned_weekdays_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\cleaned_data\cleaned_weekdays'
cleaned_weekends_folder = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\cleaned_data\cleaned_weekends'

# Function to clean and sort CSV files
def clean_and_sort_csv(csv_folder, cleaned_folder):
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

    # Loop through each CSV file in the folder
    for file_name in csv_files:
        file_path = os.path.join(csv_folder, file_name)
        df = pd.read_csv(file_path)
        df['Avg Daily Entries'] = df['Avg Daily Entries'].replace({'K': '', ',': '', ' ': ''}, regex=True).astype(float)
        df_sorted = df.sort_values(by='Station Name')
        
        # Date from file name 
        name_parts = file_name.split('_')
        month_name = name_parts[0]  # The full month name (e.g., December)
        day_year = "_".join(name_parts[1:3])  # The 'DD_YYYY' part
        cleaned_file_name = f"cleaned_{month_name}_{day_year}"
        sorted_file_path = os.path.join(cleaned_folder, cleaned_file_name)
        df_sorted.to_csv(sorted_file_path, index=False)

# Clean and sort files from both weekdays and weekends folders
clean_and_sort_csv(weekday_folder, cleaned_weekdays_folder)
clean_and_sort_csv(weekend_folder, cleaned_weekends_folder)
