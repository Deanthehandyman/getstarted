import os
import random
from datetime import datetime

# Configuration
BASE_URL = "https://deanshandymanservice.me"
OUTPUT_DIR = "service-areas"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

locations = [
    {"city": "Antlers", "state": "OK", "region": "Pushmataha County"},
    {"city": "Ashdown", "state": "AR", "region": "Little River County"},
    {"city": "Athens", "state": "TX", "region": "Henderson County"},
    {"city": "Atlanta", "state": "TX", "region": "Cass County"},
    {"city": "Bossier City", "state": "LA", "region": "Bossier Parish"},
    {"city": "Broken Bow", "state": "OK", "region": "McCurtain County"},
    {"city": "Canton", "state": "TX", "region": "Van Zandt County"},
    {"city": "Carthage", "state": "TX", "region": "Panola County"},
    {"city": "Center", "state": "TX", "region": "Shelby County"},
    {"city": "Commerce", "state": "TX", "region": "Hunt County"},
    {"city": "De Queen", "state": "AR", "region": "Sevier County"},
    {"city": "Denison", "state": "TX", "region": "Grayson County"},
    {"city": "Durant", "state": "OK", "region": "Bryan County"},
    {"city": "Gilmer", "state": "TX", "region": "Upshur County"},
    {"city": "Henderson", "state": "TX", "region": "Rusk County"},
    {"city": "Hope", "state": "AR", "region": "Hempstead County"},
    {"city": "Idabel", "state": "OK", "region": "McCurtain County"},
    {"city": "Kilgore", "state": "TX", "region": "Gregg County"},
    {"city": "Longview", "state": "TX", "region": "Gregg County"},
    {"city": "Magnolia", "state": "AR", "region": "Columbia County"},
    {"city": "Marshall", "state": "TX", "region": "Harrison County"},
    {"city": "Minden", "state": "LA", "region": "Webster Parish"},
    {"city": "Mount Pleasant", "state": "TX", "region": "Titus County"},
    {"city": "Nacogdoches", "state": "TX", "region": "Nacogdoches County"},
    {"city": "Palestine", "state": "TX", "region": "Anderson County"},
    {"city": "Paris", "state": "TX", "region": "Lamar County"},
    {"city": "Pittsburg", "state": "TX", "region": "Camp County"},
    {"city": "Shreveport", "state": "LA", "region": "Caddo Parish"},
    {"city": "Sulphur Springs", "state": "TX", "region": "Hopkins County"},
    {"city": "Texarkana", "state": "TX", "region": "Bowie County"},
    {"city": "Tyler", "state": "TX", "region": "Smith County"}
    # Note: Shortened list for display, leave all 67 of your locations in the real file!
]

service_types = [
    {"id": "starlink-installation", "name": "Starlink Installation & Setup", "desc": "Professional Starlink Gen 3 and Mini installation and mounting services"},
    {"id": "wifi-extender-setup", "name": "Wi-Fi Extender & Mesh Setup", "desc": "Custom Wi-Fi network extensions and mesh router configurations"},
    {"id": "tv-mounting-service", "name": "Professional TV Mounting", "desc": "Secure, level, and wire-free professional TV mounting services"},
    {"id": "smart-home-setup", "name": "Smart Home Device Installation", "desc": "Expert installation for security cameras, smart locks, and thermostats"},
    {"id": "ethernet-cabling", "name": "Ethernet & Low Voltage Cabling", "desc": "Clean and professional low-voltage cable routing and ethernet drops"}
]

# Content Spinner Arrays
intros = [
    "If you are located in {city} and need expert {service}, Dean's Handyman Service is your go-to mobile solution. We specialize in bringing advanced tech solutions directly to properties throughout {region}.",
    "Struggling with your tech setup in {city}? We provide top-tier {service} for homes and businesses across {region}. Skip the frustration and let a professional handle the heavy lifting.",
    "Residents of {city}, {state} know how tough it can be to find reliable tech contractors. That's why Dean brings professional {service} right to your door anywhere in {region}.",
    "Upgrade your property in {city} with our specialized {service}. With industrial-grade experience, we ensure your tech runs flawlessly across {region}."
]

why_us = [
    "Unlike standard handymen, we combine deep industrial trade skills with advanced networking knowledge. This means your {service} isn't just plugged in; it's engineered to withstand the {state} weather.",
    "Why choose Dean for your {service} in {city}? Because we treat your property like our own. Clean routing, secure mounts, and fully optimized systems are our standard.",
    "We operate a fully equipped mobile workshop. When we arrive in {city} for your {service}, we have the tools, the hardware, and the expertise to finish the job right the first time.",
    "Don't risk your expensive equipment with a DIY job. Our {service} in {region} guarantees a seamless, code-compliant, and aesthetically perfect installation."
]

ctas = [
    "Ready to get your {service} up and running in {city}? Call Dean at (281) 917-9914 to book your spot.",
    "Stop dealing with dead zones and DIY headaches. Contact us today for premier {service} in {region}.",
    "Let's get your tech sorted. Request a free quote for {service} in {city}, {state} right now.",
    "Join dozens of satisfied customers in {region}. Tap the button below to schedule your {service}."
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

    for service in service_types:
        # Seed the random number generator so the same city/service always gets the same text. 
        # This prevents Google from thinking the page is "changing" every single day.
        random.seed(city + service['id'])
        
        # Pick random content and format it with the local details
        dynamic_intro = random.choice(intros).format(city=city, state=state, region=region, service=service['name'])
        dynamic_why = random.choice(why_us).format(city=city, state=state, region=region, service=service['name'])
        dynamic_cta = random.choice(ctas).format(city=city, state=state, region=region, service=service['name'])
        dynamic_desc = f"{service['desc']} in {city}, {state}. Dean's Handyman Service provides expert mobile tech solutions for {region}."

        filename = f"{service['id']}-{url_city}-{url_state}.html"
        full_url = f"{BASE_URL}/{OUTPUT_DIR}/{filename}"
        new_urls.append(full_url)

        # Inject into HTML
        page_content = template.replace("{{SERVICE_NAME}}", service['name'])
        page_content = page_content.replace("{{SERVICE_ID}}", service['id'])
        page_content = page_content.replace("{{CITY}}", city)
        page_content = page_content.replace("{{STATE}}", state)
        page_content = page_content.replace("{{REGION}}", region)
        page_content = page_content.replace("{{URL_CITY}}", url_city)
        page_content = page_content.replace("{{URL_STATE}}", url_state)
        page_content = page_content.replace("{{META_DESC}}", dynamic_desc)
        
        # Inject the new spun content
        page_content = page_content.replace("{{INTRO_PARAGRAPH}}", dynamic_intro)
        page_content = page_content.replace("{{WHY_CHOOSE_US}}", dynamic_why)
        page_content = page_content.replace("{{CTA_TEXT}}", dynamic_cta)

        file_path = os.path.join(OUTPUT_DIR, filename)
        with open(file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(page_content)

# Update sitemap
try:
    if os.path.exists('sitemap.xml'):
        with open('sitemap.xml', 'r', encoding='utf-8') as f:
            sitemap_content = f.read()
    else:
        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>'

    if "</urlset>" in sitemap_content:
        urls_to_add = ""
        today = datetime.today().strftime('%Y-%m-%d')
        for url in new_urls:
            if f"<loc>{url}</loc>" not in sitemap_content:
                urls_to_add += f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
        
        sitemap_content = sitemap_content.replace("</urlset>", urls_to_add + "</urlset>")
        
        with open('sitemap.xml', 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
    print(f"Generated landing pages with spun content!")
except Exception as e:
    print(f"Sitemap error: {e}")
