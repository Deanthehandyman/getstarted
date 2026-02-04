import os
from datetime import datetime
import glob

# Configuration
IDEAS_FILE = 'ideas.txt'
POSTS_DIR = 'posts' # The script will create this folder automatically
SITEMAP_FILE = 'sitemap_blogs.xml'

# 1. Create the folder automatically if it's missing
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# 2. Read the ideas
if not os.path.exists(IDEAS_FILE):
    print("ideas.txt not found.")
    exit()

with open(IDEAS_FILE, 'r') as f:
    ideas = f.readlines()

# 3. Process the first 3 ideas
if len(ideas) > 0:
    to_post = [i.strip() for i in ideas[:3]]
    remaining = ideas[3:]

    for idea in to_post:
        safe_name = idea.lower().replace(" ", "-").replace(":", "").replace("/", "")
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{POSTS_DIR}/{date_str}-{safe_name}.html"
        
        blog_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{idea} | Dean's Handyman Service LLC</title>
    <meta name="description" content="Expert {idea} services in Pittsburg, TX.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://deanthehandyman.github.io/posts/{date_str}-{safe_name}.html">
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 20px; }}
        .btn {{ background: #d4af37; color: black; padding: 15px 25px; text-decoration: none; border-radius: 4px; font-weight: bold; display: inline-block; }}
    </style>
</head>
<body>
    <a href="../index.html">← Back to Home</a>
    <h1>{idea}</h1>
    <p>Need professional help with <strong>{idea}</strong> in Pittsburg or East Texas?</p>
    <p>Dean's Handyman Service LLC provides industrial-grade solutions for homes, ranches, and RVs.</p>
    <br>
    <a href="https://deanshandymanservice.me?utm_source=blog&utm_medium={safe_name}" class="btn">Get a Quote at DeansHandymanService.me</a>
    <hr>
    <p><small>© 2026 Dean's Handyman Service LLC | Pittsburg, TX 75686 | 281-917-9914</small></p>
</body>
</html>"""
        
        with open(filename, 'w') as f:
            f.write(blog_content)

    # 4. Update ideas.txt
    with open(IDEAS_FILE, 'w') as f:
        f.writelines([line + '\n' for line in remaining if line.strip()])

# 5. Build the Blog Sitemap
all_posts = glob.glob(f"{POSTS_DIR}/*.html")
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
for post in all_posts:
    base_file = os.path.basename(post)
    sitemap_xml += f'  <url>\\n    <loc>https://deanthehandyman.github.io/posts/{base_file}</loc>\\n    <changefreq>monthly</changefreq>\\n  </url>\\n'
sitemap_xml += '</urlset>'

with open(SITEMAP_FILE, 'w') as f:
    f.write(sitemap_xml)
