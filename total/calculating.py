import pandas as pd

# Define file paths
weekdays_file = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\combined\combined_weekdays.csv"
weekends_file = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\combined\combined_weekends.csv"

# Define output folder
output_folder = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total"

def process_ridership(file_path, output_filename):
    """Processes ridership data by summing Avg Daily Entries per station and selecting the busiest time period."""
    df = pd.read_csv(file_path)

    # Convert 'Avg Daily Entries' to numeric (handles cases where numbers might be misread as strings)
    df["Avg Daily Entries"] = pd.to_numeric(df["Avg Daily Entries"], errors='coerce')

    # Aggregate total ridership per station
    total_ridership = df.groupby("Station Name", as_index=False)["Avg Daily Entries"].sum()

    # Find the time period with the highest ridership for each station
    busiest_time_period = df.loc[df.groupby("Station Name")["Avg Daily Entries"].idxmax(), ["Station Name", "Time Period"]]

    # Merge the results to get total ridership and busiest time period
    final_df = total_ridership.merge(busiest_time_period, on="Station Name")

    # Define output file path
    output_file = f"{output_folder}\\{output_filename}"

    # Save the processed data
    final_df.to_csv(output_file, index=False)
    print(f"Total ridership per station saved to: {output_file}")

# Process both weekday and weekend files
process_ridership(weekdays_file, "total_ridership_weekdays.csv")
process_ridership(weekends_file, "total_ridership_weekends.csv")
