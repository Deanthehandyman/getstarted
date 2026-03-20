import os
import random
import json

# 1. Expanded List of Services
services = [
    "Starlink Installation",
    "TV Mounting Service",
    "IKEA Assembly",
    "Amazon Assembly",
    "Moving Reassembly",
    "Smart Home Setup",
    "Handyman Services",
    "Ethernet Cabling",
    "Box To Built",
    "Rural Home and Ranch Repairs",
    "RV Electrical Setup",
    "Custom Fabrication",
    "Virtual Technical Support",
    "Smart Home Consultation",
    "Remote Troubleshooting",
    "Furniture Assembly",
    "Home Office Setup",
    "Property Maintenance",
    "Emergency Repairs",
    "Outdoor Lighting Installation",
    "Gutter Cleaning and Repair",
    "Deck and Fence Restoration",
    "Drywall and Paint Touch ups"
]

# 2. Target Cities
cities = [
    {"name": "Pittsburg", "state": "TX"}, {"name": "Tyler", "state": "TX"}, 
    {"name": "Longview", "state": "TX"}, {"name": "Texarkana", "state": "TX"}, 
    {"name": "Texarkana", "state": "AR"}, {"name": "Shreveport", "state": "LA"}, 
    {"name": "Broken Bow", "state": "OK"}, {"name": "Mount Pleasant", "state": "TX"}, 
    {"name": "Gilmer", "state": "TX"}, {"name": "Daingerfield", "state": "TX"}, 
    {"name": "Ore City", "state": "TX"}, {"name": "Hughes Springs", "state": "TX"}, 
    {"name": "Avinger", "state": "TX"}, {"name": "Naples", "state": "TX"}, 
    {"name": "Omaha", "state": "TX"}, {"name": "Big Sandy", "state": "TX"}, 
    {"name": "Hawkins", "state": "TX"}, {"name": "Winfield", "state": "TX"}, 
    {"name": "Leesburg", "state": "TX"}, {"name": "Cason", "state": "TX"}, 
    {"name": "Sulphur Springs", "state": "TX"}, {"name": "Mineola", "state": "TX"}, 
    {"name": "Lindale", "state": "TX"}, {"name": "Gladewater", "state": "TX"}, 
    {"name": "White Oak", "state": "TX"}, {"name": "Kilgore", "state": "TX"}, 
    {"name": "Marshall", "state": "TX"}, {"name": "Henderson", "state": "TX"}, 
    {"name": "Carthage", "state": "TX"}, {"name": "Center", "state": "TX"}, 
    {"name": "Nacogdoches", "state": "TX"}, {"name": "Palestine", "state": "TX"}, 
    {"name": "Athens", "state": "TX"}, {"name": "Canton", "state": "TX"}, 
    {"name": "Van", "state": "TX"}, {"name": "Grand Saline", "state": "TX"}, 
    {"name": "Wills Point", "state": "TX"}, {"name": "Terrell", "state": "TX"}, 
    {"name": "Forney", "state": "TX"}, {"name": "Rockwall", "state": "TX"}, 
    {"name": "Royse City", "state": "TX"}, {"name": "Greenville", "state": "TX"}, 
    {"name": "Commerce", "state": "TX"}, {"name": "Sulphur Bluff", "state": "TX"}, 
    {"name": "Cooper", "state": "TX"}, {"name": "Bonham", "state": "TX"}, 
    {"name": "Paris", "state": "TX"}, {"name": "Hugo", "state": "OK"}, 
    {"name": "Idabel", "state": "OK"}, {"name": "Valliant", "state": "OK"}, 
    {"name": "Antlers", "state": "OK"}, {"name": "Durant", "state": "OK"}, 
    {"name": "Sherman", "state": "TX"}, {"name": "Denison", "state": "TX"}, 
    {"name": "Pottsboro", "state": "TX"}, {"name": "Whitesboro", "state": "TX"}, 
    {"name": "Gainesville", "state": "TX"}, {"name": "Minden", "state": "LA"}, 
    {"name": "Bossier City", "state": "LA"}, {"name": "Haughton", "state": "LA"}, 
    {"name": "Vivian", "state": "LA"}, {"name": "Springhill", "state": "LA"}, 
    {"name": "Homer", "state": "LA"}, {"name": "Mansfield", "state": "LA"}, 
    {"name": "Ashdown", "state": "AR"}, {"name": "De Queen", "state": "AR"}, 
    {"name": "Nashville", "state": "AR"}, {"name": "Hope", "state": "AR"}, 
    {"name": "Prescott", "state": "AR"}, {"name": "Magnolia", "state": "AR"}, 
    {"name": "Clarksville", "state": "TX"}, {"name": "Lone Star", "state": "TX"}, 
    {"name": "Atlanta", "state": "TX"}, {"name": "Linden", "state": "TX"}
]

