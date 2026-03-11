import os
from datetime import datetime

locations = [
    {"city": "Antlers", "state": "OK", "region": "Pushmataha County"},
    {"city": "Ashdown", "state": "AR", "region": "Little River County"},
    {"city": "Athens", "state": "TX", "region": "Henderson County"},
    {"city": "Atlanta", "state": "TX", "region": "Cass County"},
    {"city": "Avinger", "state": "TX", "region": "Cass County"},
    {"city": "Big Sandy", "state": "TX", "region": "Upshur County"},
    {"city": "Bonham", "state": "TX", "region": "Fannin County"},
    {"city": "Bossier City", "state": "LA", "region": "Bossier Parish"},
    {"city": "Broken Bow", "state": "OK", "region": "McCurtain County"},
    {"city": "Canton", "state": "TX", "region": "Van Zandt County"},
    {"city": "Carthage", "state": "TX", "region": "Panola County"},
    {"city": "Cason", "state": "TX", "region": "Morris County"},
    {"city": "Center", "state": "TX", "region": "Shelby County"},
    {"city": "Clarksville", "state": "TX", "region": "Red River County"},
    {"city": "Commerce", "state": "TX", "region": "Hunt County"},
    {"city": "Cooper", "state": "TX", "region": "Delta County"},
    {"city": "Daingerfield", "state": "TX", "region": "Morris County"},
    {"city": "De Queen", "state": "AR", "region": "Sevier County"},
    {"city": "Denison", "state": "TX", "region": "Grayson County"},
    {"city": "Diana", "state": "TX", "region": "Upshur County"},
    {"city": "Durant", "state": "OK", "region": "Bryan County"},
    {"city": "Forney", "state": "TX", "region": "Kaufman County"},
    {"city": "Gainesville", "state": "TX", "region": "Cooke County"},
    {"city": "Gilmer", "state": "TX", "region": "Upshur County"},
    {"city": "Gladewater", "state": "TX", "region": "Gregg County"},
    {"city": "Grand Saline", "state": "TX", "region": "Van Zandt County"},
    {"city": "Greenville", "state": "TX", "region": "Hunt County"},
    {"city": "Hallsville", "state": "TX", "region": "Harrison County"},
    {"city": "Haughton", "state": "LA", "region": "Bossier Parish"},
    {"city": "Hawkins", "state": "TX", "region": "Wood County"},
    {"city": "Henderson", "state": "TX", "region": "Rusk County"},
    {"city": "Homer", "state": "LA", "region": "Claiborne Parish"},
    {"city": "Hope", "state": "AR", "region": "Hempstead County"},
    {"city": "Hughes Springs", "state": "TX", "region": "Cass County"},
    {"city": "Hugo", "state": "OK", "region": "Choctaw County"},
    {"city": "Idabel", "state": "OK", "region": "McCurtain County"},
    {"city": "Jefferson", "state": "TX", "region": "Marion County"},
    {"city": "Kilgore", "state": "TX", "region": "Gregg County"},
    {"city": "Leesburg", "state": "TX", "region": "Camp County"},
    {"city": "Lindale", "state": "TX", "region": "Smith County"},
    {"city": "Linden", "state": "TX", "region": "Cass County"},
    {"city": "Lone Star", "state": "TX", "region": "Morris County"},
    {"city": "Longview", "state": "TX", "region": "Gregg County"},
    {"city": "Magnolia", "state": "AR", "region": "Columbia County"},
    {"city": "Mansfield", "state": "LA", "region": "De Soto Parish"},
    {"city": "Marshall", "state": "TX", "region": "Harrison County"},
    {"city": "Minden", "state": "LA", "region": "Webster Parish"},
    {"city": "Mineola", "state": "TX", "region": "Wood County"},
    {"city": "Mount Pleasant", "state": "TX", "region": "Titus County"},
    {"city": "Mount Vernon", "state": "TX", "region": "Franklin County"},
    {"city": "Nacogdoches", "state": "TX", "region": "Nacogdoches County"},
    {"city": "Naples", "state": "TX", "region": "Morris County"},
    {"city": "Nashville", "state": "AR", "region": "Howard County"},
    {"city": "Omaha", "state": "TX", "region": "Morris County"},
    {"city": "Ore City", "state": "TX", "region": "Upshur County"},
    {"city": "Palestine", "state": "TX", "region": "Anderson County"},
    {"city": "Paris", "state": "TX", "region": "Lamar County"},
    {"city": "Pittsburg", "state": "TX", "region": "Camp County"},
    {"city": "Pottsboro", "state": "TX", "region": "Grayson County"},
    {"city": "Prescott", "state": "AR", "region": "Nevada County"},
    {"city": "Queen City", "state": "TX", "region": "Cass County"},
    {"city": "Quitman", "state": "TX", "region": "Wood County"},
    {"city": "Rockwall", "state": "TX", "region": "Rockwall County"},
    {"city": "Royse City", "state": "TX", "region": "Rockwall County"},
    {"city": "Sherman", "state": "TX", "region": "Grayson County"},
    {"city": "Shreveport", "state": "LA", "region": "Caddo Parish"},
    {"city": "Springhill", "state": "LA", "region": "Webster Parish"},
    {"city": "Sulphur Bluff", "state": "TX", "region": "Hopkins County"},
    {"city": "Sulphur Springs", "state": "TX", "region": "Hopkins County"},
    {"city": "Talco", "state": "TX", "region": "Titus County"},
    {"city": "Terrell", "state": "TX", "region": "Kaufman County"},
    {"city": "Texarkana", "state": "TX", "region": "Bowie County"},
    {"city": "Tyler", "state": "TX", "region": "Smith County"},
    {"city": "Valliant", "state": "OK", "region": "McCurtain County"},
    {"city": "Van", "state": "TX", "region": "Van Zandt County"},
    {"city": "Vivian", "state": "LA", "region": "Caddo Parish"},
    {"city": "White Oak", "state": "TX", "region": "Gregg County"},
    {"city": "Whitesboro", "state": "TX", "region": "Grayson County"},
    {"city": "Wills Point", "state": "TX", "region": "Van Zandt County"},
    {"city": "Winfield", "state": "TX", "region": "Titus County"},
    {"city": "Winnsboro", "state": "TX", "region": "Wood County"}
]

