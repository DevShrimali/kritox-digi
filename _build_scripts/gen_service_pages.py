#!/usr/bin/env python3
"""Generate inner service pages from Node.js template."""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(BASE, "tech", "node.html")
OUT_DIR  = os.path.join(BASE, "services")
os.makedirs(OUT_DIR, exist_ok=True)

SERVICES = [
    {
        "slug": "web-development",
        "title": "Web Development Services | Kritox Digital",
        "badge": "Custom Web Solutions",
        "h1_plain": "Web",
        "h1_grad": "Development.",
        "hero_desc": "From pixel-perfect landing pages to complex SaaS platforms, Kritox Digital delivers scalable, high-performance web applications built with modern frameworks and best practices.",
        "hero_img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=1000",
        "stat1_val": "200+", "stat1_label": "Web Projects Delivered",
        "stat2_val": "8+",   "stat2_label": "Years Experience",
        "stat3_val": "98%",  "stat3_label": "Client Satisfaction",
        "stat4_val": "15",   "stat4_label": "Days Risk-Free Trial",
        "section_heading": "Comprehensive Web Development Services",
        "section_desc": "We offer end-to-end web development services — from discovery to deployment — tailored to your business needs.",
        "card1_icon": "layout", "card1_title": "Custom Web Apps",
        "card1_desc": "Tailor-made web applications built from the ground up to align with your business objectives.",
        "card2_icon": "shopping-cart", "card2_title": "E-Commerce Platforms",
        "card2_desc": "Scalable online stores with secure payments and seamless user experiences.",
        "card3_icon": "repeat", "card3_title": "Migration & Revamps",
        "card3_desc": "Modernize legacy systems and outdated websites without data loss or downtime.",
        "expertise_title": "Our Web Development Expertise",
        "expertise_desc": "Our team of senior web developers stay at the cutting edge of modern frameworks — React, Next.js, Node.js, Laravel — to build products that scale.",
        "why_title": "Why Choose Web Development with Kritox?",
        "why_cards": [
            ("Performance", "Sub-second load times with optimized bundles and CDN delivery."),
            ("Scalability", "Architectures designed to grow with your user base effortlessly."),
            ("Security", "OWASP-compliant code with regular audits and penetration testing."),
            ("SEO-Ready", "Semantically structured, fast-loading pages optimized for search."),
        ],
        "hire_cta": "Hire Dedicated Web Developers",
        "faq1_q": "What is your typical timeline for a web project?",
        "faq1_a": "A typical web project MVP takes 4–8 weeks. Enterprise platforms may take 3–6 months depending on scope.",
        "faq2_q": "Do you provide post-launch support?",
        "faq2_a": "Yes, we offer AMC contracts and retainer models for ongoing maintenance and optimization.",
        "faq3_q": "Can I hire a dedicated web development team?",
        "faq3_a": "Absolutely. We offer dedicated team, team-extension, and project-based models to suit your needs.",
    },
    {
        "slug": "mobile-apps",
        "title": "Mobile App Development | Kritox Digital",
        "badge": "iOS & Android Development",
        "h1_plain": "Mobile App",
        "h1_grad": "Development.",
        "hero_desc": "We build native and cross-platform mobile applications for iOS and Android that deliver exceptional user experiences and drive business growth.",
        "hero_img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&q=80&w=1000",
        "stat1_val": "80+", "stat1_label": "Apps Launched",
        "stat2_val": "5+",  "stat2_label": "Years Avg. Experience",
        "stat3_val": "4.8★","stat3_label": "App Store Ratings",
        "stat4_val": "15",  "stat4_label": "Days Risk-Free Trial",
        "section_heading": "Comprehensive Mobile App Services",
        "section_desc": "From concept to App Store listing, we handle the full mobile development lifecycle with agility and precision.",
        "card1_icon": "smartphone", "card1_title": "React Native & Flutter",
        "card1_desc": "Cross-platform apps that share 90% code while delivering a truly native experience on both platforms.",
        "card2_icon": "cpu", "card2_title": "iOS Development",
        "card2_desc": "Swift-powered iOS apps built for performance, security, and Apple HIG compliance.",
        "card3_icon": "layers", "card3_title": "Android Development",
        "card3_desc": "Kotlin-based Android apps optimized for the full spectrum of Android devices.",
        "expertise_title": "Our Mobile Development Expertise",
        "expertise_desc": "Our mobile engineers bring deep expertise in React Native, Flutter, Swift, and Kotlin — delivering apps that users love.",
        "why_title": "Why Build Mobile with Kritox?",
        "why_cards": [
            ("Cross-Platform", "One codebase, two platforms — ship faster without sacrificing quality."),
            ("UI Excellence", "Pixel-perfect designs that follow platform guidelines."),
            ("Performance", "Optimized for 60fps animations and minimal battery drain."),
            ("App Store", "Full submission support for Google Play and Apple App Store."),
        ],
        "hire_cta": "Hire Dedicated Mobile Developers",
        "faq1_q": "How long does it take to build a mobile app?",
        "faq1_a": "A simple mobile app MVP typically takes 6–10 weeks. Feature-rich apps can take 3–5 months.",
        "faq2_q": "Do you support both iOS and Android?",
        "faq2_a": "Yes. We develop native iOS (Swift), native Android (Kotlin), and cross-platform (React Native / Flutter) apps.",
        "faq3_q": "Can I hire a dedicated mobile developer from Kritox?",
        "faq3_a": "Yes, we offer dedicated mobile developer hiring starting from a 2-week trial engagement.",
    },
    {
        "slug": "ui-ux-design",
        "title": "UI/UX Design Services | Kritox Digital",
        "badge": "User-Centered Design",
        "h1_plain": "UI/UX",
        "h1_grad": "Design.",
        "hero_desc": "We craft intuitive, beautiful digital experiences that convert visitors into customers. Our design process is rooted in research, empathy, and business strategy.",
        "hero_img": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&q=80&w=1000",
        "stat1_val": "300+", "stat1_label": "Designs Delivered",
        "stat2_val": "6+",   "stat2_label": "Years Design Experience",
        "stat3_val": "40%",  "stat3_label": "Avg. Conversion Boost",
        "stat4_val": "15",   "stat4_label": "Days Risk-Free Trial",
        "section_heading": "Comprehensive UI/UX Design Services",
        "section_desc": "From wireframes to polished prototypes, we deliver design at every stage of your product journey.",
        "card1_icon": "pen-tool", "card1_title": "Product Design",
        "card1_desc": "End-to-end product design — from research and wireframing to high-fidelity Figma prototypes.",
        "card2_icon": "layout", "card2_title": "Web & App UI",
        "card2_desc": "Visually stunning interfaces built on solid design systems and component libraries.",
        "card3_icon": "users", "card3_title": "UX Research",
        "card3_desc": "User interviews, usability testing, and heatmap analysis to validate every design decision.",
        "expertise_title": "Our UI/UX Design Expertise",
        "expertise_desc": "Our designers work across Figma, Adobe XD, and Framer — combining aesthetic sensibility with data-driven UX thinking.",
        "why_title": "Why Design with Kritox?",
        "why_cards": [
            ("Conversion-Focused", "Every element is designed to guide users toward your key business goals."),
            ("Design Systems", "Scalable component libraries for consistent cross-product experiences."),
            ("Rapid Prototyping", "Interactive Figma prototypes for stakeholder sign-off before development."),
            ("Accessibility", "WCAG 2.1 AA compliant designs for inclusive digital experiences."),
        ],
        "hire_cta": "Hire Dedicated UI/UX Designers",
        "faq1_q": "What design tools do you use?",
        "faq1_a": "We primarily use Figma for UI/UX design, prototyping, and design systems, alongside Adobe tools for branding.",
        "faq2_q": "Do you conduct UX research?",
        "faq2_a": "Yes. We conduct user interviews, card sorting, A/B testing, and heatmap analysis as part of our research process.",
        "faq3_q": "Can I hire a dedicated UI/UX designer?",
        "faq3_a": "Yes — dedicated designer engagements are available on a monthly retainer or project basis.",
    },
    {
        "slug": "digital-marketing",
        "title": "Digital Marketing Services | Kritox Digital",
        "badge": "Growth & SEO Strategy",
        "h1_plain": "Digital",
        "h1_grad": "Marketing.",
        "hero_desc": "Drive measurable growth with Kritox Digital's data-driven marketing services — from SEO and PPC to social media and content strategy.",
        "hero_img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1000",
        "stat1_val": "150+", "stat1_label": "Brands Grown",
        "stat2_val": "3x",   "stat2_label": "Avg. ROI Improvement",
        "stat3_val": "85%",  "stat3_label": "Client Retention Rate",
        "stat4_val": "30",   "stat4_label": "Day Free Audit",
        "section_heading": "Comprehensive Digital Marketing Services",
        "section_desc": "We combine creativity with data to craft campaigns that reach the right people at the right time.",
        "card1_icon": "trending-up", "card1_title": "SEO & Content",
        "card1_desc": "Technical SEO, keyword strategy, and content marketing to dominate organic search results.",
        "card2_icon": "bar-chart-3", "card2_title": "Paid Advertising",
        "card2_desc": "Google Ads, Meta Ads, and LinkedIn campaigns optimized for maximum ROI.",
        "card3_icon": "share-2", "card3_title": "Social Media",
        "card3_desc": "Engaging social content strategies that build brand authority and community.",
        "expertise_title": "Our Digital Marketing Expertise",
        "expertise_desc": "Our growth team combines technical SEO know-how with creative campaign management to drive real business results.",
        "why_title": "Why Market with Kritox?",
        "why_cards": [
            ("Data-Driven", "Every campaign decision is backed by analytics, not guesswork."),
            ("Full Funnel", "From awareness to conversion — we cover the entire customer journey."),
            ("Transparent", "Clear monthly reporting with KPIs that actually matter to your business."),
            ("Agile", "Rapid iterations based on campaign performance data every 2 weeks."),
        ],
        "hire_cta": "Get a Free Marketing Audit",
        "faq1_q": "How long before I see SEO results?",
        "faq1_a": "SEO typically shows meaningful results in 3–6 months. Paid campaigns can drive traffic within days of launch.",
        "faq2_q": "Do you manage paid ad campaigns?",
        "faq2_a": "Yes. We manage Google, Meta, LinkedIn, and programmatic ad campaigns with full transparency.",
        "faq3_q": "Can I hire a dedicated digital marketer?",
        "faq3_a": "Yes — we offer dedicated marketing resource engagements on a monthly retainer basis.",
    },
    {
        "slug": "brand-strategy",
        "title": "Brand Strategy & Identity | Kritox Digital",
        "badge": "Brand Identity & Strategy",
        "h1_plain": "Brand",
        "h1_grad": "Strategy.",
        "hero_desc": "Build a brand that resonates, differentiates, and endures. Kritox Digital crafts compelling brand identities rooted in strategic thinking and visual excellence.",
        "hero_img": "https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?auto=format&fit=crop&q=80&w=1000",
        "stat1_val": "120+", "stat1_label": "Brands Created",
        "stat2_val": "7+",   "stat2_label": "Years Brand Experience",
        "stat3_val": "95%",  "stat3_label": "Client Satisfaction",
        "stat4_val": "14",   "stat4_label": "Day Brand Sprint",
        "section_heading": "Comprehensive Brand Strategy Services",
        "section_desc": "From brand discovery workshops to full visual identity systems, we build brands that tell your story powerfully.",
        "card1_icon": "target", "card1_title": "Brand Positioning",
        "card1_desc": "Define your unique market position, value proposition, and messaging hierarchy.",
        "card2_icon": "pen-tool", "card2_title": "Visual Identity",
        "card2_desc": "Logo design, color palettes, typography, and comprehensive brand style guides.",
        "card3_icon": "book-open", "card3_title": "Brand Guidelines",
        "card3_desc": "Detailed brand standards that ensure consistency across every touchpoint.",
        "expertise_title": "Our Brand Strategy Expertise",
        "expertise_desc": "Our brand strategists and designers collaborate to create identities that are distinctive, consistent, and built to last.",
        "why_title": "Why Brand with Kritox?",
        "why_cards": [
            ("Research-First", "Deep competitor and market analysis before a single pixel is designed."),
            ("Strategic", "Brand decisions are tied directly to your business and growth objectives."),
            ("Consistent", "Every deliverable follows a rigorous QA process for brand coherence."),
            ("Scalable", "Identities designed to work across print, digital, and environmental touchpoints."),
        ],
        "hire_cta": "Start Your Brand Project",
        "faq1_q": "What is included in a brand identity package?",
        "faq1_a": "Logo suite, color palette, typography system, brand voice guidelines, and a comprehensive brand style guide.",
        "faq2_q": "How long does a branding project take?",
        "faq2_a": "A typical brand identity project takes 3–6 weeks from discovery workshop to final delivery.",
        "faq3_q": "Do you help with brand strategy or just visuals?",
        "faq3_a": "Both. We start with positioning strategy, messaging architecture, and then build the visual identity on that foundation.",
    },
    {
        "slug": "cloud-solutions",
        "title": "Cloud Solutions & DevOps | Kritox Digital",
        "badge": "Cloud Infrastructure & DevOps",
        "h1_plain": "Cloud",
        "h1_grad": "Solutions.",
        "hero_desc": "Modernize your infrastructure with Kritox Digital's cloud solutions — AWS, GCP, Azure architecture, DevOps pipelines, and 24/7 managed cloud services.",
        "hero_img": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&q=80&w=1000",
        "stat1_val": "50+", "stat1_label": "Cloud Migrations",
        "stat2_val": "99.9%","stat2_label": "Uptime SLA",
        "stat3_val": "40%", "stat3_label": "Avg. Cost Reduction",
        "stat4_val": "24/7","stat4_label": "Managed Support",
        "section_heading": "Comprehensive Cloud & DevOps Services",
        "section_desc": "From cloud migration to CI/CD automation, we build and manage infrastructure that scales reliably.",
        "card1_icon": "cloud", "card1_title": "Cloud Migration",
        "card1_desc": "Lift-and-shift or re-architect your workloads to AWS, GCP, or Azure with zero downtime.",
        "card2_icon": "git-branch", "card2_title": "CI/CD & DevOps",
        "card2_desc": "Automated build, test, and deployment pipelines with Docker, Kubernetes, and GitHub Actions.",
        "card3_icon": "shield", "card3_title": "Managed Cloud",
        "card3_desc": "24/7 monitoring, cost optimization, and security management for your cloud infrastructure.",
        "expertise_title": "Our Cloud & DevOps Expertise",
        "expertise_desc": "Our certified cloud architects and DevOps engineers have delivered production infrastructure for startups and enterprises alike.",
        "why_title": "Why Cloud with Kritox?",
        "why_cards": [
            ("Certified", "AWS Certified architects with hands-on enterprise cloud experience."),
            ("Cost-Optimized", "FinOps practices that reduce your cloud spend without sacrificing performance."),
            ("Secure", "Zero-trust architecture, IAM policies, and compliance-ready setups."),
            ("Automated", "Infrastructure as Code with Terraform and Pulumi for repeatable deployments."),
        ],
        "hire_cta": "Hire a Cloud Architect",
        "faq1_q": "Which cloud providers do you support?",
        "faq1_a": "We support AWS, Google Cloud Platform, and Microsoft Azure, as well as hybrid and multi-cloud setups.",
        "faq2_q": "Can you help reduce our existing cloud bill?",
        "faq2_a": "Yes. Our FinOps audit typically identifies 20–40% cost savings within the first 30 days.",
        "faq3_q": "Do you offer managed cloud support?",
        "faq3_a": "Yes — 24/7 managed cloud support with defined SLAs is available as a monthly service.",
    },
]

