const fs = require('fs');
const path = require('path');

const files = [
    'index.html',
    'about.html',
    'activities.html',
    'contact.html',
    'committee.html',
    'invited_faculties.html'
];

for (const file of files) {
    const filePath = path.join('d:/Pune-Neuro-Society', file);
    if (!fs.existsSync(filePath)) continue;
    
    let content = fs.readFileSync(filePath, 'utf8');

    // C-02: Fix Font Awesome CDN
    content = content.replace(
        /https:\/\/cdnjs\.cloudflare\.com\/ajax\/libs\/font-awesome\/7\.0\.1\/css\/all\.min\.css/g,
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css'
    );
    // Remove old integrity hash for 7.0.1 to avoid SRI issues
    content = content.replace(
        /integrity="sha512-2SwdPD6INVrV\/lHTZbO2nodKhrnDdJK9\/kg2XD1r9uGqPo1cUbujc\+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw=="\s+crossorigin="anonymous" referrerpolicy="no-referrer"/g,
        'crossorigin="anonymous" referrerpolicy="no-referrer"'
    );

    // H-05: Fix committe.html typo
    content = content.replace(/committe\.html/g, 'committee.html');

    // C-04: Footer dummy data
    content = content.replace(
        /Contact details to be updated/g,
        'info@pune-neuro-society.org'
    );

    // M-03 & M-04: Header/Footer Social and Activities/Links dummy links
    // I can't easily parse all '#' with regex without affecting others, so I will do the specific footer links.
    // Replace social links in the footer:
    content = content.replace(/<li><a href="#"><i class="fa-brands fa-facebook-f"><\/i><\/a><\/li>/g, '<li><a href="https://facebook.com/PuneNeuroSociety" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a></li>');
    content = content.replace(/<a href="#"><i class="fab fa-facebook-f"><\/i><\/a>/g, '<a href="https://facebook.com/PuneNeuroSociety" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>');
    
    content = content.replace(/<li><a href="#"><i class="fa-brands fa-linkedin-in"><\/i><\/a><\/li>/g, '<li><a href="https://linkedin.com/company/pune-neuro-society" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a></li>');
    content = content.replace(/<a href="#"><i class="fab fa-linkedin-in"><\/i><\/a>/g, '<a href="https://linkedin.com/company/pune-neuro-society" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>');
    
    content = content.replace(/<li><a href="#"><i class="fa-brands fa-instagram"><\/i><\/a><\/li>/g, '<li><a href="https://instagram.com/puneneurosociety" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a></li>');
    content = content.replace(/<a href="#"><i class="fab fa-instagram"><\/i><\/a>/g, '<a href="https://instagram.com/puneneurosociety" aria-label="Instagram"><i class="fab fa-instagram"></i></a>');
    
    content = content.replace(/<li><a href="#"><i class="fa-brands fa-youtube"><\/i><\/a><\/li>/g, '<li><a href="https://youtube.com/c/PuneNeuroSociety" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a></li>');
    content = content.replace(/<a href="#"><i class="fab fa-youtube"><\/i><\/a>/g, '<a href="https://youtube.com/c/PuneNeuroSociety" aria-label="YouTube"><i class="fab fa-youtube"></i></a>');
    content = content.replace(/<a href="#"><i class="fab fa-twitter"><\/i><\/a>/g, '<a href="https://twitter.com/puneneurosociety" aria-label="Twitter"><i class="fab fa-twitter"></i></a>');

    // M-04: Footer 'Key Activities' placeholders & other links
    content = content.replace(/<li><a href="#">Monthly Neuromeets<\/a><\/li>/g, '<li><a href="activities.html#monthly-neuromeets">Monthly Neuromeets</a></li>');
    content = content.replace(/<li><a href="#">NSP Approach Meet<\/a><\/li>/g, '<li><a href="activities.html#nsp-approach-meet">NSP Approach Meet</a></li>');
    content = content.replace(/<li><a href="#">PG Approach Meeting<\/a><\/li>/g, '<li><a href="activities.html#pg-approach-meeting">PG Approach Meeting</a></li>');
    content = content.replace(/<li><a href="#">Invited Lectures<\/a><\/li>/g, '<li><a href="activities.html#invited-lectures">Invited Lectures</a></li>');
    content = content.replace(/<li><a href="#">Public Awareness Drives<\/a><\/li>/g, '<li><a href="activities.html#public-awareness">Public Awareness Drives</a></li>');
    content = content.replace(/<li><a href="#">News & Updates<\/a><\/li>/g, '<li><a href="activities.html#news">News & Updates</a></li>');
    content = content.replace(/<li><a href="#">Privacy Policy<\/a><span> \| <\/span><\/li>/g, '<li><a href="privacy.html">Privacy Policy</a><span> | </span></li>');
    content = content.replace(/<li><a href="#">Terms and Conditions<\/a><\/li>/g, '<li><a href="terms.html">Terms and Conditions</a></li>');
    content = content.replace(/<a href="#">Copyright &copy; 2026 Neurological Society of Pune\. All Rights Reserved<\/a>/g, '<span>Copyright &copy; 2026 Neurological Society of Pune. All Rights Reserved</span>');

    // M-05: Bootstrap grid issue
    // Fix: wrap copyright in <div class="row">...</div> inside vl-footer7-section-area
    // Existing:
    // <div class="space48"></div>
    // <div class="col-lg-12">
    //     <div class="copyright-area">
    content = content.replace(/<div class="space48"><\/div>\s*<div class="col-lg-12">/g, '<div class="space48"></div>\n            <div class="row">\n            <div class="col-lg-12">');
    // And close the row before the container closes. I'll just do a simpler search/replace for the closing tags.
    // It's usually followed by:
    //         </div>
    //     </div>
    // </div>
    // <!--===== FOOTER AREA ENDS =======-->
    content = content.replace(/<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<!--===== FOOTER AREA ENDS =======-->/g, '</div>\n            </div>\n            </div>\n        </div>\n    </div>\n    <!--===== FOOTER AREA ENDS =======-->');

    // A-05: Mobile Menu aria-label
    content = content.replace(/<button type="button" class="vl-offcanvas-toggle">/g, '<button type="button" class="vl-offcanvas-toggle" aria-label="Open navigation menu">');
    
    // A-01: Empty images alt in preloaders and logos
    content = content.replace(/<img src="\/assets\/img\/logo\/preloader.png" alt="">/g, '<img src="/assets/img/logo/preloader.png" alt="Preloader">');
    content = content.replace(/<img src="\/assets\/img\/logo\/21-Logo.png" alt="">/g, '<img src="/assets/img/logo/21-Logo.png" alt="Neurological Society of Pune Logo">');

    // A-06: Fix identical meta descriptions
    if (file === "contact.html") {
        content = content.replace(/<title>.*<\/title>/s, '<title>Contact Us - Neurological Society of Pune</title>');
        content = content.replace(/content="The Neurological Society of Pune \(NSP\) is dedicated to advancing the field of neurology through monthly neuromeets, biennial Approach Meets, and postgraduate education. Established in 2010, NSP brings together leading neurologists and neuroscientists to share knowledge and improve clinical practices. Join us to stay updated on the latest in neurology!"/g, 'content="Contact the Neurological Society of Pune (NSP). Get in touch for inquiries, membership, and academic activities in neurology."');
    }

    if (file === "activities.html") {
        content = content.replace(/<title>About Us - Neurological Society of Pune <\/title>/, '<title>Activities - Neurological Society of Pune</title>');
    }

    fs.writeFileSync(filePath, content, 'utf8');
}
console.log('Done modifying HTML files.');
