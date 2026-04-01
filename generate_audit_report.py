#!/usr/bin/env python3
"""Generate a comprehensive website audit PDF report for Neurological Society of Pune."""

from fpdf import FPDF
from datetime import datetime


class AuditPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "Confidential - Neurological Society of Pune", align="L")
            self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
            self.line(10, 16, 200, 16)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "Confidential - Neurological Society of Pune", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(2, 17, 26)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 123, 255)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 80, self.get_y())
        self.ln(4)

    def sub_section(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(9, 30, 66)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def issue_row(self, issue_id, severity, file_loc, description):
        self.set_font("Helvetica", "B", 9)
        # Severity color
        colors = {
            "CRITICAL": (220, 53, 69),
            "HIGH": (255, 140, 0),
            "MEDIUM": (255, 193, 7),
            "LOW": (40, 167, 69),
        }
        r, g, b = colors.get(severity, (100, 100, 100))
        self.set_text_color(r, g, b)
        self.cell(18, 6, issue_id)
        # Severity badge
        self.set_fill_color(r, g, b)
        self.set_text_color(255, 255, 255)
        self.cell(22, 6, severity, fill=True, align="C")
        self.set_text_color(80, 80, 80)
        self.set_font("Helvetica", "", 8)
        self.cell(2)
        self.cell(50, 6, file_loc)
        self.ln(7)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(60, 60, 60)
        self.set_x(15)
        self.multi_cell(180, 5, description)
        self.ln(3)

    def summary_row(self, label, value, bold=False):
        self.set_font("Helvetica", "B" if bold else "", 10)
        self.set_text_color(40, 40, 40)
        self.cell(100, 7, label)
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 7, str(value), new_x="LMARGIN", new_y="NEXT")