with open(TEMPLATE, "r", encoding="utf-8") as f:
    TMPL = f.read()

def make_page(s):
    html = TMPL

    # Fix all relative paths (../X -> ../X already correct since we're in services/)
    # node.html uses ../ prefix already — services/ is same depth as tech/, so paths are already correct.

    # --- <title> ---
    html = re.sub(r'<title>.*?</title>', f'<title>{s["title"]}</title>', html)

    # --- Badge ---
    html = html.replace("Backend Engineering", s["badge"], 1)

    # --- H1 ---
    html = re.sub(
        r'Node\.js <span class="text-transparent bg-clip-text bg-gradient-to-r from-\[#2F6F73\] to-\[#E5B93C\]">Development\.</span>',
        f'{s["h1_plain"]} <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2F6F73] to-[#E5B93C]">{s["h1_grad"]}</span>',
        html, count=1
    )

    # --- Hero description ---
    html = html.replace(
        "Boost your web app with Kritox Digital's Node.js development services and solutions. Build dynamic and responsive websites with our expert team.",
        s["hero_desc"], 1
    )

    # --- Hero image ---
    html = html.replace(
        "https://images.unsplash.com/photo-1555099962-4199c345e5dd?auto=format&fit=crop&q=80&w=1000",
        s["hero_img"], 1
    )
    html = html.replace('alt="Node.js Development"', f'alt="{s["h1_plain"]} {s["h1_grad"]}"', 1)

    # --- Stats bar ---
    html = re.sub(r'<p class="text-4xl font-black text-\[#E5B93C\] mb-2">10\+</p>',
                  f'<p class="text-4xl font-black text-[#E5B93C] mb-2">{s["stat1_val"]}</p>', html, count=1)
    html = html.replace('<p class="text-white text-sm font-medium">Node.js Experts</p>',
                        f'<p class="text-white text-sm font-medium">{s["stat1_label"]}</p>', 1)
    html = re.sub(r'<p class="text-4xl font-black text-\[#E5B93C\] mb-2">5\+</p>',
                  f'<p class="text-4xl font-black text-[#E5B93C] mb-2">{s["stat2_val"]}</p>', html, count=1)
    html = html.replace('<p class="text-white text-sm font-medium">Years Avg. Experience</p>',
                        f'<p class="text-white text-sm font-medium">{s["stat2_label"]}</p>', 1)
    html = re.sub(r'<p class="text-4xl font-black text-\[#E5B93C\] mb-2">95%</p>',
                  f'<p class="text-4xl font-black text-[#E5B93C] mb-2">{s["stat3_val"]}</p>', html, count=1)
    html = html.replace('<p class="text-white text-sm font-medium">Talent Retention Rate</p>',
                        f'<p class="text-white text-sm font-medium">{s["stat3_label"]}</p>', 1)
    html = html.replace('<p class="text-white text-sm font-medium">Days Risk Free Trial</p>',
                        f'<p class="text-white text-sm font-medium">{s["stat4_label"]}</p>', 1)

    # --- Comprehensive Services section ---
    html = html.replace("Comprehensive Node.js Services", s["section_heading"], 1)
    html = html.replace(
        "We offer end-to-end Node.js development services tailored to your business needs, ensuring high performance, scalability, and security.",
        s["section_desc"], 1
    )

    # Card 1
    html = html.replace('data-lucide="layout" class="w-6 h-6"', f'data-lucide="{s["card1_icon"]}" class="w-6 h-6"', 1)
    html = html.replace("Custom Node.js Development", s["card1_title"], 1)
    html = html.replace(
        "Tailor-made applications built from the ground up to perfectly align with your business objectives and user needs.",
        s["card1_desc"], 1
    )
    # Card 2
    html = html.replace('data-lucide="cpu" class="w-6 h-6"', f'data-lucide="{s["card2_icon"]}" class="w-6 h-6"', 1)
    html = html.replace("Enterprise Solutions", s["card2_title"], 1)
    html = html.replace(
        "Scalable and secure Node.js architectures designed to handle complex workflows and high data volumes.",
        s["card2_desc"], 1
    )
    # Card 3
    html = html.replace('data-lucide="repeat" class="w-6 h-6"', f'data-lucide="{s["card3_icon"]}" class="w-6 h-6"', 1)
    html = html.replace("Migration & Upgrades", s["card3_title"], 1)
    html = html.replace(
        "Seamlessly migrate your legacy systems to Node.js without data loss or significant downtime.",
        s["card3_desc"], 1
    )

    # --- Expertise section ---
    html = html.replace("Our Node.js Expertise", s["expertise_title"], 1)
    html = html.replace(
        "Our team comprises highly skilled Node.js developers who have extensive experience in building complex applications. They stay updated with the latest versions and industry best practices to deliver cutting-edge solutions.",
        s["expertise_desc"], 1
    )

    # --- Why Choose section ---
    html = html.replace("Why Choose Node.js?", s["why_title"], 1)
    why_html = ""
    for title, desc in s["why_cards"]:
        why_html += f'''
                <div class="bg-white p-6 rounded-2xl border border-[#EDEDED]">
                    <h3 class="text-lg font-bold text-[#1F3D5A] mb-2">{title}</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">{desc}</p>
                </div>'''
    html = re.sub(
        r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">).*?(</div>\s*</div>\s*</section>\s*<!-- Versatility)',
        r'\1' + why_html + r'\n            \2',
        html, count=1, flags=re.DOTALL
    )

    # --- Hire CTA ---
    html = html.replace("Hire Dedicated Node.js Developers", s["hire_cta"], 1)

    # --- CTA section heading ---
    html = html.replace(
        "Ready to start your Node.js development project? Or perhaps you have more questions about our services? We're here to help you every step of the way.",
        f"Ready to start your {s['h1_plain']} project? Our experts are here to help you plan, build, and scale.",
        1
    )

    # --- FAQ ---
    html = html.replace("What is your typical project timeline for Node.js?", s["faq1_q"], 1)
    html = html.replace(
        "Our timeline varies depending on the scope of the project. A typical Node.js web application takes 4-8 weeks for an MVP, while complex enterprise systems can take anywhere from 3 to 6 months.",
        s["faq1_a"], 1
    )
    html = html.replace("Do you offer post-launch support and maintenance?", s["faq2_q"], 1)
    html = html.replace(
        "Absolutely. We offer comprehensive AMC (Annual Maintenance Contracts) and retainer models to ensure your Node.js products remain secure, up-to-date, and optimized post-launch.",
        s["faq2_a"], 1
    )
    html = html.replace("Can I hire dedicated Node.js developers from you?", s["faq3_q"], 1)
    html = html.replace(
        "Yes, we offer flexible hiring models including dedicated teams, team extension, and project-based engagements tailored to your exact needs.",
        s["faq3_a"], 1
    )

    # --- Generic "Node.js" references (headings left over) ---
    html = html.replace("Node.js", f'{s["h1_plain"]} {s["h1_grad"].rstrip(".")}')
    html = html.replace("node.html", f'{s["slug"]}.html')

    # --- Ensure main.js is present (template may be missing it) ---
    placeholder = '    <!-- Footer placeholder, will be replaced by actual footer or kept simple here for the script to use existing footer from index -->'
    script_tag = '    <script src="../js/main.js" defer></script>'
    if placeholder in html:
        html = html.replace(placeholder, script_tag)
    elif script_tag not in html:
        html = html.replace('</body>', f'{script_tag}\n</body>', 1)

    return html


for s in SERVICES:
    out_path = os.path.join(OUT_DIR, f'{s["slug"]}.html')
    content = make_page(s)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓  services/{s['slug']}.html")

print("\nAll service pages generated.")
