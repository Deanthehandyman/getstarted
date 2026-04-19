import os
import random
import json

# 1. Expanded List of Services - Reordered to prioritize tech
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

# 2. Target Cities
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

output_dir = "service-areas"
os.makedirs(output_dir, exist_ok=True)

# 3. CONTENT POOLS - Updated for Tech Focus
title_templates = [
    "Starlink & Smart Home Expert in [CITY], [STATE] | Deans Handyman",
    "Top-Rated Tech Handyman & Wi-Fi Installer in [CITY] | Fast & Reliable",
    "[CITY]'s Best Smart Home Security & Tech Setup Services",
    "Professional Starlink Installation & Home Tech in [CITY], [STATE]",
    "Mobile Tech Specialist & Handyman Serving [CITY], [STATE]"
]

desc_templates = [
    "Need a Starlink expert or smart home installer in [CITY], [STATE]? Deans Handyman Service LLC specializes in high-tech setups and professional home repairs. Call 281-917-9914!",
    "Get expert Wi-Fi optimization, security camera setup, and Starlink installation in [CITY]. We combine tech skills with industrial-grade handyman repairs.",
    "Your local [CITY] specialist for Starlink Gen 3, smart home security, and custom networking. Industrial expertise for modern home technology.",
    "Deans Handyman Service LLC offers specialized tech installations and mobile repair services throughout [CITY]. Fast scheduling for Starlink and smart home setups."
]

h1_pool = [
    "Starlink & Smart Home Specialist in [CITY]",
    "Advanced Tech & Handyman Services for [CITY]",
    "Professional Starlink & Wi-Fi Setup in [CITY]",
    "Your Local [CITY] Tech & Repair Expert",
    "Reliable Mobile Tech & Handyman in [CITY], [STATE]"
]

hero_p_pool = [
    "From professional Starlink Gen 3 installations to custom Wi-Fi networking, Deans Handyman Service LLC brings advanced technical skills and industrial-grade reliability to [CITY], [STATE].",
    "Specializing in the tech jobs others turn down. Whether it's a complex smart home setup or heavy-duty ranch repairs, we serve the [CITY] community with precision and care.",
    "Get your home connected and secured. We provide [CITY] with expert Starlink mounting, security camera integration, and the skilled labor to handle any property repair.",
    "We bridge the gap between high-tech networking and old-school craftsmanship. Serving [CITY] with specialized Starlink, Wi-Fi, and industrial-strength handyman services."
]

bullet_pool = [
    "Specialized in Starlink Gen 3, Mini, and Custom Wi-Fi Networks.",
    "Smart Home Security, Cameras, and Automated Systems Expert.",
    "Industrial-grade tools for rock-solid technical installations.",
    "Locally owned and mobile-ready for fast service in [CITY].",
    "First 100 miles of travel from our base is completely free.",
    "Expertise in rural properties, RVs, and off-grid tech setups.",
    "Clear communication and transparent pricing for every project."
]

faq_pool = [
    {"q": "Who is the best Starlink installer in [CITY], [STATE]?", "a": "Deans Handyman Service LLC is the leading specialist for Starlink Gen 3 and Mini installations in [CITY]. We ensure optimal mounting, cable routing, and Wi-Fi performance."},
    {"q": "Do you offer smart home setup in [CITY]?", "a": "Yes! We install and configure smart security cameras, smart locks, thermostats, and whole-home mesh Wi-Fi networks throughout [CITY]."},
    {"q": "Can a handyman handle complex networking in [CITY]?", "a": "Dean isn't just a handyman; he's a tech specialist with industrial training, making him uniquely qualified for complex networking and technical installs in [CITY]."},
    {"q": "What other services do you provide in [CITY]?", "a": "Beyond tech, we handle rural home repairs, custom fabrication, electrical troubleshooting, and general property maintenance for [CITY] residents."},
    {"q": "How do I get a quote for tech services in [CITY]?", "a": "Simply fill out our online form or call 281-917-9914. We provide transparent, upfront quotes for all technical and handyman projects in [CITY]."}
]

