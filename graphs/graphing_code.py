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
        
        
        plt.barh(region_data['Station Name'], region_data['Avg Daily Entries'], label=region)
    
    plt.xlabel('Average Daily Entries')
    plt.ylabel('Station Name')
    plt.title(f'Top 3 Stations by Region: {title}')
    
    # legend
    plt.legend(title="Regions")
    plt.tight_layout()  
    plt.savefig(save_path, transparent = True) 
    plt.close() 

    print(f"Chart saved to: {save_path}")


csv_file_path_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\top_stations\top_stations_weekdays.csv"
save_path_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\graphs\top_stations_weekdays.png"
plot_top_stations(csv_file_path_weekdays, "Weekdays", save_path_weekdays)


csv_file_path_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\top_stations\top_stations_weekends.csv"
save_path_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\graphs\top_stations_weekends.png"
plot_top_stations(csv_file_path_weekends, "Weekends", save_path_weekends)
