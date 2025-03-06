import pandas as pd
import os

# Define the regional data with nested tuples for each county
virginia_data = (
    # Alexandria County
    ("Alexandria", [
        ("Braddock Road", "Alexandria"),
        ("Eisenhower Ave", "Alexandria"),
        ("King St-Old Town", "Alexandria"),
        ("Potomac Yard", "Alexandria"),
        ("Van Dorn Street", "Alexandria"),
    ]),
    
    # Arlington County
    ("Arlington County", [
        ("Arlington Cemetery", "Arlington County"),
        ("Ballston–MU", "Arlington County"),
        ("Clarendon", "Arlington County"),
        ("Court House", "Arlington County"),
        ("Crystal City", "Arlington County"),
        ("East Falls Church", "Arlington County"),
        ("Pentagon", "Arlington County"),
        ("Pentagon City", "Arlington County"),
        ("Ronald Reagan Washington National Airport", "Arlington County"),
        ("Virginia Sq-GMU", "Arlington County"),
        ("Rosslyn", "Arlington County"),
    ]),

    # Loudoun County
    ("Loudoun County", [
        ("Ashburn", "Loudoun County"),
        ("Dulles International Airport", "Loudoun County"),
        ("Loudoun Gateway", "Loudoun County"),
    ]),

    # Fairfax County
    ("Fairfax County", [
        ("Dunn Loring", "Fairfax County"),
        ("Franconia–Springfield", "Fairfax County"),
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
        ("Wiehle–Reston East", "Fairfax County"),
    ]),
)

maryland_data = (
    # Montgomery County
    ("Montgomery County", [
        ("Forest Glen", "Montgomery County"),
        ("Glenmont", "Montgomery County"),
        ("Grosvenor–Strathmore", "Montgomery County"),
        ("Medical Center", "Montgomery County"),
        ("Bethesda", "Montgomery County"),
        ("North Bethesda", "Montgomery County"),
        ("Rockville", "Montgomery County"),
        ("Shady Grove", "Montgomery County"),
        ("Silver Spring", "Montgomery County"),
        ("Twinbrook", "Montgomery County"),
        ("Wheaton", "Montgomery County"),
    ]),

    # Prince George's County
    ("Prince George's County", [
        ("Capitol Heights", "Prince George's County"),
        ("Cheverly", "Prince George's County"),
        ("College Park–University of Maryland", "Prince George's County"),
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
    ])
)

dc_data = (
    # Washington, D.C. (Northeast)
    ("Washington, D.C. (northeast)", [
        ("Benning Road", "Washington, D.C. (northeast)"),
        ("Brookland–CUA", "Washington, D.C. (northeast)"),
    ]),

    # Washington, D.C. (Northwest)
    ("Washington, D.C. (northwest)", [
        ("Archives", "Washington, D.C. (northwest)"),
    ]),

    # Washington, D.C. (Southeast)
    ("Washington, D.C. (southeast)", [
        ("Anacostia", "Washington, D.C. (southeast)"),
    ]),

    # District of Columbia (General)
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
        ("Foggy Bottom–GWU", "District of Columbia"),
        ("Fort Totten", "District of Columbia"),
        ("Friendship Heights", "District of Columbia"),
        ("Gallery Place", "District of Columbia"),
        ("Georgia Avenue–Petworth", "District of Columbia"),
        ("Judiciary Square", "District of Columbia"),
        ("L'Enfant Plaza", "District of Columbia"),
        ("McPherson Sq", "District of Columbia"),
        ("Metro Center", "District of Columbia"),
        ("Minnesota Avenue", "District of Columbia"),
        ("Mt Vernon Sq", "District of Columbia"),
        ("Navy Yard–Ballpark", "District of Columbia"),
        ("NoMa–Gallaudet U", "District of Columbia"),
        ("Potomac Ave", "District of Columbia"),
        ("Rhode Island Ave", "District of Columbia"),
        ("Shaw-Howard U", "District of Columbia"),
        ("Smithsonian", "District of Columbia"),
        ("Stadium–Armory", "District of Columbia"),
        ("Takoma", "District of Columbia"),
        ("Tenleytown–AU", "District of Columbia"),
        ("U Street", "District of Columbia"),
        ("Union Station", "District of Columbia"),
        ("Van Ness–UDC", "District of Columbia"),
        ("Waterfront", "District of Columbia"),
        ("Woodley Park", "District of Columbia"),
    ])
)

# Combine all nested tuples into one list for looping
all_data = list(virginia_data) + list(maryland_data) + list(dc_data)