dropdown_options = ""
for s in services:
    dropdown_options += f'                                <option value="{s}">{s}</option>\n'

# 4. Full HTML Template - Updated to use external CSS/JS
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-F2BSN968QN"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-F2BSN968QN');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>[META_TITLE]</title>
    <meta name="description" content="[META_DESCRIPTION]">
    <meta name="geo.placename" content="[CITY], [STATE]">
    
    <meta property="og:type" content="website" />
    <meta property="og:title" content="[META_TITLE]">
    <meta property="og:description" content="[META_DESCRIPTION]">
    <meta property="og:image" content="../truck.jpg">

    <script type="application/ld+json">
    [SCHEMA_JSON]
    </script>
    
    <script type="application/ld+json">
    [FAQ_SCHEMA_JSON]
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>

    <div class="success-modal" id="successModal">
        <div class="success-modal-content">
            <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
            <h3 style="margin-bottom: 0.5rem; color: var(--dark);">Project Details Sent!</h3>
            <p style="color: var(--gray); font-size: 1.05rem;">Taking you to Dean's secure calendar to book your quick review call...</p>
        </div>
    </div>

    <header>
        <div class="container nav-container">
            <a href="../index.html" class="logo-wrapper">
                <img src="https://i.imgur.com/CtBcYkI.png" alt="Dean's Handyman Service LLC Logo" class="logo-img">
                <div class="logo-text">Dean's<br><span>Handyman Service LLC</span></div>
            </a>
            <div class="menu-toggle" id="mobile-menu-btn"><span></span><span></span><span></span></div>
            <nav class="nav-links" id="nav-menu">
                <a href="../index.html">Home</a>
                <a href="../about.html">About</a>
                <a href="../services.html" class="active">Services</a>
                <a href="../starlink-install.html">Starlink</a>
                <a href="../areas.html">Service Areas</a>
                <a href="../gallery.html">Work</a>
                <a href="../blog.html">Blog</a>
                <a href="../faqs.html">FAQs</a>
                <a href="../contact.html">Contact</a>
                <a href="tel:2819179914" class="btn-pill"><i class="fas fa-phone-alt me-2"></i>(281) 917-9914</a>
            </nav>
        </div>
    </header>

    <a href="tel:2819179914" class="mobile-fab" aria-label="Call Now">📞</a>

    <main>
        <section class="hero">
            <div class="container hero-layout">
                <div class="hero-text" data-aos="fade-right">
                    <div class="trust-badges">
                        <div class="trust-badge">📡 Tech & Repair Specialist</div>
                        <div class="trust-badge">📍 Serving [CITY], [STATE]</div>
                    </div>
                    
                    <h1>[HERO_H1]</h1>
                    <p>[HERO_P]</p>
                    
                    <ul>
                        [DYNAMIC_BULLETS]
                    </ul>
                    
                    <h3 style="color: white; margin-top: 2.5rem; font-size: 1.3rem;">Specialized Services in [CITY]:</h3>
                    [SERVICES_GRID]
                </div>

                <div class="lead-card" id="contact" data-aos="fade-left">
                    <h3 style="text-align: center; margin-bottom: 0.5rem;">Get a Free [CITY] Quote</h3>
                    <p style="text-align: center; font-size: 0.9rem; color: #666; margin-bottom: 1.5rem;">Select your service below and I'll contact you shortly.</p>
                    
                    <form id="quoteForm" action="https://formsubmit.co/deanshandymanservice1@gmail.com" method="POST" enctype="multipart/form-data">
                        <input type="hidden" name="_subject" value="🚨 NEW LEAD ([CITY] Hub Page)">
                        <input type="hidden" name="_next" value="https://calendar.app.google/wAGf72SYFC5io4nV9">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="hidden" name="_template" value="table">

                        <div class="form-group">
                            <label for="client-name">Full Name</label>
                            <input type="text" id="client-name" name="Client_Name" placeholder="First & Last Name" required>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                            <div class="form-group">
                                <label for="phone">Phone Number</label>
                                <input type="tel" id="phone" name="Phone_Number" placeholder="(555) 555-5555" required>
                            </div>
                            <div class="form-group">
                                <label for="email">Email</label>
                                <input type="email" id="email" name="Email" placeholder="your@email.com" required>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="service">Service Needed</label>
                            <select id="service" name="Service_Requested" required>
                                <option value="" disabled selected>Select a Service...</option>
