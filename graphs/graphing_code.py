import pandas as pd
import matplotlib.pyplot as plt

# Function to plot horizontal bar chart and save the plot
def plot_top_stations(input_file_path, title, save_path):
    # Read the CSV file
    df = pd.read_csv(input_file_path)

    #Order data by avg daily entries in ascending order 
    df = df.sort_values(by='Avg Daily Entries', ascending=True)
    
    plt.figure(figsize=(10, 6))
    
    # Plot the horizontal bar chart
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        
        # Create a bar chart for each region
        plt.barh(region_data['Station Name'], region_data['Avg Daily Entries'], label=region)
    
    # Set labels and title
    plt.xlabel('Average Daily Entries')
    plt.ylabel('Station Name')
    plt.title(f'Top 3 Stations by Region: {title}')
    
    # Display the legend
    plt.legend(title="Regions")
    
    # Save the plot to the specified path
    plt.tight_layout()  # Ensure that the labels and legend do not overlap
    plt.savefig(save_path, transparent = True) # Save as transparent
    plt.close()  # Close the plot after saving

    print(f"Chart saved to: {save_path}")

# Step 1: Plot and save the chart for weekdays data
csv_file_path_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\top_stations\top_stations_weekdays.csv"
save_path_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\graphs\top_stations_weekdays.png"
plot_top_stations(csv_file_path_weekdays, "Weekdays", save_path_weekdays)

# Step 2: Plot and save the chart for weekends data
csv_file_path_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\top_stations\top_stations_weekends.csv"
save_path_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\graphs\top_stations_weekends.png"
plot_top_stations(csv_file_path_weekends, "Weekends", save_path_weekends)
