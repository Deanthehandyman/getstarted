import os
import random
import json
import hashlib
import urllib.request
import urllib.parse

# --- CONFIGURATION ---
# Ensure PUSHBULLET_TOKEN is set in your GitHub Secrets
PUSHBULLET_TOKEN = os.getenv("PUSHBULLET_TOKEN") 
OUTPUT_DIR = "service-areas"
MANIFEST_FILE = "page_manifest.json"

# 1. Business Info
BUSINESS_NAME = "Deans Handyman Service LLC"
PHONE = "281-917-9914"
URL = "https://share.google/mbSD0mHW19fklhEiR"

# 2. Service & City Data
services = [
    "Starlink Installation", "Smart Home Setup", "Wi-Fi & Network Optimization",
    "Security Camera Installation", "Ethernet Cabling", "TV Mounting Service",
    "Home Office Setup", "Remote Troubleshooting", "Virtual Technical Support",
    "RV Electrical Setup", "Custom Fabrication", "Property Maintenance", 
    "Emergency Repairs", "Outdoor Lighting Installation"
]

cities = [
    {"name": "Pittsburg", "state": "TX"}, {"name": "Tyler", "state": "TX"}, 
    {"name": "Longview", "state": "TX"}, {"name": "Texarkana", "state": "TX"},
    {"name": "Mineola", "state": "TX"}, {"name": "Daingerfield", "state": "TX"}
]

# 3. HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{service} in {city}, {state} | {business}</title>
    <meta name="description" content="Professional {service} and technical support in {city}, {state}. Call {phone} today.">
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: auto; padding: 20px; }}
        header {{ background: #222; color: #fff; padding: 1rem; text-align: center; }}
        .cta {{ background: #f4f4f4; padding: 20px; border-left: 5px solid #007bff; margin: 20px 0; }}
        a {{ color: #007bff; }}
    </style>
</head>
<body>
    <header><h1>{service} in {city}</h1></header>
    <main>
        <p>Looking for <strong>{service}</strong> in {city}, {state}? {business} provides white-glove technical installations and handyman services.</p>
        <div class="cta">
            <p>Call or Text: <strong>{phone}</strong></p>
            <p><a href="{url}">Book Online Now</a></p>
        </div>
    </main>
    <footer><p>&copy; 2024 {business}</p></footer>
</body>
</html>
"""

def get_content_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def send_push_summary(new_count, updated_count, total):
    """Sends summary using built-in urllib (No 'requests' needed)."""
    if not PUSHBULLET_TOKEN:
        print("Pushbullet token missing. Skipping alert.")
        return

    body_text = (
        f"🛠️ SEO Bot Report\n"
        f"----------------------\n"
        f"🆕 New: {new_count}\n"
        f"🔄 Updated: {updated_count}\n"
        f"📁 Total: {total}\n"
        f"----------------------"
    )
    
    data = json.dumps({
        "type": "note",
        "title": "Site Update Complete",
        "body": body_text
    }).encode('utf-8')

    req = urllib.request.Request(
        "https://api.pushbullet.com/v2/pushes",
        data=data,
        headers={
            "Access-Token": PUSHBULLET_TOKEN,
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            print("Pushbullet notification sent.")
    except Exception as e:
        print(f"Failed to send notification: {e}")

# --- EXECUTION ---
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, 'r') as f:
            manifest = json.load(f)
    else:
        manifest = {}

    new_pages = 0
    updated_pages = 0

    for city_data in cities:
        city, state = city_data["name"], city_data["state"]
        random.seed(city) 
        primary_service = random.choice(services)
        
        filename = f"handyman-services-{city.lower().replace(' ', '-')}-{state.lower()}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        content = HTML_TEMPLATE.format(
            service=primary_service, city=city, state=state,
            business=BUSINESS_NAME, phone=PHONE, url=URL
        )

        current_hash = get_content_hash(content)
        old_hash = manifest.get(filename)

        if old_hash != current_hash:
            if old_hash is None: new_pages += 1
            else: updated_pages += 1
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            manifest[filename] = current_hash

    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest, f, indent=4)

    if new_pages > 0 or updated_pages > 0:
        send_push_summary(new_pages, updated_pages, len(manifest))
    
    print(f"Process complete. New: {new_pages}, Updated: {updated_pages}")

if __name__ == "__main__":
    main()
