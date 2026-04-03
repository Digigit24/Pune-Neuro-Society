import sys
content = open('contact.html', 'r', encoding='utf-8').read()
replacement = '''                </div>

                <!-- Right Form Side -->
                <div class="col-lg-7 contact-form-side">
                    <h3 class="form-title">Send us a message</h3>
                    <form action="https://formspree.io/f/contact-nsp" method="POST">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="custom-form-group">
                                    <label for="contact_name" class="visually-hidden" style="position:absolute; width:1px; height:1px; overflow:hidden;">Your Name</label>
                                    <input type="text" id="contact_name" name="name" class="custom-form-control" placeholder="Your Name" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="custom-form-group">
                                    <label for="contact_email" class="visually-hidden" style="position:absolute; width:1px; height:1px; overflow:hidden;">Email Address</label>
                                    <input type="email" id="contact_email" name="email" class="custom-form-control" placeholder="Email Address" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="custom-form-group">
                                    <label for="contact_phone" class="visually-hidden" style="position:absolute; width:1px; height:1px; overflow:hidden;">Phone Number</label>
                                    <input type="tel" id="contact_phone" name="phone" class="custom-form-control" placeholder="Phone Number" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="custom-form-group">
                                    <label for="contact_subject" class="visually-hidden" style="position:absolute; width:1px; height:1px; overflow:hidden;">Subject</label>
                                    <input type="text" id="contact_subject" name="subject" class="custom-form-control" placeholder="Subject">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="custom-form-group">
                                    <label for="contact_message" class="visually-hidden" style="position:absolute; width:1px; height:1px; overflow:hidden;">How can we help you?</label>
                                    <textarea id="contact_message" name="message" class="custom-form-control" placeholder="How can we help you?" required></textarea>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="check-terms">
                                    <input type="checkbox" id="terms_check" name="terms" required>
                                    <label for="terms_check">I agree to the terms and privacy policy.</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <button type="submit" class="vl-btn-modern">
                                    Send Message <i class="fa-solid fa-paper-plane"></i>
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>'''

search_str = '''                        <div class="social-connect">
                            <p>Follow us on social media:</p>
                            <div class="social-icons-row">
                                <a href="#" class="social-btn"><i class="fa-brands fa-facebook-f"></i></a>
                                <a href="#" class="social-btn"><i class="fa-brands fa-twitter"></i></a>
                                <a href="#" class="social-btn"><i class="fa-brands fa-linkedin-in"></i></a>
                                <a href="#" class="social-btn"><i class="fa-brands fa-instagram"></i></a>
                            </div>
                        </div>
                    </div>
    </section>'''

if search_str in content:
    replacement_str = search_str.replace('    </section>', replacement)
    content = content.replace(search_str, replacement_str)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed contact.html")
else:
    print("Could not find search string.")
