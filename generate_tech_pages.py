import os
import random
import json
import hashlib
import requests

# --- CONFIGURATION ---
PUSHBULLET_TOKEN = os.getenv("PUSHBULLET_TOKEN") # Set this in GitHub Secrets or your env
OUTPUT_DIR = "service-areas"
MANIFEST_FILE = "page_manifest.json"

# 1. Services & Cities (Kept from your original script)
services = [
    "Starlink Installation", "Smart Home Setup", "Wi-Fi & Network Optimization",
    "Security Camera Installation", "Ethernet Cabling", "Smart Home Consultation",
    "TV Mounting Service", "Home Office Setup", "Remote Troubleshooting",
    "Virtual Technical Support", "IKEA Assembly", "Amazon Assembly", 
    "Moving Reassembly", "Handyman Services", "Box To Built", 
    "Rural Home and Ranch Repairs", "RV Electrical Setup", 
    "Custom Fabrication", "Furniture Assembly", "Property Maintenance", 
    "Emergency Repairs", "Outdoor Lighting Installation", 
    "Gutter Cleaning and Repair", "Deck and Fence Restoration", 
    "Drywall and Paint Touch ups"
]

cities = [
    {"name": "Pittsburg", "state": "TX"}, {"name": "Tyler", "state": "TX"}, 
    {"name": "Longview", "state": "TX"}, {"name": "Texarkana", "state": "TX"}
    # ... rest of your cities list
]

# (Content pools and html_template omitted for brevity, keep your existing ones here)

def get_content_hash(content):
    """Creates a unique fingerprint of the page content."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def send_push_summary(new_count, updated_count, total):
    """Sends a single summary to Pushbullet."""
    if not PUSHBULLET_TOKEN:
        print("Pushbullet token not found. Skipping notification.")
        return

    summary = (
        f"🚀 SEO Update Complete\n"
        f"----------------------\n"
        f"🆕 New Pages: {new_count}\n"
        f"🔄 Updated: {updated_count}\n"
        f"📁 Total Live: {total}\n"
        f"----------------------\n"
        f"View changes at: https://github.com/Deanthehandyman/getstarted"
    )
    
    requests.post(
        "https://api.pushbullet.com/v2/pushes",
        headers={"Access-Token": PUSHBULLET_TOKEN},
        json={"type": "note", "title": "🛠️ Site Sync Summary", "body": summary}
    )

# --- MAIN EXECUTION ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load existing manifest
if os.path.exists(MANIFEST_FILE):
    with open(MANIFEST_FILE, 'r') as f:
        manifest = json.load(f)
else:
    manifest = {}

new_pages = 0
updated_pages = 0

for city_data in cities:
    city, state = city_data["name"], city_data["state"]
    random.seed(city) # Keep it consistent
    
    filename = f"handyman-services-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # ... [Insert your existing logic to build 'page_content' here] ...
    page_content = "Generated HTML here..." 

    current_hash = get_content_hash(page_content)
    old_hash = manifest.get(filename)

    if old_hash is None:
        new_pages += 1
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_content)
        manifest[filename] = current_hash
    elif old_hash != current_hash:
        updated_pages += 1
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_content)
        manifest[filename] = current_hash

# Save updated manifest
with open(MANIFEST_FILE, 'w') as f:
    json.dump(manifest, f, indent=4)

# Final Summary Push
send_push_summary(new_pages, updated_pages, len(manifest))

print(f"Done! New: {new_pages}, Updated: {updated_pages}")
