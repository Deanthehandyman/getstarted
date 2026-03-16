import os
import random
    from datetime import datetime
    import glob # Added for cleanup
    import json # Added for schema
    
    # Configuration
    BASE_URL = "https://deanshandymanservice.me"
    OUTPUT_DIR = "service-areas"
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # --- Cleanup old files ---
    old_files_patterns = [
        "amazon-assembly-*.html", 
        "starlink-installation-*.html",
        "tv-mounting-*.html",
        "ikea-assembly-*.html",
        "moving-reassembly-*.html",
        "smart-home-setup-*.html",
        "handyman-*.html",
        "ethernet-cabling-*.html",
        "box-to-built-*.html"
    ]
    for pattern in old_files_patterns:
        for old_file in glob.glob(pattern):
            try:
                os.remove(old_file)
                print(f"Removed old file: {old_file}")
            except OSError as e:
                print(f"Error removing file {old_file}: {e}")
    # --- End Cleanup ---
    
    
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
        {"city": "Gainesville", "state": "TX", "region": "Cooke County"},
        {"city": "Gilmer", "state": "TX", "region": "Upshur County"},
        {"city": "Greenville", "state": "TX", "region": "Hunt County"},
        {"city": "Hope", "state": "AR", "region": "Hempstead County"},
        {"city": "Hugo", "state": "OK", "region": "Choctaw County"},
        {"city": "Idabel", "state": "OK", "region": "McCurtain County"},
        {"city": "Jefferson", "state": "TX", "region": "Marion County"},
        {"city": "Kilgore", "state": "TX", "region": "Gregg and Rusk Counties"},
        {"city": "Longview", "state": "TX", "region": "Gregg and Harrison Counties"},
        {"city": "Magnolia", "state": "AR", "region": "Columbia County"},
        {"city": "Marshall", "state": "TX", "region": "Harrison County"},
        {"city": "Minden", "state": "LA", "region": "Webster Parish"},
        {"city": "Mount Pleasant", "state": "TX", "region": "Titus County"},
        {"city": "Nacogdoches", "state": "TX", "region": "Nacogdoches County"},
        {"city": "Nashville", "state": "AR", "region": "Howard County"},
        {"city": "Palestine", "state": "TX", "region": "Anderson County"},
        {"city": "Paris", "state": "TX", "region": "Lamar County"},
        {"city": "Pittsburg", "state": "TX", "region": "Camp County"},
        {"city": "Prescott", "state": "AR", "region": "Nevada County"},
        {"city": "Sherman", "state": "TX", "region": "Grayson County"},
        {"city": "Shreveport", "state": "LA", "region": "Caddo Parish"},
        {"city": "Sulphur Springs", "state": "TX", "region": "Hopkins County"},
        {"city": "Texarkana", "state": "TX/AR", "region": "Bowie County/Miller County"},
        {"city": "Tyler", "state": "TX", "region": "Smith County"},
        {"city": "Van", "state": "TX", "region": "Van Zandt County"},
        {"city": "Wills Point", "state": "TX", "region": "Van Zandt County"}
    ]
    
    services = [
        {"name": "Starlink Installation", "slug": "starlink-installation", "keywords": "Starlink installation, satellite internet setup, Starlink dish mounting", "h1": "Starlink Installation", "h2": "Professional Starlink Dish Installation", "description": "Expert Starlink installation services in {city}. Fast satellite internet setup for your home or business."},
        {"name": "TV Mounting Service", "slug": "tv-mounting-service", "keywords": "TV mounting, wall mount TV, flat screen mounting", "h1": "TV Mounting", "h2": "Secure TV Wall Mounting Service", "description": "Professional TV mounting service in {city}. Secure wall mounting for all TV sizes and types."},
        {"name": "IKEA Assembly", "slug": "ikea-assembly", "keywords": "IKEA assembly, furniture assembly, flat pack assembly", "h1": "IKEA Furniture Assembly", "h2": "IKEA & Flat Pack Furniture Assembly", "description": "IKEA and flat pack furniture assembly service in {city}. Quick and reliable assembly for your new furniture."},
        {"name": "Amazon Assembly", "slug": "amazon-assembly", "keywords": "Amazon assembly, furniture assembly, product assembly", "h1": "Amazon Product Assembly", "h2": "Amazon & Online Order Assembly", "description": "Assembly service for Amazon purchases and other online orders in {city}. We build it for you."},
        {"name": "Moving Reassembly", "slug": "moving-reassembly", "keywords": "furniture reassembly, moving help, disassembly and reassembly", "h1": "Furniture Reassembly After Moving", "h2": "Moving? We Disassemble & Reassemble", "description": "Furniture disassembly and reassembly services in {city} for your move. We make moving easier."},
        {"name": "Smart Home Setup", "slug": "smart-home-setup", "keywords": "smart home setup, smart device installation, home automation", "h1": "Smart Home Device Setup", "h2": "Smart Home Installation Services", "description": "Smart home device setup and installation in {city}. Get your smart thermostat, lights, and speakers connected."},
        {"name": "Handyman Services", "slug": "handyman", "keywords": "handyman, home repair, general contractor, home maintenance", "h1": "Handyman Services", "h2": "Reliable Handyman for Home Repairs", "description": "General handyman services in {city}. Home repairs, maintenance, and installations."},
        {"name": "Ethernet Cabling", "slug": "ethernet-cabling", "keywords": "ethernet cabling, network wiring, Cat6 installation", "h1": "Ethernet & Network Cabling", "h2": "Ethernet & Data Cabling Installation", "description": "Ethernet and network cabling installation in {city}. Structured cabling for homes and offices."},
        {"name": "Box To Built", "slug": "box-to-built", "keywords": "furniture assembly, product assembly, flat pack", "h1": "From Box To Built Assembly", "h2": "Any Product Assembly Service", "description": "We assemble anything that comes in a box in {city}. Furniture, grills, fitness equipment, and more."}
    ]
    
    # --- Title and Description Variations ---
    title_variations = [
        "{service_name} in {city}, {state} | {business_name}",
        "Expert {service_name} {city} | {business_name}",
        "{city} {service_name} - Call Us | {business_name}",
        "Affordable {service_name} {city}, {state} | {business_name}"
    ]
    
    description_variations = [
        "Need {service_name} in {city}, {state}? {business_name} offers professional services. Call {phone_number} for a quote.",
        "Your local expert for {service_name} in {city}. {business_name} provides fast and reliable service. Contact us at {phone_number}.",
        "Looking for {service_name} near {city}? {business_name} is here to help. Phone: {phone_number}.",
        "Get top-rated {service_name} in {city}, {state} with {business_name}. Call {phone_number} today!"
    ]
    business_name = "Deans Handyman Service LLC"
    phone_number = "281-917-9914"
    # --- End Variations ---
    
    
    for service in services:
        for location in locations:
            city = location["city"]
            state = location["state"]
            region = location["region"]
            service_name = service["name"]
            slug = service["slug"]
            
            filename = f"{slug}-{city.lower().replace(' ', '-')}-{state.lower()}.html"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            # --- Choose random title/description ---
            random_title = random.choice(title_variations).format(service_name=service_name, city=city, state=state, business_name=business_name)
            random_description = random.choice(description_variations).format(service_name=service_name, city=city, state=state, business_name=business_name, phone_number=phone_number)
            # --- End random choice ---
    
            # --- LocalBusiness Schema ---
            schema = {
                "@context": "https://schema.org",
                "@type": "LocalBusiness",
                "name": business_name,
                "telephone": phone_number,
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": city,
                    "addressRegion": state
                },
                "description": f"Providing {service_name} and handyman services in {city}, {state}.",
                "url": f"{BASE_URL}/{OUTPUT_DIR}/{filename}"
            }
            schema_script = f'<script type="application/ld+json">{json.dumps(schema)}</script>'
            
            html_content = f\"\"\"<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{random_title}</title>
        <meta name="description" content="{random_description}">
        <meta name="keywords" content="{service["keywords"]}, {city}, {state}, {region}">
        {schema_script}
    </head>
    <body>
        <h1>{service["h1"]} in {city}, {state}</h1>
        <h2>{service["h2"]}</h2>
        <p>{service["description"].format(city=city)}</p>
        <p>Serving {city}, {state} and the surrounding {region}.</p>
        <p>Contact {business_name} at {phone_number}</p>
    </body>
    </html>\"\"\"
            
            with open(filepath, 'w') as f:
                f.write(html_content)
            print(f"Generated: {filepath}")
    