def build_report():
    pdf = AuditPDF()
    pdf.set_auto_page_break(auto=True, margin=20)

    # ===================== PAGE 1: COVER =====================
    pdf.add_page()
    pdf.ln(30)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(2, 17, 26)
    pdf.cell(0, 14, "Website Audit Report", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 16)
    pdf.set_text_color(0, 123, 255)
    pdf.cell(0, 10, "Neurological Society of Pune (NSP)", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)
    pdf.set_draw_color(0, 123, 255)
    pdf.set_line_width(1)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(12)

    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    details = [
        ("Report Date", datetime.now().strftime("%B %d, %Y")),
        ("Scope", "Full website audit - 6 HTML pages + JS assets"),
        ("Pages Audited", "index.html, about.html, activities.html, contact.html, committe.html, invited_faculties.html"),
        ("Assets Audited", "main.js, CSS plugins, Font Awesome CDN, image assets"),
        ("Auditor", "Automated Audit Tool"),
        ("Status", "Errors Listed - No Code Changes Made"),
    ]
    for label, val in details:
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(45, 7, label + ":")
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(140, 7, val)
        pdf.ln(1)

    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(2, 17, 26)
    pdf.cell(0, 10, "Executive Summary", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 6, (
        "A comprehensive audit of the Neurological Society of Pune website has identified "
        "29 issues across 6 HTML pages and 1 JavaScript file. These range from critical JavaScript "
        "crashes and broken CDN links to spelling errors and accessibility gaps. "
        "This report lists every error found without making any code modifications."
    ))
    pdf.ln(6)

    # Summary table
    pdf.set_fill_color(2, 17, 26)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(60, 8, "Severity", fill=True, align="C")
    pdf.cell(40, 8, "Count", fill=True, align="C")
    pdf.cell(80, 8, "% of Total", fill=True, align="C", new_x="LMARGIN", new_y="NEXT")

    rows = [("Critical", "5", "17%"), ("High", "6", "21%"), ("Medium", "6", "21%"), ("Low / Spelling & Grammar", "12", "41%")]
    pdf.set_text_color(40, 40, 40)
    for i, (sev, cnt, pct) in enumerate(rows):
        bg = (245, 245, 245) if i % 2 == 0 else (255, 255, 255)
        pdf.set_fill_color(*bg)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(60, 7, sev, fill=True, align="C")
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(40, 7, cnt, fill=True, align="C")
        pdf.cell(80, 7, pct, fill=True, align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_fill_color(2, 17, 26)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(60, 8, "TOTAL", fill=True, align="C")
    pdf.cell(40, 8, "29", fill=True, align="C")
    pdf.cell(80, 8, "100%", fill=True, align="C", new_x="LMARGIN", new_y="NEXT")

    # ===================== PAGE 2: CRITICAL ISSUES =====================
    pdf.add_page()
    pdf.section_title("1. Critical Issues (5)")

    pdf.issue_row("C-01", "CRITICAL", "main.js:57-58",
        "JavaScript null reference crash: document.querySelector('.progress-wrap path') returns null on pages "
        "that don't have a .progress-wrap element (about.html, activities.html, contact.html). "
        "Calling .getTotalLength() on null causes an uncaught TypeError that halts ALL subsequent "
        "JavaScript execution on those pages, breaking sliders, AOS animations, mobile menu, and the preloader.")

    pdf.issue_row("C-02", "CRITICAL", "All 6 HTML pages",
        "Font Awesome CDN link references version 7.0.1 which does not exist on cdnjs. "
        "The URL https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css returns a 404 error. "
        "Latest available is 6.x. The SRI hash is also invalid. This means all Font Awesome icons loaded via "
        "the CDN will fail to render on every page of the site.")

    pdf.issue_row("C-03", "CRITICAL", "index.html:291-293",
        "Template placeholder data from the original theme is still visible in the mobile menu: "
        "Phone shows '+57 9954 6476' (Colombian number), email shows 'hello@exdos.com', "
        "location shows 'Bhemeara, Kushtia' (Bangladesh). This is the theme developer's dummy data, not NSP's. "
        "Additionally, the envelope icon is paired with the phone number and the phone icon with the email (swapped).")

    pdf.issue_row("C-04", "CRITICAL", "All 6 footers",
        "Footer email field displays 'Contact details to be updated' - a visible placeholder text "
        "that is shown to all visitors. This appears in every page's footer section.")

    pdf.issue_row("C-05", "CRITICAL", "activities.html:7",
        "<title> tag says 'About Us - Neurological Society of Pune' instead of 'Activities'. "
        "This appears in browser tabs, bookmarks, and search engine results, misleading users.")

    # ===================== PAGE 3: HIGH ISSUES =====================
    pdf.add_page()
    pdf.section_title("2. High Priority Issues (6)")

    pdf.issue_row("H-01", "HIGH", "index.html:517-550",
        "Broken internal links: 'projects-single.html' is referenced 4 times in the Key Milestones section "
        "but the page does not exist in the repository. Clicking these links will produce a 404 error.")

    pdf.issue_row("H-02", "HIGH", "index.html:769-867",
        "Broken internal links: 'team.html' is referenced 6 times (team member name links) "
        "but the page does not exist. All team member names in the Executive Committee section are dead links.")

    pdf.issue_row("H-03", "HIGH", "index.html:945-1051",
        "Broken internal links: 'blog-single.html' is referenced 5 times in the blog/news cards section. "
        "The page does not exist. All 'Read More' links and blog card titles are dead links.")

    pdf.issue_row("H-04", "HIGH", "committe.html, invited_faculties.html",
        "Missing AOS.init() call: Both pages include the AOS library (aos.js) and use data-aos attributes "
        "on elements, but neither page calls AOS.init() in their inline scripts. "
        "As a result, scroll-triggered animations will never activate on these two pages.")

    pdf.issue_row("H-05", "HIGH", "committe.html",
        "Filename typo: The file is named 'committe.html' (missing the second 'e'). "
        "All navigation links across all 6 pages reference this misspelled filename. "
        "Should be 'committee.html'.")

    pdf.issue_row("H-06", "HIGH", "contact.html:516-557",
        "Contact form action is '#' with no backend handler. Form inputs lack name and id attributes. "
        "Submitting the form does nothing - data cannot be processed or received. "
        "The form is entirely non-functional.")

    # ===================== PAGE 4: MEDIUM ISSUES =====================
    pdf.add_page()
    pdf.section_title("3. Medium Priority Issues (6)")

    pdf.issue_row("M-01", "MEDIUM", "committe.html vs invited_faculties.html",
        "Duplicate content: The Committee page (committe.html) displays the exact same 6 faculty member "
        "cards as the Invited Faculties page. The committee page heading says 'Committee Members' but "
        "shows faculty profiles instead of actual NSP executive committee members with their roles "
        "(President, Secretary, Treasurer, etc.).")

    pdf.issue_row("M-02", "MEDIUM", "committe.html:297, invited_faculties.html:297",
        "Inconsistent mobile menu logo: These two pages use 'logo1.png' for the offcanvas mobile menu logo, "
        "while the other 4 pages (index, about, activities, contact) use '21 Logo.png'. "
        "This creates an inconsistent brand appearance when navigating on mobile.")

    pdf.issue_row("M-03", "MEDIUM", "All 6 pages - footer",
        "All social media links (Facebook, LinkedIn, Instagram, YouTube) in both the header and footer "
        "sections across all 6 pages have href='#'. They are non-functional placeholder links that "
        "scroll to the top of the page when clicked instead of navigating to actual social profiles.")

    pdf.issue_row("M-04", "MEDIUM", "All 6 pages - footer",
        "Footer 'Key Activities' section: All 5 links (Monthly Neuromeets, NSP Approach Meet, "
        "PG Approach Meeting, Invited Lectures, Public Awareness Drives) are href='#' placeholders. "
        "Additionally, 'News & Updates', 'Privacy Policy', and 'Terms Of Condition' footer links are all dead.")

    pdf.issue_row("M-05", "MEDIUM", "All 6 pages - footer",
        "Bootstrap grid issue: The copyright section uses <div class='col-lg-12'> placed directly outside "
        "the <div class='row'> container. Per Bootstrap's grid system, column classes must be direct children "
        "of a .row element. This causes incorrect padding and alignment of the copyright bar.")

    pdf.issue_row("M-06", "MEDIUM", "main.js:106",
        "Dead code: 'AOS.init;' on line 106 is a property access with missing parentheses '()'. "
        "It does nothing. Line 107-109 has AOS.init({disable: 'mobile'}) which does work, but only inside "
        "the IIFE. On pages like about.html, activities.html and contact.html that call AOS.init() in inline "
        "scripts, the duplicate initialization may cause unexpected behavior.")

    # ===================== PAGE 5: ACCESSIBILITY ISSUES =====================
    pdf.add_page()
    pdf.section_title("4. Accessibility Issues (6)")

    pdf.issue_row("A-01", "MEDIUM", "All 6 pages",
        "All images across the site have empty alt='' attributes or non-descriptive alt text. "
        "This means screen readers cannot convey image content to visually impaired users. "
        "Examples: preloader image, footer logo, gallery images, team member photos.")

    pdf.issue_row("A-02", "MEDIUM", "contact.html:520-541",
        "Contact form inputs have no associated <label> elements. Placeholders alone are not accessible - "
        "they disappear when the user starts typing, and screen readers may not announce them properly. "
        "Each input needs a proper <label> with a matching 'for' attribute.")

    pdf.issue_row("A-03", "MEDIUM", "All 6 pages - footer/header",
        "Social media links use icon-only content (<i class='fa-brands fa-facebook-f'>) with no "
        "aria-label or screen-reader-only text. Screen readers will announce these as empty links "
        "with no accessible name.")

    pdf.issue_row("A-04", "MEDIUM", "index.html:313-315",
        "The hero section video element has no <track> element for captions or subtitles. "
        "While it is a background video with no audio content, adding kind='descriptions' "
        "is recommended for WCAG 2.1 Level A compliance.")

    pdf.issue_row("A-05", "MEDIUM", "All 6 pages",
        "The mobile menu toggle button <button class='vl-offcanvas-toggle'> has no aria-label. "
        "Screen readers will only announce 'button' with no indication of what it does. "
        "Should have aria-label='Open navigation menu'.")

    pdf.issue_row("A-06", "MEDIUM", "index.html, contact.html",
        "The contact page title tag says 'Neurological Society of Pune' (generic) and index.html "
        "also uses 'Neurological Society of Pune'. These are not unique, descriptive page titles. "
        "Each page should have a unique <title> for SEO and accessibility. Multiple pages share "
        "identical <meta name='description'> content as well.")

    # ===================== PAGE 6: SPELLING & GRAMMAR =====================
    pdf.add_page()
    pdf.section_title("5. Spelling & Grammar Errors (12)")

    spelling_errors = [
        ("SG-01", "index.html:462", "'It is on of its kind meeting'", "Should be 'one of its kind'"),
        ("SG-02", "index.html:453-454", "'It consisted of Neurophysician and Neurosurgeons practicing in city of Pune. There used to have once monthly neuromeets where different hospitals will present their cases.'",
         "Grammar issues: 'consisted' should be 'consists' (present tense), 'There used to have' should be 'They used to have', 'will present' should be 'would present'"),
        ("SG-03", "All 6 footers", "'Terms Of Condition'", "Should be 'Terms and Conditions'"),
        ("SG-04", "All 6 footers", "'Copyright @2025'", "Should be 'Copyright (c) 2025' using proper copyright symbol"),
        ("SG-05", "activities.html:622", "'Last but not the least'", "Should be 'Last but not least' (standard English idiom without 'the')"),
        ("SG-06", "committe.html (filename)", "'committe'", "Should be 'committee' - missing second 'e'"),
        ("SG-07", "assets/img/logo/preloder.png", "'preloder'", "Should be 'preloader' - filename typo"),
        ("SG-08", "assets/img/conerence-talk.png", "'conerence'", "Should be 'conference' - filename typo"),
        ("SG-09", "assets/img/logo/21 Logo.png", "Space in filename '21 Logo.png'",
         "Filenames with spaces can cause issues on web servers and in URLs. Should use '21-Logo.png' or '21_Logo.png'"),
        ("SG-10", "committe.html:379-381, invited_faculties.html:378-380",
         "'Associate Professor, Harvard Medical School, Philadelphia, USA'",
         "Harvard Medical School is located in Boston, Massachusetts, not Philadelphia. This is a factual error in the faculty bio."),
        ("SG-11", "index.html:456-458", "'it was decided to have bigger format of neuromeets and thus started the Approach meet'",
         "Grammar: Should be 'a bigger format' (missing article 'a')"),
        ("SG-12", "index.html:447", "'NSP was established in year 2010'",
         "Grammar: Should be 'in the year 2010' (missing article 'the')"),
    ]

    for sid, loc, found, fix in spelling_errors:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(40, 167, 69)
        pdf.cell(18, 6, sid)
        pdf.set_fill_color(40, 167, 69)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(14, 6, "LOW", fill=True, align="C")
        pdf.set_text_color(80, 80, 80)
        pdf.set_font("Helvetica", "", 8)
        pdf.cell(2)
        pdf.cell(50, 6, loc)
        pdf.ln(7)
        pdf.set_x(15)
        pdf.set_font("Helvetica", "I", 8)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(180, 4.5, f"Found: {found}")
        pdf.set_x(15)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(180, 4.5, f"Correction: {fix}")
        pdf.ln(3)

    # ===================== PAGE 7: JS AUDIT =====================
    pdf.add_page()
    pdf.section_title("6. JavaScript Audit Details")

    js_issues = [
        ("JS-01", "CRITICAL", "main.js:57-58",
         "progressPath = document.querySelector('.progress-wrap path') returns null on pages without .progress-wrap. "
         "Calling .getTotalLength() on null throws TypeError halting all JS."),
        ("JS-02", "HIGH", "main.js:106",
         "AOS.init; is a no-op (property access, not function call). Missing parentheses '()'."),
        ("JS-03", "HIGH", "main.js:130-131",
         "Swapped prev/next arrows: prevArrow points to '.next-arrow' and nextArrow points to '.prev-arrow'. "
         "This reverses navigation direction for the case-slider-area Slick carousel."),
        ("JS-04", "HIGH", "main.js:170-171",
         "Same swapped arrow issue in testimonial-slider: prevArrow: $('.next-arrow1'), nextArrow: $('.prev-arrow1')."),
        ("JS-05", "HIGH", "main.js:189-190",
         "Same swapped arrow issue in hero-main-slider: prevArrow: $('.next-arrow-hero'), nextArrow: $('.prev-arrow-hero')."),
        ("JS-06", "HIGH", "main.js:283-284",
         "Same swapped arrow issue in cas3-widget-slider-area: prevArrow: $('.next-arrow-case3'), nextArrow: $('.prev-arrow-case3')."),
        ("JS-07", "HIGH", "main.js:390-391",
         "Same swapped arrow issue in service-widget-slider-area: prevArrow: $('.next-arrow-ser4'), nextArrow: $('.prev-arrow-ser4')."),
        ("JS-08", "MEDIUM", "main.js:474-478",
         "Counter code is outside the jQuery IIFE wrapper. Uses jQuery '$' which may not be available "
         "if another library defines '$'. Should be inside the (function($){...})(jQuery) wrapper."),
        ("JS-09", "LOW", "main.js:119-415",
         "All Slick slider initializations are outside $(document).ready() block. While Slick works with "
         "deferred DOM, this could cause race conditions on slow connections. Best practice is to initialize "
         "inside document.ready."),
    ]

    for jid, sev, loc, desc in js_issues:
        pdf.issue_row(jid, sev, loc, desc)

    # ===================== PAGE 8: RECOMMENDATIONS =====================
    pdf.add_page()
    pdf.section_title("7. Files Audited")

    files = [
        "index.html - Home page (1298 lines)",
        "about.html - About page (676 lines)",
        "activities.html - Activities page (815 lines)",
        "contact.html - Contact page (778 lines)",
        "committe.html - Committee page (676 lines)",
        "invited_faculties.html - Faculty page (665 lines)",
        "assets/js/main.js - Main JavaScript (478 lines)",
    ]
    for f in files:
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(5)
        pdf.cell(0, 7, f"  {f}", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(6)
    pdf.section_title("8. Recommendations")

    recommendations = [
        "1. Fix the Font Awesome CDN link to use version 6.5.1 (or latest 6.x) across all 6 pages. This will restore all FA icons site-wide.",
        "2. Wrap the progressPath code in main.js with a null check: if (progressPath) { ... }. This prevents the JS crash on pages without .progress-wrap.",
        "3. Replace all template placeholder data: Remove exdos.com email, +57 phone, Bhemeara address from index.html mobile menu. Replace 'Contact details to be updated' in all footers with the actual email from contact.html.",
        "4. Fix the activities.html <title> tag to say 'Activities - Neurological Society of Pune'.",
        "5. Add AOS.init({once: true}) to inline scripts on committe.html and invited_faculties.html.",
        "6. Remove dead links (team.html, projects-single.html, blog-single.html) or create those pages. Replace with existing pages like invited_faculties.html and activities.html.",
        "7. Add proper name/id attributes and <label> elements to the contact form. Implement a backend handler (e.g., Formspree, Netlify Forms, or a custom endpoint).",
        "8. Populate the Committee page with actual NSP executive committee members and their roles instead of duplicating the Faculty page content.",
        "9. Add real social media URLs for Facebook, LinkedIn, Instagram, and YouTube across all pages.",
        "10. Fix all spelling/grammar errors listed in Section 5, including the Harvard/Philadelphia factual error.",
        "11. Rename 'committe.html' to 'committee.html' and update all nav links across all 6 pages.",
        "12. Add meaningful alt text to all images and aria-labels to icon-only links for accessibility compliance.",
    ]

    for rec in recommendations:
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 5.5, rec)
        pdf.ln(2)

    pdf.ln(6)
    pdf.set_draw_color(200, 200, 200)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 7, "--- End of Report ---", align="C")

    # Save
    output_path = "/home/user/Pune-Neuro-Society/Website_Audit_Report.pdf"
    pdf.output(output_path)
    print(f"PDF generated: {output_path}")
    print(f"Pages: {pdf.page_no()}")


if __name__ == "__main__":
    build_report()
