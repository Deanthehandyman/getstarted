document.addEventListener('DOMContentLoaded', function() {
    // AOS Initialization
    if (typeof AOS !== 'undefined') {
        AOS.init({ duration: 800, once: true, offset: 50 });
    }

    // Mobile Menu Toggle
    const menuBtn = document.getElementById('mobile-menu-btn');
    const navMenu = document.getElementById('nav-menu');
    if (menuBtn && navMenu) {
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
    }

    // Back to Top Button
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '↑';
    backToTop.id = 'back-to-top';
    backToTop.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTop);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });

    backToTop.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Form Handler
    const quoteForm = document.getElementById('quoteForm');
    if (quoteForm) {
        quoteForm.addEventListener('submit', function(e) {
            e.preventDefault(); 
            const form = this;
            const btn = document.getElementById('submitBtn');
            const originalBtnText = btn.innerText;
            btn.innerText = "Processing...";
            btn.disabled = true;

            // File size check
            const fileInput = document.getElementById('photo');
            if (fileInput && fileInput.files.length > 0) {
                let totalSize = 0;
                for (let i = 0; i < fileInput.files.length; i++) {
                    totalSize += fileInput.files[i].size;
                }
                if (totalSize > 10485760) {
                    alert("Whoops! Your photos are too large (over 10MB). Please select fewer photos.");
                    btn.innerText = originalBtnText;
                    btn.disabled = false;
                    return;
                }
            }

            // Pushbullet Notification (Note: Token is kept for now as per user's request to keep it the same, 
            // but in a real scenario, this should be handled server-side)
            const PUSHBULLET_TOKEN = "o.ZS7JlD9tJxXKORXgsQspxFV5fK7iDFPl";
            const name = document.getElementById('client-name')?.value || '';
            const email = document.getElementById('email')?.value || '';
            const phone = document.getElementById('phone')?.value || '';
            const service = document.getElementById('service')?.value || '';
            const address = document.getElementById('address')?.value || '';
            const details = document.getElementById('details')?.value || '';
            const hasPhoto = (fileInput && fileInput.files.length > 0) ? "YES (Check Gmail)" : "No";

            const noteBody = `🚨 NEW LEAD!\n\nName: ${name}\nEmail: ${email}\nPhone: ${phone}\nService: ${service}\nLocation: ${address}\nDetails: ${details}\nPhoto: ${hasPhoto}`;

            fetch('https://api.pushbullet.com/v2/pushes', {
                method: 'POST',
                headers: { 'Access-Token': PUSHBULLET_TOKEN, 'Content-Type': 'application/json' },
                body: JSON.stringify({ type: 'note', title: '🛠️ New Handyman Lead', body: noteBody })
            })
            .then(() => { triggerSuccessAndSubmit(form); })
            .catch(() => { triggerSuccessAndSubmit(form); });
        });
    }

    function triggerSuccessAndSubmit(form) {
        const successModal = document.getElementById('successModal');
        if (successModal) {
            successModal.style.display = 'flex';
        }
        setTimeout(() => { form.submit(); }, 2000);
    }
});