[DROPDOWN_OPTIONS]
                                <option value="Other">Other / General Inquiry</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="address">Project Location</label>
                            <input type="text" id="address" name="Location" value="[CITY], [STATE]" required>
                        </div>

                        <div class="form-group">
                            <label for="details">Project Details</label>
                            <textarea id="details" name="Project_Details" rows="3" placeholder="What needs fixing, building, or installing?" required></textarea>
                        </div>

                        <div class="form-group">
                            <label for="photo">Upload Photo (Optional)</label>
                            <input type="file" id="photo" name="attachment" class="file-upload" accept="image/*">
                        </div>

                        <button type="submit" id="submitBtn" class="btn-accent" style="width:100%; font-size: 1.1rem; padding: 1rem;">Check Availability & Get Quote</button>
                    </form>
                </div>
            </div>
        </section>
        
        <section style="padding: 80px 0; background: white;">
            <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
                <div data-aos="fade-right">
                    <h2>Local Service in [CITY], [STATE]</h2>
                    <p style="font-size: 1.1rem; color: var(--gray); margin-bottom: 2rem;">We take pride in our work. Check out some of our recent technical installations and property upgrades. From hidden Starlink wires to custom ranch repairs, we treat your property like our own.</p>
                    
                    <iframe 
                        width="100%" 
                        height="250" 
                        style="border:0; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);" 
                        loading="lazy" 
                        allowfullscreen 
                        src="https://maps.google.com/maps?q=[MAP_CITY],+[STATE]&t=&z=11&ie=UTF8&iwloc=&output=embed">
                    </iframe>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;" data-aos="fade-left">
                    <img src="../truck.jpg" alt="Starlink Installation in [CITY]" style="width: 100%; height: 250px; object-fit: cover; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <img src="../oldtruck.jpg" alt="Handyman Repair in [CITY]" style="width: 100%; height: 250px; object-fit: cover; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                </div>
            </div>
        </section>

        <section style="padding: 80px 0; background: var(--light);">
            <div class="container">
                <h2 style="text-align: center;">Frequently Asked Questions in [CITY]</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem;">
                    [DYNAMIC_FAQS]
                </div>
            </div>
        </section>

        <section style="background: var(--dark); padding-top: 60px; padding-bottom: 60px;">
            <div class="container">
                <h2 style="color: white; text-align: center; font-size: 2rem;">Frictionless Payments</h2>
                <div class="payment-grid">
                    <div style="background: #334155;">💵 Cash / Check</div>
                    <a href="https://cash.app/$HandymanDean" target="_blank" rel="noopener" style="background: #00D632;">💲 Cash App</a>
                    <a href="https://venmo.com/u/HandymanDean" target="_blank" rel="noopener" style="background: #008CFF;">📱 Venmo</a>
                    <a href="https://paypal.me/HandymanDean" target="_blank" rel="noopener" style="background: #003087;">🅿️ PayPal</a>
                    <div style="background: #7411C5;">🟣 Zelle (281-917-9914)</div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <div>
                <h4>Dean's Handyman Service LLC</h4>
                <p>Pittsburg, TX 75686<br>Mobile Service across TX, AR, LA, OK<br>Professional tradesman with industrial training</p>
            </div>
            <div>
                <h4>Contact Me directly</h4>
                <p>Phone: <a href="tel:2819179914" style="color: var(--primary); text-decoration: none;">(281) 917-9914</a><br>
                Email: <a href="mailto:deanshandymanservice1@gmail.com" style="color: var(--primary); text-decoration: none;">deanshandymanservice1@gmail.com</a></p>
            </div>
        </div>
        <div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #334155; font-size: 0.9rem; opacity: 0.6;">
            © 2026 Dean's Handyman Service LLC. All rights reserved.
        </div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="../js/script.js"></script>
