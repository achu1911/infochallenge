import pandas as pd

# Function to calculate the top 3 stations for each region
def calculate_top_3_stations(input_file_path, output_file_path):
    # Read the CSV file
    df = pd.read_csv(input_file_path)
    
    # Group by Region and sort stations by 'Avg Daily Entries' in descending order
    sorted_stations_by_region = df.groupby('Region').apply(
        lambda x: x.sort_values('Avg Daily Entries', ascending=False)
    ).reset_index(drop=True)
    
    # Select the top 3 stations for each region
    top_3_stations = sorted_stations_by_region.groupby('Region').head(3)
    
    # Save the result to the specified CSV file
    top_3_stations.to_csv(output_file_path, index=False)
    print(f"Top 3 stations for each region saved to: {output_file_path}")

# Step 1: Calculate the top 3 stations for weekdays
csv_file_path_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership_weekdays_region.csv"
output_file_path_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\top_stations\top_stations_weekdays.csv"
calculate_top_3_stations(csv_file_path_weekdays, output_file_path_weekdays)

# Step 2: Calculate the top 3 stations for weekends
csv_file_path_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership_weekends_region.csv"
output_file_path_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\top_stations\top_stations_weekends.csv"
calculate_top_3_stations(csv_file_path_weekends, output_file_path_weekends)
