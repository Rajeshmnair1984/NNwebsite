import os
import re

template_file = "/Users/raj/Documents/GitHub/NN Wesbite/NNwebsite/services.html"
with open(template_file, "r") as f:
    template_content = f.read()

pages = [
    ("screen-repair.html", "Screen Repair", "Professional and quick screen replacement services for your devices."),
    ("battery-replacement.html", "Battery Replacement", "Restore your device's battery life with our certified battery replacement."),
    ("water-damage-repair.html", "Water Damage Repair", "Expert recovery and repair for liquid-damaged electronics."),
    ("diagnostics.html", "Diagnostics", "Comprehensive diagnostics to identify and resolve underlying hardware or software issues."),
    ("repair-faqs.html", "Repair FAQs", "Answers to your most common repair-related questions."),
    ("phone-cases-protection.html", "Phone Cases & Protection", "High-quality cases and screen protectors to keep your devices safe."),
    ("chargers-cables.html", "Chargers & Cables", "Reliable charging solutions and cables for all your smart devices."),
    ("audio-headphones.html", "Audio & Headphones", "Premium audio accessories, from wireless earbuds to over-ear headphones."),
    ("pre-owned-devices.html", "Certified Pre-Owned Devices", "Quality-checked, certified pre-owned smartphones and tablets."),
    ("warranty-returns.html", "Warranty & Returns", "Information on our transparent warranty and returns policies."),
    ("mobile-plans.html", "Mobile Plans", "Flexible and affordable mobile plans tailored to your connectivity needs."),
    ("internet-services.html", "Internet Services", "High-speed and reliable internet services for your home or business."),
    ("sim-activation.html", "SIM Activation", "Quick and seamless SIM activation to get you connected instantly."),
    ("plan-comparison.html", "Plan Comparison", "Compare our connectivity plans to find the right fit for you."),
    ("device-setup.html", "Device Setup", "Hassle-free setup services for your new computers, smartphones, and tablets."),
    ("data-transfer.html", "Data Transfer", "Securely migrate your photos, contacts, and files to your new device."),
    ("virus-removal.html", "Virus Removal", "Expert removal of malware and viruses to keep your data secure."),
    ("smart-home-support.html", "Smart Home Support", "Installation and troubleshooting for your smart home devices."),
    ("pos-payment-solutions.html", "POS & Payment Solutions", "Modern point-of-sale systems and secure payment gateways for your business."),
    ("website-development.html", "Website Development", "Custom web development services to establish your online presence."),
    ("app-development.html", "App Development", "Bespoke mobile and web app development to scale your business operations."),
    ("business-automation.html", "Business Automation", "Streamline your workflows with our business automation and integration tools."),
    ("digital-marketing.html", "Digital Marketing", "Data-driven digital marketing strategies to grow your brand and reach."),
    ("alberta-locations.html", "Alberta Locations", "Find a Near Nerd store in Edmonton, Edson, Wetaskiwin, Camrose, Morinville, Sylvan Lake, Peace River, Drayton Valley, or Grande Prairie."),
    ("yukon-locations.html", "Yukon Locations", "Visit our store in Whitehorse, Yukon for expert tech support."),
    ("our-story.html", "Our Story", "Learn about the origins and journey of Near Nerd."),
    ("mission-values.html", "Mission & Values", "Discover the core principles that drive our commitment to quality tech service."),
    ("careers.html", "Careers", "Join the Near Nerd team and build a career in technology solutions."),
    ("why-near-nerd.html", "Why Near Nerd", "See why customers and franchisees trust Near Nerd for their technology needs."),
    ("business-model.html", "The Business Model", "Understand our proven and scalable business model for franchise success."),
    ("what-you-get.html", "What You Get (Support & Training)", "Comprehensive support, training, and resources we provide to our franchise partners."),
    ("apply-discovery-call.html", "Apply / Book Discovery Call", "Take the first step towards franchise ownership with a short discovery call."),
    ("investing.html", "Investing", "Explore the financial opportunities of investing with Near Nerd."),
    ("investment-overview.html", "Investment Overview", "Detailed breakdown of the investment required to launch a Near Nerd franchise."),
    ("available-territories.html", "Available Territories", "Discover high-potential markets currently available for new franchise locations."),
    ("tech-tips.html", "Tech Tips", "Actionable tips and tricks to get the most out of your devices."),
    ("repair-advice.html", "Repair Advice", "Expert insights on troubleshooting and when it's time to seek professional repair."),
    ("business-insights.html", "Business Insights", "Articles and guides on leveraging technology for business growth."),
    ("connectivity-guides.html", "Connectivity Guides", "Step-by-step guides on networking, mobile plans, and internet setup."),
    ("community-news.html", "Community News", "Updates and announcements from Near Nerd and the communities we serve."),
    ("product-faqs.html", "Product FAQs", "Answers regarding accessories, pre-owned devices, and new hardware."),
    ("telecom-faqs.html", "Telecom FAQs", "Common questions on our mobile plans, internet services, and SIM activations."),
    ("franchise-faqs.html", "Franchise FAQs", "Frequently asked questions for prospective Near Nerd franchise owners."),
    ("customer-support.html", "Customer Support", "Get assistance from our dedicated customer support team."),
    ("franchise-inquiry.html", "Franchise Inquiry", "Contact our franchise development team to learn more about ownership opportunities."),
    ("general-inquiry.html", "General Inquiry", "Reach out to us with any general questions or partnership ideas.")
]

# regex to replace title
title_re = re.compile(r'<title>(.*?)</title>')
# regex to replace h1
h1_re = re.compile(r'<h1 class="text-4xl md:text-6xl font-bold mb-6 tracking-tight".*?>(.*?)</h1>', re.DOTALL)
# regex to replace subtitle
subtitle_re = re.compile(r'<p class="text-xl text-text-secondary-light dark:text-text-secondary-dark max-w-3xl mx-auto">(.*?)</p>', re.DOTALL)
# regex to replace sections
sections_re = re.compile(r'<div class="space-y-16">.*?</div>\n\n</div>\n</section>', re.DOTALL)

for filename, title, description in pages:
    content = template_content
    content = title_re.sub(f"<title>{title} - Near Nerd</title>", content)
    content = h1_re.sub(f'<h1 class="text-4xl md:text-6xl font-bold mb-6 tracking-tight" style="letter-spacing: -0.02em;">{title}</h1>', content)
    content = subtitle_re.sub(f'<p class="text-xl text-text-secondary-light dark:text-text-secondary-dark max-w-3xl mx-auto">{description}</p>', content)
    content = sections_re.sub('</div>\n</section>', content)
    
    filepath = os.path.join("/Users/raj/Documents/GitHub/NN Wesbite/NNwebsite", filename)
    with open(filepath, "w") as f:
        f.write(content)

print(f"Generated {len(pages)} pages.")