# 3. Create the output directory
output_dir = "service-areas"
os.makedirs(output_dir, exist_ok=True)

# 4. SEO Variations for City Hub Pages
title_templates = [
    "Expert Handyman & Tech Services in [CITY], [STATE] | Deans Handyman",
    "Top-Rated Handyman & Starlink Installer in [CITY] | Fast & Reliable",
    "[CITY]'s Best Property Maintenance & Handyman Services",
    "Affordable Home Repairs & Tech Setup in [CITY], [STATE]"
]

desc_templates = [
    "Looking for a reliable handyman or Starlink installer in [CITY], [STATE]? Deans Handyman Service LLC provides professional, fast, and local help. Call 281-917-9914 today!",
    "Get expert home repairs, tech setup, and property maintenance done right in [CITY]. We are your local, trusted professionals at Deans Handyman Service LLC.",
    "Need help with home repairs or Starlink in [CITY], [STATE]? We serve the area with top-tier handyman and technical services. Contact us for a free quote.",
]

# Generate the dynamic dropdown list for the form
dropdown_options = ""
for s in services:
    dropdown_options += f'                                <option value="{s}">{s}</option>\n'

# Generate a visual grid of services to place on the page
services_grid_html = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 2rem;">'
for s in services:
    services_grid_html += f'<div style="background: rgba(255,255,255,0.1); padding: 0.8rem 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); font-weight: 500; font-size: 0.95rem; display: flex; align-items: center; gap: 0.5rem;"><i class="fas fa-check" style="color: var(--accent);"></i> {s}</div>'
services_grid_html += '</div>'


