import pandas as pd

# Regional and state data
virginia_data = (
    ("Alexandria", [
        ("Braddock Road", "Alexandria"),
        ("Eisenhower Ave", "Alexandria"),
        ("King St-Old Town", "Alexandria"),
        ("Potomac Yard", "Alexandria"),
        ("Van Dorn Street", "Alexandria"),
    ], "Virginia"),
    ("Arlington County", [
        ("Arlington Cemetery", "Arlington County"),
        ("Ballston-MU", "Arlington County"),
        ("Clarendon", "Arlington County"),
        ("Court House", "Arlington County"),
        ("Crystal City", "Arlington County"),
        ("East Falls Church", "Arlington County"),
        ("Pentagon", "Arlington County"),
        ("Pentagon City", "Arlington County"),
        ("Ronald Reagan Washington National Airport", "Arlington County"),
        ("Virginia Sq-GMU", "Arlington County"),
        ("Rosslyn", "Arlington County"),
    ], "Virginia"),
    ("Loudoun County", [
        ("Ashburn", "Loudoun County"),
        ("Dulles Airport", "Loudoun County"),
        ("Loudoun Gateway", "Loudoun County"),
    ], "Virginia"),
    ("Fairfax County", [
        ("Dunn Loring", "Fairfax County"),
        ("Franconia-Springfield", "Fairfax County"),
        ("Greensboro", "Fairfax County"),
        ("Herndon", "Fairfax County"),
        ("Huntington", "Fairfax County"),
        ("Innovation Center", "Fairfax County"),
        ("McLean", "Fairfax County"),
        ("Reston Town Center", "Fairfax County"),
        ("Spring Hill", "Fairfax County"),
        ("Tysons", "Fairfax County"),
        ("Vienna", "Fairfax County"),
        ("West Falls Church", "Fairfax County"),
        ("Wiehle-Reston East", "Fairfax County"),
    ], "Virginia"),
)

maryland_data = (
    ("Montgomery County", [
        ("Forest Glen", "Montgomery County"),
        ("Glenmont", "Montgomery County"),
        ("Grosvenor-Strathmore", "Montgomery County"),
        ("Medical Center", "Montgomery County"),
        ("Bethesda", "Montgomery County"),
        ("North Bethesda", "Montgomery County"),
        ("Rockville", "Montgomery County"),
        ("Shady Grove", "Montgomery County"),
        ("Silver Spring", "Montgomery County"),
        ("Twinbrook", "Montgomery County"),
        ("Wheaton", "Montgomery County"),
    ], "Maryland"),
    ("Prince George's County", [
        ("Addison Road", "Prince George's County"),
        ("Capitol Heights", "Prince George's County"),
        ("Cheverly", "Prince George's County"),
        ("College Park-U of Md", "Prince George's County"),
        ("Downtown Largo", "Prince George's County"),
        ("Greenbelt", "Prince George's County"),
        ("Hyattsville Crossing", "Prince George's County"),
        ("Landover", "Prince George's County"),
        ("Morgan Boulevard", "Prince George's County"),
        ("Naylor Road", "Prince George's County"),
        ("New Carrollton", "Prince George's County"),
        ("Southern Ave", "Prince George's County"),
        ("Suitland", "Prince George's County"),
        ("West Hyattsville", "Prince George's County"),
        ("Branch Ave", "Suitland, Maryland")
    ], "Maryland")
)

dc_data = (
    ("Washington, D.C. (northeast)", [
        ("Benning Road", "Washington, D.C. (northeast)"),
        ("Brookland-CUA", "Washington, D.C. (northeast)"),
    ], "D.C."),
    ("Washington, D.C. (northwest)", [
        ("Archives", "Washington, D.C. (northwest)"),
    ], "D.C."),
    ("Washington, D.C. (southeast)", [
        ("Anacostia", "Washington, D.C. (southeast)"),
    ], "D.C."),
    ("District of Columbia", [
        ("Capitol South", "District of Columbia"),
        ("Cleveland Park", "District of Columbia"),
        ("Columbia Heights", "District of Columbia"),
        ("Congress Heights", "District of Columbia"),
        ("Deanwood", "District of Columbia"),
        ("Dupont Circle", "District of Columbia"),
        ("Eastern Market", "District of Columbia"),
        ("Farragut North", "District of Columbia"),
        ("Farragut West", "District of Columbia"),
        ("Federal Center SW", "District of Columbia"),
        ("Federal Triangle", "District of Columbia"),
        ("Foggy Bottom-GWU", "District of Columbia"),
        ("Fort Totten", "District of Columbia"),
        ("Friendship Heights", "District of Columbia"),
        ("Gallery Place", "District of Columbia"),
        ("Georgia Ave-Petworth", "District of Columbia"),
        ("Judiciary Square", "District of Columbia"),
        ("L'Enfant Plaza", "District of Columbia"),
        ("McPherson Sq", "District of Columbia"),
        ("Metro Center", "District of Columbia"),
        ("Minnesota Ave", "District of Columbia"),
        ("Mt Vernon Sq", "District of Columbia"),
        ("Navy Yard-Ballpark", "District of Columbia"),
        ("NoMa-Gallaudet U", "District of Columbia"),
        ("Potomac Ave", "District of Columbia"),
        ("Rhode Island Ave", "District of Columbia"),
        ("Shaw-Howard U", "District of Columbia"),
        ("Smithsonian", "District of Columbia"),
        ("Stadium-Armory", "District of Columbia"),
        ("Takoma", "District of Columbia"),
        ("Tenleytown-AU", "District of Columbia"),
        ("U Street", "District of Columbia"),
        ("Union Station", "District of Columbia"),
        ("Van Ness-UDC", "District of Columbia"),
        ("Waterfront", "District of Columbia"),
        ("Woodley Park", "District of Columbia"),
    ], "D.C."),
)

# Combining into one list
all_data = list(virginia_data) + list(maryland_data) + list(dc_data)

station_region_mapping = {}
station_state_mapping = {}

for region, stations, state in all_data:
    for station_name, _ in stations:
        station_region_mapping[station_name] = region
        station_state_mapping[station_name] = state


def process_ridership(csv_file_path, output_file_path):
    df = pd.read_csv(csv_file_path)

    # Assign regions and states to the stations in the CSV data
    df['Region'] = df['Station Name'].map(station_region_mapping)
    df['State'] = df['Station Name'].map(station_state_mapping)

    # Identifying any rows with missing data
    missing_regions = df[df['Region'].isnull()]
    missing_states = df[df['State'].isnull()]
    
    print(f"Missing regions in {csv_file_path}:")
    print(missing_regions[['Station Name', 'Region']])
    
    print(f"Missing states in {csv_file_path}:")
    print(missing_states[['Station Name', 'State']])

    df.to_csv(output_file_path, index=False)

    # Print the updated DataFrame (for checking)
    print(f"Updated DataFrame saved to {output_file_path}")
    print(df.head())


# Weekday & weekend files 
weekdays_file_path = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership_weekdays.csv"
weekends_file_path = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership_weekends.csv"

weekdays_output_path = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership_weekdays_region_state.csv"
weekends_output_path = r"C:\Users\alexa\OneDrive\Documents\GitHub\infochallenge\total\total_ridership_weekends_region_state.csv"

# Process the weekday data
process_ridership(weekdays_file_path, weekdays_output_path)

# Process the weekend data
process_ridership(weekends_file_path, weekends_output_path)
