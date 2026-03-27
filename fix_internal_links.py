import os
import glob

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

# Find all HTML files in the main directory
html_files = glob.glob("*.html")

links_updated = 0
files_modified = set()

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    original_content = content
    
    for city_data in cities:
        city = city_data["name"]
        state = city_data["state"]

        safe_city = city.lower().replace(" ", "-")
        safe_state = state.lower()

        # The exact strings we are looking for
        old_link_relative = f"handyman-{safe_city}-{safe_state}.html"
        new_link_relative = f"service-areas/handyman-services-{safe_city}-{safe_state}.html"
        
        old_link_absolute = f"https://deanshandymanservice.me/{old_link_relative}"
        new_link_absolute = f"https://deanshandymanservice.me/{new_link_relative}"

        # 1. Replace relative links (e.g., href="handyman-bossier-city-la.html")
        # We make sure we don't accidentally edit the redirect files themselves
        if old_link_relative in content and filepath != old_link_relative:
            content = content.replace(f'"{old_link_relative}"', f'"{new_link_relative}"')
            content = content.replace(f"'{old_link_relative}'", f"'{new_link_relative}'")
            links_updated += 1
            
        # 2. Replace absolute links (e.g., href="https://deanshandymanservice.me/...")
        if old_link_absolute in content and filepath != old_link_relative:
            content = content.replace(old_link_absolute, new_link_absolute)
            links_updated += 1
            
    # If we made changes, save the file
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        files_modified.add(filepath)

print(f"✅ Found and updated {links_updated} outdated links across {len(files_modified)} files!")
if files_modified:
    print(f"📝 Modified files: {', '.join(files_modified)}")