try:
    with open('tech-template.html', 'r', encoding='utf-8') as file:
        template = file.read()
except FileNotFoundError:
    print("Error: Could not find 'tech-template.html'.")
    exit()

new_urls = []

for loc in locations:
    city = loc["city"]
    state = loc["state"]
    region = loc["region"]
    
    url_city = city.lower().replace(" ", "-")
    url_state = state.lower()
    
    filename = f"starlink-installation-{url_city}-{url_state}.html"
    new_urls.append(f"https://deanshandymanservice.me/{filename}")
    
    page_content = template.replace("{{CITY}}", city)
    page_content = page_content.replace("{{STATE}}", state)
    page_content = page_content.replace("{{REGION}}", region)
    page_content = page_content.replace("{{URL_CITY}}", url_city)
    page_content = page_content.replace("{{URL_STATE}}", url_state)
    
    with open(filename, 'w', encoding='utf-8') as new_file:
        new_file.write(page_content)

# Update sitemap
try:
    if os.path.exists('sitemap.xml'):
        with open('sitemap.xml', 'r', encoding='utf-8') as f:
            sitemap_content = f.read()
    else:
        # Create a basic sitemap structure if it doesn't exist
        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>'
        
    if "</urlset>" in sitemap_content:
        urls_to_add = ""
        for url in new_urls:
            if url not in sitemap_content:
                urls_to_add += f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{datetime.today().strftime('%Y-%m-%d')}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
        
        sitemap_content = sitemap_content.replace("</urlset>", urls_to_add + "</urlset>")
        
        with open('sitemap.xml', 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
    print("Process complete. Pages generated and sitemap updated.")
except Exception as e:
    print(f"Sitemap error: {e}")
