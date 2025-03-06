import pandas as pd 
import matplotlib.pyplot as plt
import os

folder_path = r'C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\csv_files\weekdays'
weekdays_files = ['December_04_2024.csv', 'June_05_2024.csv', 'March_06_2024.csv', 'September_04_2024.csv']

# Create a figure for the plot
plt.figure(figsize=(10, 6))

# Loop through each CSV file
for csv in weekdays_files:
    file_path = os.path.join(folder_path, csv)

    # Read the CSV file
    data = pd.read_csv(file_path)

    # Print the columns to debug
    print(f"Columns in {csv}: {data.columns}")

    # Check if 'Avg Daily Entries' exists in the columns
    if 'Avg Daily Entries' in data.columns:
        # Clean 'Avg Daily Entries' column (remove 'K' and convert to float)
        data['Avg Daily Entries'] = data['Avg Daily Entries'].replace({'K': ''}, regex=True).astype(float) * 1000

        # Extract the date from the filename (e.g., 'December_04_2024')
        date_str = os.path.splitext(csv)[0]  # Remove the '.csv' extension
        # Plot the bar chart, using the filename as the x-axis label
        plt.bar(date_str, data['Avg Daily Entries'].mean(), label=csv)  # Plot the average for each file
    else:
        print(f"Column 'Avg Daily Entries' not found in {csv}. Skipping this file.")

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Average Daily Entries (Thousands)')
plt.title('Avg Daily Entries from Multiple Weekday CSV Files')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend to distinguish the CSVs
plt.legend()

# Show the plot
plt.show()
