import pandas as pd
import matplotlib.pyplot as plt

# Mapping each region to a state
region_to_state = {
    # Virginia
    "Alexandria": "Virginia",
    "Arlington County": "Virginia",
    "Loudoun County": "Virginia",
    "Fairfax County": "Virginia",
    
    # Maryland
    "Montgomery County": "Maryland",
    "Prince George's County": "Maryland",
    "Suitland, Maryland": "Maryland",

    # Washington, D.C.
    "Washington, D.C. (northeast)": "D.C.",
    "Washington, D.C. (northwest)": "D.C.",
    "Washington, D.C. (southeast)": "D.C.",
    "District of Columbia": "D.C."
}

# Function to plot pie chart of total ridership by state
def plot_ridership_pie_chart(input_file_path, save_path):
    # Read the CSV file
    df = pd.read_csv(input_file_path)

    # Map each region to its corresponding state
    df['State'] = df['Region'].map(region_to_state)

    # Ensure that the mapping is correct, and show any rows where the state is missing
    missing_states = df[df['State'].isnull()]
    if not missing_states.empty:
        print("The following regions are missing a state mapping:")
        print(missing_states[['Station Name', 'Region']])

    # Group by state and sum the avg daily entries
    state_ridership = df.groupby('State')['Avg Daily Entries'].sum()

    # Define colors for each state
    state_colors = {
    "D.C.": "#AEC6CF",  # Pastel Blue
    "Maryland": "#FFB3A7",  # Pastel Orange
    "Virginia": "#77DD77"  # Pastel Green
    }

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        state_ridership, 
        labels=state_ridership.index, 
        autopct='%1.1f%%', 
        colors=[state_colors[state] for state in state_ridership.index], 
        startangle=140, 
        wedgeprops={'edgecolor': 'black'}
    )

    # Format text for better readability
    for text in texts + autotexts:
        text.set_fontsize(12)
        text.set_weight("bold")

    # Set title based on file name (weekdays or weekends)
    title = "Percentage of Total Avg Ridership by State (Weekdays)" if "weekdays" in input_file_path else "Percentage of Total Avg Ridership by State (Weekends)"
    plt.title(title, fontsize=14, weight="bold")

    # Save the plot
    plt.savefig(save_path, transparent=True)
    plt.close()  # Close the plot after saving

    print(f"Pie chart saved to: {save_path}")


# File paths for the weekdays and weekends datasets
csv_file_path_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership\total_ridership_regions\total_ridership_region_state\total_ridership_weekdays_region_state.csv"
csv_file_path_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership\total_ridership_regions\total_ridership_region_state\total_ridership_weekends_region_state.csv"

# File paths for saving the pie charts
save_path_pie_chart_weekdays = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\graphs\ridership_pie_chart_weekdays.png"
save_path_pie_chart_weekends = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\graphs\ridership_pie_chart_weekends.png"

# Generate the pie charts
plot_ridership_pie_chart(csv_file_path_weekdays, save_path_pie_chart_weekdays)
plot_ridership_pie_chart(csv_file_path_weekends, save_path_pie_chart_weekends)
