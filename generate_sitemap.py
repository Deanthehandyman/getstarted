import os
from datetime import datetime

# Configuration - Match these to your previous script
BASE_URL = "https://deanshandymanservice.me"
OUTPUT_DIR = "service-areas"
SITEMAP_FILENAME = "sitemap.xml"

def generate_sitemap():
    # Start the XML structure
    now = datetime.now().strftime("%Y-%m-%d")
    sitemap_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    # 1. Add your main homepage first (optional but recommended)
    sitemap_content.append(f"""  <url>
    <loc>{BASE_URL}/</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>""")

    # 2. Loop through the generated service files
    if os.path.exists(OUTPUT_DIR):
        files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html")]
        print(f"Found {len(files)} pages to index.")

        for filename in files:
            # Construct the full URL
            # Note: We include the OUTPUT_DIR in the path
            url = f"{BASE_URL}/{OUTPUT_DIR}/{filename}"
            
            entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""
            sitemap_content.append(entry)
    else:
        print(f"Directory {OUTPUT_DIR} not found!")
        return

    # Close the tag
    sitemap_content.append('</urlset>')

    # Write the file
    with open(SITEMAP_FILENAME, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_content))
    
    print(f"Successfully created {SITEMAP_FILENAME}")

if __name__ == "__main__":
    generate_sitemap()
