import os
from datetime import datetime

# Configuration
IDEAS_FILE = 'getstarted/ideas.txt'
POSTS_DIR = 'getstarted/posts'

# Ensure the directory exists
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# 1. Read the ideas
if not os.path.exists(IDEAS_FILE):
    with open(IDEAS_FILE, 'w') as f:
        f.write("Starlink Installation in Pittsburg TX\nRV Repair in East Texas\nHome Maintenance Tips")

with open(IDEAS_FILE, 'r') as f:
    ideas = f.readlines()

# 2. Process the first 3
if len(ideas) > 0:
    to_post = [i.strip() for i in ideas[:3]]
    remaining = ideas[3:]

    for idea in to_post:
        safe_name = idea.lower().replace(" ", "-").replace(":", "").replace("/", "")
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{POSTS_DIR}/{date_str}-{safe_name}.html"
        
        # Professional SEO-focused HTML Template
        blog_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{idea} | Dean's Handyman Service</title>
    <meta name="description" content="Professional {idea} services in Pittsburg, TX and surrounding East Texas areas.">
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 20px; }}
        .button {{ background: #2ecc71; color: white; padding: 15px 25px; text-decoration: none; border-radius: 5px; display: inline-block; }}
    </style>
</head>
<body>
    <h1>{idea}</h1>
    <p>Are you looking for expert help with <strong>{idea}</strong> in the Pittsburg or East Texas area? You've come to the right place.</p>
    <p>At Dean's Handyman Service LLC, we specialize in high-quality home repairs, custom fabrication, and Starlink networking solutions tailored to the unique needs of our local community.</p>
    <br>
    <a href="https://deanshandymanservice.me" class="button">Visit DeansHandymanService.me for a Quote</a>
    <hr>
    <p><small>Serving Pittsburg, TX 75686 and surrounding areas. Call: 281-917-9914</small></p>
</body>
</html>"""
        
        with open(filename, 'w') as f:
            f.write(blog_content)

    # 3. Update the ideas file (removes the 3 we just used)
    with open(IDEAS_FILE, 'w') as f:
        f.writelines([line + '\n' for line in remaining if line.strip()])

