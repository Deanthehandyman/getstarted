import os

# Your exact city list
cities = [
    {"name": "Pittsburg", "state": "TX"}, {"name": "Tyler", "state": "TX"}, {"name": "Longview", "state": "TX"}, 
    {"name": "Texarkana", "state": "TX"}, {"name": "Texarkana", "state": "AR"}, {"name": "Shreveport", "state": "LA"}, 
    {"name": "Broken Bow", "state": "OK"}, {"name": "Mount Pleasant", "state": "TX"}, {"name": "Gilmer", "state": "TX"}, 
    {"name": "Daingerfield", "state": "TX"}, {"name": "Ore City", "state": "TX"}, {"name": "Hughes Springs", "state": "TX"}, 
    {"name": "Avinger", "state": "TX"}, {"name": "Naples", "state": "TX"}, {"name": "Omaha", "state": "TX"}, 
    {"name": "Big Sandy", "state": "TX"}, {"name": "Hawkins", "state": "TX"}, {"name": "Winfield", "state": "TX"}, 
    {"name": "Leesburg", "state": "TX"}, {"name": "Cason", "state": "TX"}, {"name": "Sulphur Springs", "state": "TX"}, 
    {"name": "Mineola", "state": "TX"}, {"name": "Lindale", "state": "TX"}, {"name": "Gladewater", "state": "TX"}, 
    {"name": "White Oak", "state": "TX"}, {"name": "Kilgore", "state": "TX"}, {"name": "Marshall", "state": "TX"}, 
    {"name": "Henderson", "state": "TX"}, {"name": "Carthage", "state": "TX"}, {"name": "Center", "state": "TX"}, 
    {"name": "Nacogdoches", "state": "TX"}, {"name": "Palestine", "state": "TX"}, {"name": "Athens", "state": "TX"}, 
    {"name": "Canton", "state": "TX"}, {"name": "Van", "state": "TX"}, {"name": "Grand Saline", "state": "TX"}, 
    {"name": "Wills Point", "state": "TX"}, {"name": "Terrell", "state": "TX"}, {"name": "Forney", "state": "TX"}, 
    {"name": "Rockwall", "state": "TX"}, {"name": "Royse City", "state": "TX"}, {"name": "Greenville", "state": "TX"}, 
    {"name": "Commerce", "state": "TX"}, {"name": "Sulphur Bluff", "state": "TX"}, {"name": "Cooper", "state": "TX"}, 
    {"name": "Bonham", "state": "TX"}, {"name": "Paris", "state": "TX"}, {"name": "Hugo", "state": "OK"}, 
    {"name": "Idabel", "state": "OK"}, {"name": "Valliant", "state": "OK"}, {"name": "Antlers", "state": "OK"}, 
    {"name": "Durant", "state": "OK"}, {"name": "Sherman", "state": "TX"}, {"name": "Denison", "state": "TX"}, 
    {"name": "Pottsboro", "state": "TX"}, {"name": "Whitesboro", "state": "TX"}, {"name": "Gainesville", "state": "TX"}, 
    {"name": "Minden", "state": "LA"}, {"name": "Bossier City", "state": "LA"}, {"name": "Haughton", "state": "LA"}, 
    {"name": "Vivian", "state": "LA"}, {"name": "Springhill", "state": "LA"}, {"name": "Homer", "state": "LA"}, 
    {"name": "Mansfield", "state": "LA"}, {"name": "Ashdown", "state": "AR"}, {"name": "De Queen", "state": "AR"}, 
    {"name": "Nashville", "state": "AR"}, {"name": "Hope", "state": "AR"}, {"name": "Prescott", "state": "AR"}, 
    {"name": "Magnolia", "state": "AR"}, {"name": "Clarksville", "state": "TX"}, {"name": "Lone Star", "state": "TX"}, 
    {"name": "Atlanta", "state": "TX"}, {"name": "Linden", "state": "TX"}
]

BASE_URL = "https://deanshandymanservice.me"
NEW_FOLDER = "service-areas"

redirects_created = 0

for city_data in cities:
    city = city_data["name"]
    state = city_data["state"]

    safe_city = city.lower().replace(" ", "-")
    safe_state = state.lower()

    # The OLD filename (causing the 404s right now)
    old_filename = f"handyman-{safe_city}-{safe_state}.html"
    
    # The NEW filename and URL (where we want to send people)
    new_filename = f"handyman-services-{safe_city}-{safe_state}.html"
    new_url = f"{BASE_URL}/{NEW_FOLDER}/{new_filename}"

    # The HTML code that performs the redirect
    redirect_html = f"""<!DOCTYPE html>
<html>
  <head>
    <link rel="canonical" href="{new_url}" />
    <meta http-equiv="refresh" content="0; url='{new_url}'" />
    <title>Page Moved</title>
  </head>
  <body>
    <p>This page has moved. <a href="{new_url}">Click here</a> to go to the new {city} page.</p>
  </body>
</html>
"""

    # This creates (or overwrites) the old file in your root directory
    with open(old_filename, "w", encoding="utf-8") as f:
        f.write(redirect_html)

    redirects_created += 1

print(f"✅ Successfully generated {redirects_created} redirect pages to fix the 404s!")