# 5. Full HTML Template
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
    
    <meta property="og:type" content="website" />
    <meta property="og:title" content="[META_TITLE]">
    <meta property="og:description" content="[META_DESCRIPTION]">
    <meta property="og:image" content="https://deanshandymanservice.me/truck.jpg">

    <script type="application/ld+json">
    [SCHEMA_JSON]
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <style>
        :root {
            --primary: #008bd2;
            --primary-dark: #006fa8;
            --accent: #f0a500;
            --dark: #0f172a;
            --gray: #475569;
            --light: #f8fafc;
            --white: #ffffff;
            --trust-green: #22c55e;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', system-ui, sans-serif; line-height: 1.6; color: var(--dark); background: var(--light); overflow-x: hidden; }
        html { scroll-behavior: smooth; }

        h1, h2, h3 { font-family: 'Montserrat', sans-serif; font-weight: 800; line-height: 1.2; }
        h1 { font-size: clamp(2.2rem, 5vw, 3.5rem); color: white; margin-bottom: 1rem; text-shadow: 0 4px 12px rgba(0,0,0,0.6); }
        h2 { font-size: clamp(2rem, 5vw, 2.8rem); text-align: center; margin-bottom: 1.5rem; color: var(--dark); }
        h3 { font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--primary-dark); }

        .container { max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; }

        .btn-accent { background: var(--accent); color: var(--dark); box-shadow: 0 6px 20px rgba(240,165,0,0.3); padding: 0.9rem 1.8rem; border-radius: 50px; font-weight: 700; border: none; cursor: pointer; transition: all 0.3s ease; }
        .btn-accent:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(240,165,0,0.4); }
        .btn-pill { background: var(--primary); color: white !important; padding: 0.9rem 1.8rem; border-radius: 9999px; font-weight: 700; font-size: 0.95rem; white-space: nowrap; box-shadow: 0 4px 12px rgba(0,139,210,0.25); transition: all 0.3s; text-decoration: none; display: inline-flex; align-items: center;}
        .btn-pill:hover { background: var(--primary-dark); transform: translateY(-1px); }

        /* HEADER */
        header { background: white; box-shadow: 0 4px 20px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 1000; }
        .nav-container { display: flex; justify-content: space-between; align-items: center; height: 90px; }
        .logo-wrapper { display: flex; align-items: center; gap: 12px; text-decoration: none; }
        .logo-img { height: 60px; width: auto; }
        .logo-text { font-weight: 800; font-size: 1.1rem; line-height: 1.1; text-transform: uppercase; color: var(--dark); }
        .logo-text span { color: var(--primary); font-size: 0.8rem; display: block; }

        .nav-links { display: flex; align-items: center; gap: 2rem; }
        .nav-links a { color: var(--dark); font-weight: 600; text-decoration: none; text-transform: uppercase; font-size: 0.9rem; transition: color 0.3s; }
        .nav-links a:hover, .nav-links a.active { color: var(--primary); }

        .menu-toggle { display: none; flex-direction: column; gap: 6px; cursor: pointer; }
        .menu-toggle span { width: 28px; height: 3px; background: var(--dark); border-radius: 2px; transition: all 0.4s; }

        @media (max-width: 992px) {
            .menu-toggle { display: flex; }
            .nav-links { position: fixed; top: 0; right: -100%; width: 300px; height: 100vh; background: white; flex-direction: column; align-items: flex-start; padding: 120px 40px; gap: 1.5rem; transition: right 0.5s ease; box-shadow: -10px 0 30px rgba(0,0,0,0.15); }
            .nav-links.active { right: 0; }
            .nav-links a { font-size: 1.2rem; }
        }

        /* HERO */
        .hero { background: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), url('https://i.imgur.com/KMsvpls.jpg') center/cover no-repeat fixed; color: white; padding: 100px 0 80px; min-height: 85vh; display: flex; align-items: center; }
        .hero-layout { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 3rem; align-items: start; }
        .hero-text p { font-size: 1.2rem; font-weight: 400; margin-bottom: 2rem; color: #e2e8f0; }
        .trust-badges { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem; }
        .trust-badge { background: rgba(34,197,94,0.2); color: #4ade80; padding: 0.5rem 1rem; border-radius: 50px; font-weight: 700; font-size: 0.9rem; display: flex; align-items: center; gap: 0.5rem; border: 1px solid rgba(34,197,94,0.3); }

        /* FORM */
        .lead-card { background: white; padding: 2.5rem; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.2); border-top: 8px solid var(--accent); color: var(--dark); position: sticky; top: 120px; }
        .form-group { margin-bottom: 1.2rem; }
        .form-group label { display: block; margin-bottom: 0.4rem; font-weight: 700; color: var(--dark); font-size: 0.95rem; }
        .form-group input, .form-group select, .form-group textarea { width: 100%; padding: 0.8rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem; transition: border 0.3s; }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(0,139,210,0.15); }

        /* MISC */
        .payment-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; margin-top: 2rem; }
        .payment-grid a, .payment-grid div { padding: 0.8rem 1.5rem; border-radius: 8px; font-weight: 700; text-decoration: none; color: white; transition: transform 0.3s; min-width: 120px; text-align: center; }
        .payment-grid a:hover { transform: scale(1.05); }

        .mobile-fab { position: fixed; bottom: 30px; left: 30px; background: #22c55e; color: white; width: 70px; height: 70px; border-radius: 50%; display: none; align-items: center; justify-content: center; font-size: 1.8rem; box-shadow: 0 8px 25px rgba(0,0,0,0.25); z-index: 999; text-decoration: none; transition: transform 0.3s; }
        .mobile-fab:hover { transform: scale(1.1); }
        
        /* Success Modal */
        .success-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.85); z-index: 2000; align-items: center; justify-content: center; backdrop-filter: blur(4px); }
        .success-modal-content { background: white; padding: 3rem 2rem; border-radius: 16px; text-align: center; max-width: 420px; width: 90%; box-shadow: 0 20px 50px rgba(0,0,0,0.5); border-top: 8px solid var(--trust-green); }
        .success-icon { font-size: 4rem; margin-bottom: 1rem; }

        @media (max-width: 992px) {
            .hero { padding: 80px 0 60px; background-attachment: scroll; }
            .hero-layout { grid-template-columns: 1fr; }
            .lead-card { position: relative; top: 0; }
            .mobile-fab { display: flex; }
        }

        footer { background: var(--dark); color: #cbd5e1; padding: 80px 0 40px; }
        footer h4 { color: white; margin-bottom: 1.5rem; }
        footer .container { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 3rem; }
    </style>
</head>
<body>

    <div class="success-modal" id="successModal">
        <div class="success-modal-content">
            <div class="success-icon">✅</div>
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

            <div class="menu-toggle" id="mobile-menu-btn">
                <span></span><span></span><span></span>
            </div>

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
                        <div class="trust-badge">⭐ 5-Star Rated Professional</div>
                        <div class="trust-badge">📍 Serving [CITY], [STATE]</div>
                    </div>
                    
                    <h1>Expert Handyman & Tech Services in [CITY]</h1>
                    <p>From seamless Starlink installations to complete property maintenance, Deans Handyman Service LLC brings industrial-level expertise directly to your door in [CITY], [STATE].</p>
                    
                    <h3 style="color: white; margin-top: 2rem; font-size: 1.4rem;">Services Available in Your Area:</h3>
                    [SERVICES_GRID]
                </div>

                <div class="lead-card" id="contact" data-aos="fade-left">
                    <h3 style="text-align: center; margin-bottom: 0.5rem;">Request a Free Quote</h3>
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

                        <button type="submit" id="submitBtn" class="btn-accent" style="width:100%; font-size: 1.1rem; padding: 1rem;">Check Availability & Get Quote</button>
                    </form>
                </div>
            </div>
        </section>
        
        <section style="background: var(--dark); padding-top: 60px; padding-bottom: 60px;">
            <div class="container">
                <h2 style="color: white; text-align: center; font-size: 2rem;">Frictionless Payments</h2>
                <div class="payment-grid">
                    <div style="background: #334155;">💵 Cash / Check</div>
                    <a href="https://cash.app/$HandymanDean" target="_blank" rel="noopener" style="background: #00D632;">💲 Cash App</a>
                    <a href="https://venmo.com/u/DeanshandymanserviceLLC" target="_blank" rel="noopener" style="background: #008CFF;">📱 Venmo</a>
                    <a href="https://www.paypal.com/ncp/payment/CVURGTVEWZ96J" target="_blank" rel="noopener" style="background: #003087;">🅿️ PayPal</a>
                    <div style="background: #7411C5;">🟣 Zelle</div>
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
    <script>
        AOS.init({ duration: 800, once: true, offset: 50 });

        const menuBtn = document.getElementById('mobile-menu-btn');
        const navMenu = document.getElementById('nav-menu');
        menuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            const spans = menuBtn.querySelectorAll('span');
            if (navMenu.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(7px, 7px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(7px, -7px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });

        document.getElementById('quoteForm').addEventListener('submit', function(e) {
            e.preventDefault(); 
            const form = this;
            const btn = document.getElementById('submitBtn');
            btn.innerText = "Processing...";
            btn.disabled = true;

            const PUSHBULLET_TOKEN = "o.ZS7JlD9tJxXKORXgsQspxFV5fK7iDFPl";
            const name = document.getElementById('client-name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const service = document.getElementById('service').value;
            const address = document.getElementById('address').value;
            const details = document.getElementById('details').value;

            const noteBody = `🚨 NEW LEAD ([CITY] Hub Page)!\n\nName: ${name}\nPhone: ${phone}\nService: ${service}\nLocation: ${address}\nDetails: ${details}`;

            fetch('https://api.pushbullet.com/v2/pushes', {
                method: 'POST',
                headers: { 'Access-Token': PUSHBULLET_TOKEN, 'Content-Type': 'application/json' },
                body: JSON.stringify({ type: 'note', title: '🛠️ New Handyman Lead', body: noteBody })
            })
            .then(() => { triggerSuccessAndSubmit(form); })
            .catch(() => { triggerSuccessAndSubmit(form); });
        });

        function triggerSuccessAndSubmit(form) {
            document.getElementById('successModal').style.display = 'flex';
            setTimeout(() => { form.submit(); }, 2000);
        }
    </script>
</body>
</html>
"""

# 6. Generate the Pages (1 PER CITY)
for city_data in cities:
    city = city_data["name"]
    state = city_data["state"]
    
    safe_city = city.lower().replace(" ", "-")
    safe_state = state.lower()
    filename = f"handyman-services-{safe_city}-{safe_state}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Pick random SEO variations
    meta_title = random.choice(title_templates).replace("[CITY]", city).replace("[STATE]", state)
    meta_description = random.choice(desc_templates).replace("[CITY]", city).replace("[STATE]", state)
    
    # Create Advanced Schema (Listing ALL services for this city)
    offers_list = []
    for s in services:
        offers_list.append({
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": s
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Deans Handyman Service LLC",
        "telephone": "281-917-9914",
        "areaServed": {
            "@type": "City",
            "name": city,
            "containedInPlace": {
                "@type": "State",
                "name": state
            }
        },
        "makesOffer": offers_list
    }
    schema_json = json.dumps(schema, indent=4)
    
    # String replacement
    page_content = html_template.replace("[META_TITLE]", meta_title)
    page_content = page_content.replace("[META_DESCRIPTION]", meta_description)
    page_content = page_content.replace("[SCHEMA_JSON]", schema_json)
    page_content = page_content.replace("[CITY]", city)
    page_content = page_content.replace("[STATE]", state)
    page_content = page_content.replace("[SERVICES_GRID]", services_grid_html)
    page_content = page_content.replace("[DROPDOWN_OPTIONS]", dropdown_options)
    
    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(page_content)

print(f"Successfully generated {len(cities)} comprehensive City Hub pages in the '{output_dir}' folder.")

# ==========================================
# 7. AUTO-UPDATE THE AREAS.HTML DIRECTORY
# ==========================================
print("Updating the areas.html directory page...")

areas_html_template = """<!DOCTYPE html>
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
    <title>Service Areas | Dean's Handyman Service LLC – TX, AR, LA, OK</title>
    
    <meta name="description" content="Dean's Handyman Service LLC covers a 200-mile radius from Pittsburg, TX. Expert Starlink installation and skilled repairs across Texas, Arkansas, Louisiana, and Oklahoma.">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <style>
        :root { --primary: #008bd2; --primary-dark: #006fa8; --accent: #f0a500; --dark: #0f172a; --gray: #475569; --light: #f8fafc; --white: #ffffff; }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', system-ui, sans-serif; line-height: 1.6; color: var(--dark); background: var(--light); }
        h1, h2, h3 { font-family: 'Montserrat', sans-serif; font-weight: 800; }
        .container { max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; }
        
        /* HEADER */
        header { background: white; box-shadow: 0 4px 20px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 1000; }
        .nav-container { display: flex; justify-content: space-between; align-items: center; height: 90px; }
        .logo-wrapper { display: flex; align-items: center; gap: 12px; text-decoration: none; }
        .logo-img { height: 60px; width: auto; }
        .logo-text { font-weight: 800; font-size: 1.1rem; line-height: 1.1; text-transform: uppercase; color: var(--dark); }
        .logo-text span { color: var(--primary); font-size: 0.8rem; display: block; }
        .nav-links { display: flex; align-items: center; gap: 2rem; }
        .nav-links a { color: var(--dark); font-weight: 600; text-decoration: none; text-transform: uppercase; font-size: 0.9rem; transition: color 0.3s; }
        .nav-links a:hover { color: var(--primary); }
        .btn-pill { background: var(--primary); color: white !important; padding: 0.9rem 1.8rem; border-radius: 9999px; font-weight: 700; font-size: 0.95rem; white-space: nowrap; transition: all 0.3s; text-decoration: none; display: inline-flex; align-items: center;}
        
        .page-hero { background: linear-gradient(rgba(15, 23, 42, 0.75), rgba(15, 23, 42, 0.75)), url('https://i.imgur.com/KMsvpls.jpg') center/cover no-repeat fixed; color: white; padding: 120px 0 80px; text-align: center; }
        .page-hero h1 { font-size: clamp(2.8rem, 7vw, 4.5rem); margin-bottom: 1rem; }

        .search-container { text-align: center; margin: 3rem 0; }
        .search-box { width: 100%; max-width: 600px; padding: 1rem 1.5rem; border: 2px solid #e2e8f0; border-radius: 50px; font-size: 1.1rem; outline: none; transition: border-color 0.3s; }
        .search-box:focus { border-color: var(--primary); }

        /* GRID STYLES */
        .area-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; padding-bottom: 6rem; }
        .city-card { background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid var(--primary); transition: transform 0.3s; display: flex; flex-direction: column; justify-content: space-between; }
        .city-card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); border-left-color: var(--accent); }
        .city-card h3 { font-size: 1.3rem; color: var(--dark); margin-bottom: 1rem; }
        .city-btn { display: inline-block; background: #f1f5f9; color: var(--primary-dark); padding: 0.6rem 1rem; border-radius: 6px; font-weight: 600; text-decoration: none; text-align: center; transition: background 0.3s; }
        .city-btn:hover { background: var(--primary); color: white; }

        footer { background: var(--dark); color: #cbd5e1; padding: 60px 0 40px; text-align: center; }
    </style>
</head>
<body>

    <header>
        <div class="container nav-container">
            <a href="index.html" class="logo-wrapper">
                <img src="https://i.imgur.com/CtBcYkI.png" alt="Dean's Handyman Service LLC Logo" class="logo-img">
                <div class="logo-text">Dean's<br><span>Handyman Service LLC</span></div>
            </a>
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="services.html">Services</a>
                <a href="areas.html" class="active">Service Areas</a>
                <a href="tel:2819179914" class="btn-pill"><i class="fas fa-phone-alt me-2"></i>(281) 917-9914</a>
            </nav>
        </div>
    </header>

    <section class="page-hero">
        <div class="container">
            <h1>Our 200-Mile Service Area</h1>
            <p style="font-size: 1.4rem; font-weight: 500;">Expert mobile repairs and tech installations across TX, AR, LA, OK.</p>
        </div>
    </section>

    <div class="container">
        <div class="search-container">
            <input type="text" id="citySearch" class="search-box" placeholder="Search for your city (e.g., Tyler, Shreveport)...">
        </div>

        <div class="area-grid" id="areaGrid">
            [DYNAMIC_CITY_GRIDS_GO_HERE]
        </div>
    </div>

    <footer>
        <div class="container">
            <p>© 2026 Dean's Handyman Service LLC. All rights reserved.</p>
        </div>
    </footer>

    <script>
        const searchInput = document.getElementById('citySearch');
        const cityCards = document.querySelectorAll('.city-card');
        
        searchInput.addEventListener('input', (e) => {
            const filter = e.target.value.toLowerCase();
            cityCards.forEach(card => {
                const cityName = card.getAttribute('data-name').toLowerCase();
                card.style.display = cityName.includes(filter) ? 'flex' : 'none';
            });
        });
    </script>
</body>
</html>
"""

# Build the dynamic grid layout
city_cards_html = ""
for city_data in cities:
    city = city_data["name"]
    state = city_data["state"]
    safe_city = city.lower().replace(" ", "-")
    safe_state = state.lower()
    link_path = f"service-areas/handyman-services-{safe_city}-{safe_state}.html"
    
    city_cards_html += f'<div class="city-card" data-name="{city} {state}">\n'
    city_cards_html += f'  <h3>📍 {city}, {state}</h3>\n'
    city_cards_html += f'  <a href="{link_path}" class="city-btn">View Available Services</a>\n'
    city_cards_html += '</div>\n'

final_areas_html = areas_html_template.replace("[DYNAMIC_CITY_GRIDS_GO_HERE]", city_cards_html)

with open("areas.html", "w", encoding="utf-8") as f:
    f.write(final_areas_html)

# ==========================================
# 8. AUTO-GENERATE THE SITEMAP (sitemap.xml)
# ==========================================
from datetime import datetime
print("Generating sitemap.xml...")

BASE_URL = "https://deanshandymanservice.me"
now = datetime.now().strftime("%Y-%m-%d")

sitemap_content = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

core_pages = ["", "about.html", "services.html", "starlink-install.html", "areas.html", "gallery.html", "blog.html", "faqs.html", "contact.html", "privacy.html", "reviews.html"]

for page in core_pages:
    sitemap_content.append(f"""  <url>\n    <loc>{BASE_URL}/{page}</loc>\n    <lastmod>{now}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>""")

# Add only the newly consolidated City Hub pages (Priority 0.8)
for city_data in cities:
    safe_city = city_data["name"].lower().replace(" ", "-")
    safe_state = city_data["state"].lower()
    filename = f"handyman-services-{safe_city}-{safe_state}.html"
    
    sitemap_content.append(f"""  <url>\n    <loc>{BASE_URL}/service-areas/{filename}</loc>\n    <lastmod>{now}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>""")

sitemap_content.append('</urlset>')

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_content))

print("Successfully generated sitemap.xml!")
