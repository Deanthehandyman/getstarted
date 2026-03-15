import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import time

# 1. Open your local sitemap to get the list of all URLs
print("🤖 Booting up the tester bot...")
try:
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
except FileNotFoundError:
    print("❌ Error: Could not find sitemap.xml in this folder.")
    exit()

# Extract all the links from the XML
urls = []
for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
    urls.append(loc)

print(f"📡 Found {len(urls)} pages to test. Firing away...\n")

bad_links = []
count = 0

# 2. Ping every single URL like a web browser
for url in urls:
    count += 1
    try:
        # Create a request that pretends to be a real web browser (so servers don't block the bot)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=10)
        
        if response.getcode() == 200:
            print(f"✅ [{count}/{len(urls)}] LIVE: {url}")
            
    except urllib.error.HTTPError as e:
        print(f"🚨 [{count}/{len(urls)}] BROKEN ({e.code}): {url}")
        bad_links.append((url, e.code))
    except urllib.error.URLError as e:
        print(f"⚠️  [{count}/{len(urls)}] FAILED TO CONNECT: {url}")
        bad_links.append((url, "Connection Error"))
    
    # Pause for a split second so we don't crash your web host by asking for 670 pages at once
    time.sleep(0.1) 

# 3. Print the final report
print("\n" + "="*40)
print("📊 TEST COMPLETE")
print("="*40)

if not bad_links:
    print("🎉 ALL PAGES ARE LIVE! No 404 errors found.")
else:
    print(f"⚠️ Found {len(bad_links)} broken pages:")
    for link, error in bad_links:
        print(f" - {error}: {link}")