</body>
</html>
"""

# 6. Generate the Pages
for city_data in cities:
    city = city_data["name"]
    state = city_data["state"]
    random.seed(city)
    
    safe_city = city.lower().replace(" ", "-")
    safe_state = state.lower()
    safe_map_city = city.replace(" ", "+")
    filename = f"handyman-services-{safe_city}-{safe_state}.html"
    filepath = os.path.join(output_dir, filename)
    
    meta_title = random.choice(title_templates).replace("[CITY]", city).replace("[STATE]", state)
    meta_description = random.choice(desc_templates).replace("[CITY]", city).replace("[STATE]", state)
    hero_h1 = random.choice(h1_pool).replace("[CITY]", city).replace("[STATE]", state)
    hero_p = random.choice(hero_p_pool).replace("[CITY]", city).replace("[STATE]", state)
    
    selected_bullets = random.sample(bullet_pool, 3)
    bullets_html = ""
    for bullet in selected_bullets:
        bullets_html += f"<li>{bullet.replace('[CITY]', city)}</li>\n"
        
    shuffled_services = services.copy()
    # Ensure tech services are always included in the grid
    tech_services = shuffled_services[:6]
    other_services = shuffled_services[6:]
    random.shuffle(other_services)
    display_services = tech_services + other_services[:6]
    
    services_grid_html = '<div style="display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 1rem;">'
    for s in display_services: 
        icon = "fa-satellite-dish" if "Starlink" in s or "Wi-Fi" in s or "Network" in s else "fa-wrench"
        services_grid_html += f'<div style="background: rgba(255,255,255,0.1); padding: 0.5rem 1rem; border-radius: 50px; border: 1px solid rgba(255,255,255,0.2); font-weight: 500; font-size: 0.85rem;"><i class="fas {icon}" style="color: var(--accent); margin-right: 5px;"></i> {s}</div>'
    services_grid_html += '</div>'
    
    selected_faqs = random.sample(faq_pool, 3)
    faqs_html = ""
    faq_schema_elements = []
    
    for faq in selected_faqs:
        q = faq['q'].replace("[CITY]", city).replace("[STATE]", state)
        a = faq['a'].replace("[CITY]", city).replace("[STATE]", state)
        faqs_html += f'<div style="background: var(--light); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--primary);"><h4>{q}</h4><p>{a}</p></div>\n'
        faq_schema_elements.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema_elements}
    faq_schema_json = json.dumps(faq_schema, indent=4)
    
    offers_list = [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s}} for s in services]
    schema = {"@context": "https://schema.org", "@type": "LocalBusiness", "name": "Deans Handyman Service LLC", "telephone": "281-917-9914", "areaServed": {"@type": "City", "name": city, "containedInPlace": {"@type": "State", "name": state}}, "makesOffer": offers_list}
    schema_json = json.dumps(schema, indent=4)
    
    page_content = html_template.replace("[META_TITLE]", meta_title).replace("[META_DESCRIPTION]", meta_description).replace("[SCHEMA_JSON]", schema_json).replace("[FAQ_SCHEMA_JSON]", faq_schema_json).replace("[CITY]", city).replace("[STATE]", state).replace("[MAP_CITY]", safe_map_city).replace("[HERO_H1]", hero_h1).replace("[HERO_P]", hero_p).replace("[DYNAMIC_BULLETS]", bullets_html).replace("[SERVICES_GRID]", services_grid_html).replace("[DYNAMIC_FAQS]", faqs_html).replace("[DROPDOWN_OPTIONS]", dropdown_options)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(page_content)

print(f"Successfully generated {len(cities)} highly unique City Hub pages with Maps and Photo Support in the '{output_dir}' folder.")
