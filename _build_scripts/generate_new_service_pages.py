import os
import re

# Load Templates
with open('_build_scripts/head_template.html', 'r', encoding='utf-8') as f:
    full_head_template = f.read()

with open('_build_scripts/footer_template.html', 'r', encoding='utf-8') as f:
    footer_content = f.read()

# Extract only the Header part (before the first <section>)
# We also want to keep the <body> tag and Navbar.
header_match = re.search(r'(.*?)<section', full_head_template, re.DOTALL | re.IGNORECASE)
if header_match:
    header_base = header_match.group(1)
else:
    # Fallback if no section found
    header_base = full_head_template

pages_data = {
    "brand-strategy.html": {
        "title": "Brand Strategy",
        "subtitle": "Build a brand that resonates, differentiates, and endures. We craft compelling identities rooted in strategy and excellence.",
        "bg_gradient": "linear-gradient(135deg, #1F3D5A 0%, #2F6F73 100%)",
        "image": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&q=80",
        "experts": "10+",
        "stats": [
            ("award", "10+", "Brand Experts"),
            ("calendar", "5+", "Years Avg Experience"),
            ("target", "95%", "Talent Retention"),
            ("zap", "15 Days", "Risk Free Trial")
        ],
        "services": [
            ("search", "Brand Audit & Research", "Deep dive into your current brand positioning and market perception."),
            ("pen-tool", "Logo & Visual Identity Design", "Creating memorable, scalable logos that represent your core values."),
            ("book-open", "Brand Guidelines Development", "Comprehensive documentation ensuring visual consistency across all channels."),
            ("message-square", "Brand Messaging & Voice", "Developing your unique voice, tone, and core messaging pillars."),
            ("bar-chart", "Market Positioning Strategy", "Strategic analysis to position your brand effectively against competitors."),
            ("rocket", "Brand Launch & Rollout", "Creating cohesive visual languages including typography and color palettes.")
        ],
        "expertise": [
            "Brand Strategy Frameworks", "Competitor Analysis Tools", "Visual Identity Systems",
            "Brand Story Development", "Market Research Methods", "Brand Performance Metrics"
        ],
        "why_choose": [
            ("trending-up", "Increased ROI", "Data-driven strategies that turn brand equity into business revenue."),
            ("zap", "Faster Time to Market", "Agile branding processes that get you launched without compromising quality."),
            ("maximize", "Scalability & Performance", "Systems built to grow with your company from startup to enterprise."),
            ("dollar-sign", "Cost-Effective Solutions", "Premium agency results at highly competitive investment levels.")
        ],
        "versatility": [
            ("shopping-cart", "E-commerce & Retail", "Driving loyalty through emotional brand connections."),
            ("heart", "Healthcare & Medical", "Building trust through professional and caring identity systems."),
            ("shield", "Fintech & Banking", "Establishing authority and security in digital finance."),
            ("book", "Education & E-learning", "Inspiring learners with vibrant, engaging brand identities."),
            ("plane", "Travel & Hospitality", "Capturing the essence of destination and adventure."),
            ("home", "Real Estate", "Professional branding for high-value property development.")
        ],
        "faqs": [
            ("How much does brand strategy cost?", "Our pricing is tailored to your project scale. Contact us for a custom quote."),
            ("How long does brand design take?", "A typical brand strategy and identity project takes 4-8 weeks."),
            ("What is your brand process?", "We follow a 6-step process: Discovery, Research, Strategy, Design, Testing, and Rollout."),
            ("Do you provide ongoing brand support?", "Yes, we offer brand management and evolution services after initial launch."),
            ("Can I see examples of your work?", "Certainly! Explore our portfolio section below for recent success stories."),
            ("What happens after project completion?", "We provide full source files and a comprehensive brand guide for your team.")
        ]
    },
    "cloud-solutions.html": {
        "title": "Cloud Solutions",
        "subtitle": "Scalable, secure, and robust cloud infrastructure to accelerate your digital transformation and global growth.",
        "bg_gradient": "linear-gradient(135deg, #1F3D5A 0%, #15803d 100%)",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80",
        "experts": "15+",
        "stats": [
            ("server", "15+", "Cloud Architects"),
            ("calendar", "6+", "Years Avg Experience"),
            ("shield", "100%", "Security Compliance"),
            ("zap", "15 Days", "Risk Free Trial")
        ],
        "services": [
            ("cloud-lightning", "Cloud Migration Services", "Seamless transition of legacy systems to modern cloud environments."),
            ("settings", "AWS/Azure/GCP Setup", "Expert configuration of major public cloud platforms."),
            ("cpu", "Serverless Architecture", "Building scalable applications without managing infrastructure."),
            ("shield-check", "Cloud Security & Compliance", "Implementing robust security protocols and compliance measures."),
            ("git-branch", "DevOps & CI/CD Pipeline", "Automating deployment pipelines for faster, reliable releases."),
            ("pie-chart", "Cloud Cost Optimization", "Auditing and optimizing cloud spend and performance.")
        ],
        "expertise": [
            "AWS, Azure, Google Cloud Platform", "Kubernetes & Docker", "Terraform & Infrastructure as Code",
            "Jenkins, GitLab CI/CD", "Cloud Security Best Practices", "Multi-Cloud Architecture"
        ],
        "why_choose": [
            ("clock", "99.9% Uptime", "Resilient architectures ensuring your business never sleeps."),
            ("shield", "Military-Grade Security", "Protecting your most sensitive data with advanced encryption."),
            ("maximize", "Infinite Scalability", "Infrastructure that grows instantly with your user base."),
            ("cpu", "Modern DevOps", "Streamlined workflows that accelerate your development cycles.")
        ],
        "versatility": [
            ("shopping-cart", "E-commerce & Retail", "Handling traffic spikes during peak sales effortlessly."),
            ("heart", "Healthcare & Medical", "HIPAA compliant cloud storage for patient records."),
            ("shield", "Fintech & Banking", "PCI DSS compliant infrastructure for payment processing."),
            ("code", "SaaS & Enterprise", "Scalable multi-tenant cloud platforms for global users."),
            ("database", "Big Data", "Processing massive datasets with distributed cloud power."),
            ("settings", "Manufacturing", "IoT cloud integration for real-time factory monitoring.")
        ],
        "faqs": [
            ("Which cloud platform do you use?", "We work with AWS, Azure, and Google Cloud, depending on your needs."),
            ("How long does cloud migration take?", "Small migrations take 2-4 weeks; enterprise shifts can take several months."),
            ("Is my data secure in the cloud?", "Yes, we implement enterprise-grade encryption and security protocols."),
            ("Do you offer 24/7 monitoring?", "Yes, we provide round-the-clock infrastructure monitoring and support."),
            ("Can you help reduce our cloud bills?", "Absolutely. Cost optimization is a core part of our cloud services."),
            ("What is your backup policy?", "We set up automated, geo-redundant backups for maximum data safety.")
        ]
    },
    "digital-marketing.html": {
        "title": "Digital Marketing",
        "subtitle": "Data-driven marketing strategies to increase visibility, drive qualified traffic, and boost your conversion rates.",
        "bg_gradient": "linear-gradient(135deg, #1F3D5A 0%, #7e22ce 100%)",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80",
        "experts": "20+",
        "stats": [
            ("trending-up", "200%", "Avg Traffic Growth"),
            ("calendar", "5+", "Years Avg Experience"),
            ("users", "500+", "Successful Campaigns"),
            ("zap", "15 Days", "Risk Free Trial")
        ],
        "services": [
            ("search", "Search Engine Optimization (SEO)", "Improving organic visibility and ranking on search engines."),
            ("mouse-pointer-2", "Pay-Per-Click Advertising (PPC)", "Targeted Google Ads and Bing Ads campaigns for immediate ROI."),
            ("share-2", "Social Media Marketing (SMM)", "Building brand presence and engagement on social platforms."),
            ("file-text", "Content Marketing Strategy", "Creating valuable content that attracts and converts your target audience."),
            ("mail", "Email Marketing Campaigns", "Personalized outreach that nurtures leads into loyal customers."),
            ("bar-chart-2", "Analytics & Reporting", "Detailed performance tracking and actionable data insights.")
        ],
        "expertise": [
            "Google Analytics & Tag Manager", "SEMrush, Ahrefs, Moz", "Google Ads, Facebook Ads Manager",
            "Hootsuite, Buffer", "HubSpot, Mailchimp", "Data Studio, Tableau"
        ],
        "why_choose": [
            ("target", "Data-Driven Approach", "We base every decision on hard data and user behavior analysis."),
            ("dollar-sign", "Maximizing ROI", "Optimizing every dollar spent to drive the highest possible return."),
            ("eye", "Brand Visibility", "Putting your brand in front of the right people at the right time."),
            ("users", "Customer Engagement", "Building meaningful relationships that lead to long-term loyalty.")
        ],
        "versatility": [
            ("shopping-cart", "E-commerce & Retail", "Driving sales through targeted shopping ads and SEO."),
            ("home", "Real Estate", "Generating high-quality leads for property listings."),
            ("heart", "Healthcare & Medical", "Building authority and trust through medical content."),
            ("briefcase", "B2B SaaS", "Nurturing leads through complex decision-making cycles."),
            ("book", "Education & E-learning", "Reaching prospective students through social and search."),
            ("plane", "Travel & Hospitality", "Capturing intent when users are planning their next trip.")
        ],
        "faqs": [
            ("How long to see SEO results?", "SEO typically takes 3-6 months to show significant organic growth."),
            ("Do you manage ad spend?", "Yes, we handle full campaign management across Google and Social."),
            ("What is your reporting cycle?", "We provide detailed monthly reports with weekly check-ins."),
            ("Can you help with local SEO?", "Yes, we specialize in dominating local search results for businesses."),
            ("Do you create social content?", "Yes, our creative team handles everything from copy to visuals."),
            ("What is your PPC strategy?", "We focus on high-intent keywords and conversion rate optimization.")
        ]
    },
    "mobile-apps.html": {
        "title": "Mobile Apps",
        "subtitle": "Engaging, high-performance native and cross-platform mobile applications that users love and return to.",
        "bg_gradient": "linear-gradient(135deg, #1F3D5A 0%, #0891b2 100%)",
        "image": "https://images.unsplash.com/photo-1512428559087-560552a1d9ab?auto=format&fit=crop&q=80",
        "experts": "15+",
        "stats": [
            ("smartphone", "50+", "Apps Launched"),
            ("calendar", "6+", "Years Avg Experience"),
            ("download", "1M+", "Combined Downloads"),
            ("zap", "15 Days", "Risk Free Trial")
        ],
        "services": [
            ("apple", "Native iOS Development", "High-performance applications built specifically for Apple devices."),
            ("play", "Native Android Development", "Robust Android applications built for the Google ecosystem."),
            ("layers", "Cross-Platform (React Native)", "Efficient cross-platform apps sharing a single codebase."),
            ("smartphone", "Flutter App Development", "Beautiful, natively compiled applications for mobile from DART."),
            ("layout", "Mobile UI/UX Design", "Intuitive, user-centric interfaces designed for touch interaction."),
            ("upload-cloud", "App Store Deployment", "Complete management of store submission and approval processes.")
        ],
        "expertise": [
            "Swift, Objective-C (iOS)", "Kotlin, Java (Android)", "React Native, Flutter",
            "Firebase, AWS Amplify", "REST APIs, GraphQL", "App Store Optimization (ASO)"
        ],
        "why_choose": [
            ("zap", "High Performance", "Butter-smooth animations and rapid load times across all devices."),
            ("smile", "Engaging UX", "Interfaces that users love to spend time in and return to."),
            ("shield", "Secure Architecture", "Protecting user data with industry-leading security practices."),
            ("refresh-cw", "Ongoing Support", "Regular updates to ensure compatibility with latest OS versions.")
        ],
        "versatility": [
            ("shopping-cart", "E-commerce & Retail", "Providing seamless mobile shopping experiences."),
            ("heart", "Healthcare & Medical", "Patient monitoring and health tracking applications."),
            ("shield", "Fintech & Banking", "Secure mobile banking and investment platforms."),
            ("music", "Entertainment", "Rich media streaming and social interaction apps."),
            ("zap", "On-Demand Services", "Real-time tracking and delivery service applications."),
            ("book", "Education & E-learning", "Interactive learning and student management tools.")
        ],
        "faqs": [
            ("iOS or Android first?", "We analyze your target audience to decide which platform to launch first."),
            ("How long to build an app?", "An MVP typically takes 3-4 months; complex apps take 6+ months."),
            ("Do you do app design?", "Yes, we handle the entire process from wireframing to final UI."),
            ("Will you submit to stores?", "Yes, we handle the entire App Store and Play Store submission."),
            ("Do you support the app later?", "Yes, we offer maintenance plans for OS updates and bug fixes."),
            ("Can you update old apps?", "Yes, we can refactor and modernize existing mobile applications.")
        ]
    },
    "ui-ux-design.html": {
        "title": "UI/UX Design",
        "subtitle": "Intuitive, user-centric designs that elevate digital products and drive massive engagement.",
        "bg_gradient": "linear-gradient(135deg, #1F3D5A 0%, #db2777 100%)",
        "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&q=80",
        "experts": "12+",
        "stats": [
            ("pen-tool", "12+", "Design Experts"),
            ("calendar", "5+", "Years Avg Experience"),
            ("heart", "98%", "User Satisfaction"),
            ("zap", "15 Days", "Risk Free Trial")
        ],
        "services": [
            ("users", "User Research & Testing", "Understanding behavior and needs through deep data analysis."),
            ("map", "Information Architecture", "Structuring content for intuitive and logical navigation."),
            ("layout", "Wireframing & Prototyping", "Building functional blueprints and interactive design models."),
            ("palette", "Visual UI Design", "Crafting stunning, pixel-perfect interfaces that align with your brand."),
            ("box", "Design System Creation", "Developing scalable component libraries for design consistency."),
            ("monitor", "Responsive Web Design", "Ensuring flawless appearance across every possible screen size.")
        ],
        "expertise": [
            "Figma, Sketch, Adobe XD", "User Testing Tools", "A/B Testing Platforms",
            "Analytics & Heatmaps", "Design Systems (Atomic Design)", "Accessibility (WCAG 2.1)"
        ],
        "why_choose": [
            ("smile", "User-Centric", "We place your users at the heart of every design decision."),
            ("zap", "Conversion Focus", "Optimizing flows to turn users into loyal customers."),
            ("eye", "Visual Excellence", "Creating designs that 'wow' and feel premium at first glance."),
            ("refresh-cw", "Iterative Process", "Continuous improvement based on real-world user feedback.")
        ],
        "versatility": [
            ("shopping-cart", "E-commerce & Retail", "Optimizing checkout flows to reduce cart abandonment."),
            ("layout", "SaaS & Enterprise", "Simplifying complex data into intuitive, usable dashboards."),
            ("smartphone", "Mobile Apps", "Micro-interactions and thumb-friendly mobile layouts."),
            ("heart", "Healthcare & Medical", "Clear, accessible interfaces for patient-focused applications."),
            ("shield", "Fintech & Banking", "Trust-building designs for sensitive financial transactions."),
            ("book", "Education & E-learning", "Engaging, focused layouts for e-learning environments.")
        ],
        "faqs": [
            ("What is your design process?", "We follow: Research, Ideate, Prototype, Test, and Refine."),
            ("Do you use Figma?", "Yes, Figma is our primary tool for collaboration and design."),
            ("Can you do a UX Audit?", "Yes, we can analyze your current product to find friction points."),
            ("How long is the design phase?", "UI/UX for a standard product takes about 4-6 weeks."),
            ("Is design included in dev?", "We offer both standalone design and integrated design/dev."),
            ("Do you handle accessibility?", "Yes, we design for WCAG 2.1 compliance as a standard practice.")
        ]
    },
    "web-development.html": {
        "title": "Web Development",
        "subtitle": "Scalable, secure, and high-performance web applications built for modern businesses and complex challenges.",
        "bg_gradient": "linear-gradient(135deg, #1F3D5A 0%, #ea580c 100%)",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80",
        "experts": "30+",
        "stats": [
            ("code", "30+", "Web Developers"),
            ("calendar", "5+", "Years Avg Experience"),
            ("globe", "200+", "Websites Launched"),
            ("zap", "15 Days", "Risk Free Trial")
        ],
        "services": [
            ("code", "Custom Website Development", "Tailor-made web solutions built for your specific business needs."),
            ("shopping-bag", "E-commerce Solutions", "Powerful online stores that drive sales and handle growth."),
            ("layers", "Web Application Development", "Complex, feature-rich apps that live in the browser."),
            ("layout-template", "CMS Development", "Manage your content easily with WordPress, Strapi, or custom CMS."),
            ("zap", "Progressive Web Apps (PWA)", "Websites that feel and act like native mobile applications."),
            ("plug", "API Integration & Development", "Connecting your web apps to the services your business uses.")
        ],
        "expertise": [
            "React.js, Vue.js, Angular", "Node.js, Python, PHP", "MongoDB, PostgreSQL, MySQL",
            "AWS, Vercel, Netlify", "Git, GitHub/GitLab", "RESTful APIs, GraphQL"
        ],
        "why_choose": [
            ("zap", "High Performance", "Lightning-fast load times for better SEO and user experience."),
            ("shield-check", "Secure & Robust", "Enterprise-grade security protecting your business and users."),
            ("maximize", "Scalable Tech", "Stack choices that ensure your site grows with your traffic."),
            ("check-circle", "Future-Proof", "Clean, maintainable code using the latest industry standards.")
        ],
        "versatility": [
            ("shopping-cart", "E-commerce & Retail", "High-conversion storefronts with seamless payment flows."),
            ("home", "Real Estate", "Feature-rich portals with map searches and listing filters."),
            ("heart", "Healthcare & Medical", "Patient portals and appointment scheduling systems."),
            ("book", "Education & E-learning", "LMS platforms with video courses and assessments."),
            ("briefcase", "Corporate", "Professional presence websites that build brand authority."),
            ("code", "SaaS & Enterprise", "Internal tools and customer-facing cloud applications.")
        ],
        "faqs": [
            ("Which tech stack is best?", "We choose the stack (MERN, Python, etc) based on your requirements."),
            ("How long to build a site?", "Standard sites take 4-6 weeks; complex apps take 3-6 months."),
            ("Will it be mobile-friendly?", "Absolutely. We build for mobile-first responsiveness."),
            ("Do you offer SEO help?", "Yes, we ensure all sites are built with SEO best practices."),
            ("Can you maintain our site?", "Yes, we offer monthly maintenance and security packages."),
            ("Do you build on WordPress?", "Yes, we specialize in custom, high-performance WordPress sites.")
        ]
    }
}

def generate_page(filename, data):
    # Fix Head: Update Title and use only the sliced Header
    page_head = header_base.replace('<title>Brand Strategy & Identity | Kritox Digital</title>', f'<title>{data["title"]} Services | Kritox Digital</title>')

    # Breadcrumbs
    breadcrumb = f'''
    <nav class="flex mb-8" aria-label="Breadcrumb">
        <ol class="inline-flex items-center space-x-1 md:space-x-3">
            <li class="inline-flex items-center">
                <a href="../index.html" class="inline-flex items-center text-sm font-medium text-white/70 hover:text-white transition-colors">
                    <i data-lucide="home" class="w-4 h-4 mr-2"></i> Home
                </a>
            </li>
            <li>
                <div class="flex items-center">
                    <i data-lucide="chevron-right" class="w-4 h-4 text-white/40"></i>
                    <a href="../services.html" class="ml-1 text-sm font-medium text-white/70 hover:text-white transition-colors md:ml-2">Services</a>
                </div>
            </li>
            <li aria-current="page">
                <div class="flex items-center">
                    <i data-lucide="chevron-right" class="w-4 h-4 text-white/40"></i>
                    <span class="ml-1 text-sm font-medium text-[#E5B93C] md:ml-2">{data["title"]}</span>
                </div>
            </li>
        </ol>
    </nav>
    '''

    # SECTION 1: BANNER
    section1 = f'''
    <section class="relative pt-32 pb-24 md:pt-40 md:pb-32 overflow-hidden" style="background: {data["bg_gradient"]};">
        <div class="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div class="text-white">
                    {breadcrumb}
                    <h1 class="font-black tracking-tight leading-[1.05] mb-6 text-[2.5rem] md:text-[3.5rem]">
                        {data["title"]} <span class="text-[#E5B93C]">Services.</span>
                    </h1>
                    <p class="text-xl text-white/80 leading-relaxed mb-10 max-w-xl">
                        {data["subtitle"]}
                    </p>
                    <div class="flex flex-wrap items-center gap-6">
                        <a href="../contact.html" class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] bg-[#E5B93C] px-8 py-4 rounded-xl hover:bg-white transition-all transform hover:-translate-y-1 shadow-lg shadow-[#E5B93C]/20">
                            Get Free Quote <i data-lucide="arrow-right" class="w-5 h-5"></i>
                        </a>
                        <div class="flex items-center gap-4">
                            <div class="flex text-[#E5B93C]">
                                <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                                <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                                <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                                <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                                <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                            </div>
                            <div class="text-sm">
                                <span class="font-black block text-lg">4.9/5</span>
                                <span class="text-white/60">(128 reviews)</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="relative group">
                    <div class="absolute -inset-4 bg-white/10 rounded-[2.5rem] blur-xl opacity-50 group-hover:opacity-75 transition-opacity"></div>
                    <img src="{data["image"]}" alt="{data["title"]}" class="relative rounded-[2rem] shadow-2xl w-full h-[450px] md:h-[550px] object-cover border border-white/10">
                </div>
            </div>
        </div>
    </section>
    '''

    # SECTION 2: STATS BAR
    section2 = f'''
    <section class="bg-[#1F3D5A] py-8 border-y border-white/5 relative z-20">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6 items-center">
    '''
    for icon, val, lbl in data["stats"]:
        section2 += f'''
                <div class="flex items-center justify-center gap-4 text-white border-r border-white/10 last:border-0 px-4">
                    <div class="w-12 h-12 bg-white/5 rounded-xl flex items-center justify-center text-[#E5B93C]">
                        <i data-lucide="{icon}" class="w-6 h-6"></i>
                    </div>
                    <div class="text-left">
                        <p class="text-2xl font-black">{val}</p>
                        <p class="text-[12px] text-white/50 uppercase tracking-widest font-bold">{lbl}</p>
                    </div>
                </div>
        '''
    section2 += '''
            </div>
        </div>
    </section>
    '''

    # SECTION 3: COMPREHENSIVE SERVICES
    section3 = f'''
    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Comprehensive <span class="text-[#2F6F73]">{data["title"]}</span> Services</h2>
                <p class="text-lg text-[#4A4A4A]">End-to-end solutions designed to scale your business and outpace the competition.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    '''
    for icon, title, desc in data["services"]:
        section3 += f'''
                <div class="bg-[#FAFAFA] p-8 rounded-3xl border border-[#EDEDED] hover:border-[#2F6F73] hover:shadow-xl transition-all group">
                    <div class="w-14 h-14 bg-white border border-[#EDEDED] rounded-2xl flex items-center justify-center text-[#2F6F73] mb-6 group-hover:bg-[#2F6F73] group-hover:text-white transition-all shadow-sm">
                        <i data-lucide="{icon}" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-3">{title}</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed mb-6">{desc}</p>
                    <a href="../contact.html" class="inline-flex items-center gap-2 text-sm font-bold text-[#2F6F73] hover:gap-3 transition-all">Learn More <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                </div>
        '''
    section3 += '''
            </div>
        </div>
    </section>
    '''

    # SECTION 4: EXPERTISE
    section4 = f'''
    <section class="py-24 bg-[#FAFAFA] border-y border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div>
                    <h2 class="text-3xl md:text-4xl font-black text-[#1F3D5A] mb-6">Our {data["title"]} Expertise</h2>
                    <p class="text-lg text-[#4A4A4A] mb-10 leading-relaxed">We leverage industry-leading tools and deep domain knowledge to deliver exceptional results.</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
    '''
    for exp in data["expertise"]:
        section4 += f'''
                        <div class="flex items-center gap-3">
                            <div class="w-6 h-6 rounded-full bg-[#2F6F73]/10 text-[#2F6F73] flex items-center justify-center shrink-0">
                                <i data-lucide="check" class="w-4 h-4"></i>
                            </div>
                            <span class="font-bold text-[#1F3D5A] text-sm">{exp}</span>
                        </div>
        '''
    section4 += f'''
                    </div>
                </div>
                <div class="bg-white p-2 rounded-[2.5rem] shadow-2xl overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&q=80" class="rounded-[2.4rem] w-full h-[400px] object-cover" alt="Expertise">
                </div>
            </div>
        </div>
    </section>
    '''

    # SECTION 5: WHY CHOOSE
    section5 = f'''
    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-16 text-center">Why Choose <span class="text-[#2F6F73]">{data["title"]}</span></h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
    '''
    for icon, title, desc in data["why_choose"]:
        section5 += f'''
                <div class="text-center p-6 group">
                    <div class="w-20 h-20 bg-[#FAFAFA] rounded-3xl flex items-center justify-center text-[#E5B93C] mx-auto mb-6 shadow-inner group-hover:bg-[#1F3D5A] group-hover:text-white transition-all">
                        <i data-lucide="{icon}" class="w-10 h-10"></i>
                    </div>
                    <h3 class="text-lg font-bold text-[#1F3D5A] mb-3">{title}</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">{desc}</p>
                </div>
        '''
    section5 += '''
            </div>
        </div>
    </section>
    '''

    # SECTION 6: VERSATILITY
    section6 = f'''
    <section class="py-24 bg-[#1F3D5A] text-white overflow-hidden relative">
        <div class="absolute top-0 left-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-10"></div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <h2 class="text-3xl md:text-5xl font-black mb-16 text-center">{data["title"]} Versatility Across Industries</h2>
            <div class="grid grid-cols-2 lg:grid-cols-3 gap-6">
    '''
    for icon, name, use in data["versatility"]:
        section6 += f'''
                <div class="bg-white/5 border border-white/10 rounded-2xl p-8 hover:bg-white/10 transition-colors">
                    <div class="w-12 h-12 bg-[#E5B93C]/20 text-[#E5B93C] rounded-xl flex items-center justify-center mb-6">
                        <i data-lucide="{icon}" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">{name}</h3>
                    <p class="text-white/60 text-sm leading-relaxed">{use}</p>
                </div>
        '''
    section6 += '''
            </div>
        </div>
    </section>
    '''

    # SECTION 7: PROCESS
    section7 = f'''
    <section class="py-24 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-16 text-center">Our {data["title"]} Development Process</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-8 relative">
                <div class="hidden lg:block absolute top-12 left-10 right-10 h-0.5 bg-[#EDEDED] z-0"></div>
                <div class="relative z-10 text-center">
                    <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-[#1F3D5A] mx-auto mb-4 shadow-xl border-4 border-[#FAFAFA]">1</div>
                    <h4 class="font-bold text-[#1F3D5A] mb-1">Discovery</h4>
                    <p class="text-[12px] text-[#4A4A4A]">Audit & Research</p>
                </div>
                <div class="relative z-10 text-center">
                    <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-[#1F3D5A] mx-auto mb-4 shadow-xl border-4 border-[#FAFAFA]">2</div>
                    <h4 class="font-bold text-[#1F3D5A] mb-1">Strategy</h4>
                    <p class="text-[12px] text-[#4A4A4A]">Roadmap Design</p>
                </div>
                <div class="relative z-10 text-center">
                    <div class="w-16 h-16 bg-[#1F3D5A] text-white rounded-full flex items-center justify-center mx-auto mb-4 shadow-xl border-4 border-[#FAFAFA]">3</div>
                    <h4 class="font-bold text-[#1F3D5A] mb-1">Development</h4>
                    <p class="text-[12px] text-[#4A4A4A]">Execution Phase</p>
                </div>
                <div class="relative z-10 text-center">
                    <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-[#1F3D5A] mx-auto mb-4 shadow-xl border-4 border-[#FAFAFA]">4</div>
                    <h4 class="font-bold text-[#1F3D5A] mb-1">Testing</h4>
                    <p class="text-[12px] text-[#4A4A4A]">Quality Assurance</p>
                </div>
                <div class="relative z-10 text-center">
                    <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-[#1F3D5A] mx-auto mb-4 shadow-xl border-4 border-[#FAFAFA]">5</div>
                    <h4 class="font-bold text-[#1F3D5A] mb-1">Launch</h4>
                    <p class="text-[12px] text-[#4A4A4A]">Deployment</p>
                </div>
                <div class="relative z-10 text-center">
                    <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-[#1F3D5A] mx-auto mb-4 shadow-xl border-4 border-[#FAFAFA]">6</div>
                    <h4 class="font-bold text-[#1F3D5A] mb-1">Support</h4>
                    <p class="text-[12px] text-[#4A4A4A]">Post-Launch Care</p>
                </div>
            </div>
        </div>
    </section>
    '''

    # SECTION 8: WHY KRITOX
    section8 = f'''
    <section class="py-24 bg-white border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-16 text-center">Why Choose Kritox Digital for {data["title"]} Development</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 max-w-4xl mx-auto">
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">Certified Experts</span>
                </div>
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">5+ Years Average Experience</span>
                </div>
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">95% Client Retention Rate</span>
                </div>
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">Agile Development Methodology</span>
                </div>
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">Transparent Communication</span>
                </div>
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">On-Time Delivery Guarantee</span>
                </div>
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">NDA & IP Protection</span>
                </div>
                <div class="flex items-center gap-4 py-4 border-b border-[#EDEDED]">
                    <i data-lucide="check-circle" class="text-[#2F6F73] w-6 h-6"></i>
                    <span class="font-bold text-[#1F3D5A]">Post-Launch Support</span>
                </div>
            </div>
        </div>
    </section>
    '''

    # SECTION 9: INDUSTRIES SERVE (INNER VARIANT)
    section9 = f'''
    <section class="py-24 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-4xl font-black text-[#1F3D5A] mb-12 text-center">Industries We Serve</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-8 gap-4">
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="shopping-cart" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">E-commerce</p>
                </div>
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="heart-pulse" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">Healthcare</p>
                </div>
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="landmark" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">Fintech</p>
                </div>
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="graduation-cap" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">Education</p>
                </div>
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="plane" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">Travel</p>
                </div>
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="building-2" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">Real Estate</p>
                </div>
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="box" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">SaaS</p>
                </div>
                <div class="bg-white p-4 rounded-xl border border-[#EDEDED] text-center hover:border-[#2F6F73] transition-colors group">
                    <i data-lucide="truck" class="w-6 h-6 mx-auto mb-2 text-[#2F6F73]"></i>
                    <p class="text-[10px] font-black uppercase text-[#1F3D5A]">Logistics</p>
                </div>
            </div>
        </div>
    </section>
    '''

    # SECTION 10: PORTFOLIO (INNER VARIANT)
    section10 = f'''
    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-16 text-center">Our {data["title"]} Portfolio</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
                <div class="group border border-[#EDEDED] rounded-3xl overflow-hidden hover:shadow-2xl transition-all">
                    <div class="h-64 overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
                        <div class="absolute top-4 left-4 flex gap-2">
                             <span class="px-3 py-1 bg-white/90 backdrop-blur-sm rounded-full text-[10px] font-black text-[#1F3D5A] uppercase">Featured</span>
                        </div>
                    </div>
                    <div class="p-8">
                        <h3 class="text-2xl font-bold text-[#1F3D5A] mb-2">Technical Excellence</h3>
                        <p class="text-sm text-[#4A4A4A] mb-4">Scalable architecture and seamless user experience implementation.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="px-3 py-1 bg-[#FAFAFA] border border-[#EDEDED] rounded-full text-[10px] font-black text-[#4A4A4A] uppercase">Performance</span>
                            <span class="px-3 py-1 bg-[#FAFAFA] border border-[#EDEDED] rounded-full text-[10px] font-black text-[#4A4A4A] uppercase">Security</span>
                            <span class="px-3 py-1 bg-[#FAFAFA] border border-[#EDEDED] rounded-full text-[10px] font-black text-[#4A4A4A] uppercase">Scale</span>
                        </div>
                        <a href="../contact.html" class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] group-hover:text-[#2F6F73] transition-colors">View Case Study <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                    </div>
                </div>
                <div class="group border border-[#EDEDED] rounded-3xl overflow-hidden hover:shadow-2xl transition-all">
                    <div class="h-64 overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
                        <div class="absolute top-4 left-4 flex gap-2">
                             <span class="px-3 py-1 bg-white/90 backdrop-blur-sm rounded-full text-[10px] font-black text-[#1F3D5A] uppercase">Success Story</span>
                        </div>
                    </div>
                    <div class="p-8">
                        <h3 class="text-2xl font-bold text-[#1F3D5A] mb-2">Modern Solutions</h3>
                        <p class="text-sm text-[#4A4A4A] mb-4">Empowering industry leaders with robust digital tools.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="px-3 py-1 bg-[#FAFAFA] border border-[#EDEDED] rounded-full text-[10px] font-black text-[#4A4A4A] uppercase">Integration</span>
                            <span class="px-3 py-1 bg-[#FAFAFA] border border-[#EDEDED] rounded-full text-[10px] font-black text-[#4A4A4A] uppercase">Cloud</span>
                            <span class="px-3 py-1 bg-[#FAFAFA] border border-[#EDEDED] rounded-full text-[10px] font-black text-[#4A4A4A] uppercase">Mobile</span>
                        </div>
                        <a href="../contact.html" class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] group-hover:text-[#2F6F73] transition-colors">View Case Study <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

    # SECTION 11: TESTIMONIALS (INNER VARIANT)
    section11 = f'''
    <section class="py-24 bg-[#FAFAFA] border-y border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-16 text-center">What Our Clients Say</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-white p-8 rounded-2xl border border-[#EDEDED] shadow-sm flex flex-col h-full">
                    <div class="flex text-[#E5B93C] mb-4">
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i>
                    </div>
                    <p class="text-[#4A4A4A] text-[15px] italic leading-relaxed mb-8 flex-grow">"Kritox delivered our {data["title"]} project with exceptional speed and quality. Their team is truly top-tier."</p>
                    <div class="flex items-center gap-4 border-t border-[#EDEDED] pt-6">
                        <div class="w-10 h-10 rounded-full bg-[#1F3D5A] text-white flex items-center justify-center font-bold">JD</div>
                        <div>
                            <p class="font-bold text-[#1F3D5A] text-sm">John Doe</p>
                            <p class="text-[12px] text-[#4A4A4A]">CTO, TechCorp</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-2xl border border-[#EDEDED] shadow-sm flex flex-col h-full">
                    <div class="flex text-[#E5B93C] mb-4">
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i>
                    </div>
                    <p class="text-[#4A4A4A] text-[15px] italic leading-relaxed mb-8 flex-grow">"Professional, transparent, and results-oriented. The ROI from this engagement was clear from day one."</p>
                    <div class="flex items-center gap-4 border-t border-[#EDEDED] pt-6">
                        <div class="w-10 h-10 rounded-full bg-[#2F6F73] text-white flex items-center justify-center font-bold">AS</div>
                        <div>
                            <p class="font-bold text-[#1F3D5A] text-sm">Alice Smith</p>
                            <p class="text-[12px] text-[#4A4A4A]">Founder, RetailGlobal</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-2xl border border-[#EDEDED] shadow-sm flex flex-col h-full">
                    <div class="flex text-[#E5B93C] mb-4">
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i><i data-lucide="star" class="w-4 h-4 fill-current"></i>
                    </div>
                    <p class="text-[#4A4A4A] text-[15px] italic leading-relaxed mb-8 flex-grow">"The best {data["title"]} partner we have worked with. Their attention to detail is remarkable."</p>
                    <div class="flex items-center gap-4 border-t border-[#EDEDED] pt-6">
                        <div class="w-10 h-10 rounded-full bg-[#E5B93C] text-white flex items-center justify-center font-bold">RK</div>
                        <div>
                            <p class="font-bold text-[#1F3D5A] text-sm">Robert King</p>
                            <p class="text-[12px] text-[#4A4A4A]">PM, InnovateSoft</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

    # SECTION 12: CLIENT LOGOS (INNER VARIANT)
    section12 = f'''
    <section class="py-16 bg-white overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-2xl font-black text-[#1F3D5A] mb-12 text-center opacity-30 tracking-[0.3em] uppercase">Trusted By Leading Brands</h2>
            <div class="flex flex-wrap justify-center items-center gap-12 grayscale opacity-50">
                <img src="../assets/client logo/hello healthy.png" class="h-8 object-contain hover:grayscale-0 hover:opacity-100 transition-all cursor-pointer">
                <img src="../assets/client logo/HP Logo(PantoneU) copy.png" class="h-8 object-contain hover:grayscale-0 hover:opacity-100 transition-all cursor-pointer">
                <img src="../assets/client logo/Stern-logo-blue.png" class="h-8 object-contain hover:grayscale-0 hover:opacity-100 transition-all cursor-pointer">
                <img src="../assets/client logo/logo-skedulo-navy.svg" class="h-8 object-contain hover:grayscale-0 hover:opacity-100 transition-all cursor-pointer">
                <img src="../assets/client logo/smarteinc.png" class="h-8 object-contain hover:grayscale-0 hover:opacity-100 transition-all cursor-pointer">
                <img src="../assets/client logo/KBOnline.png" class="h-8 object-contain hover:grayscale-0 hover:opacity-100 transition-all cursor-pointer">
            </div>
        </div>
    </section>
    '''

    # SECTION 13: FAQs
    section13 = f'''
    <section class="py-24 bg-[#FAFAFA]">
        <div class="max-w-4xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-12 text-center">Frequently Asked Questions</h2>
            <div class="faq-content-pane space-y-4">
    '''
    for q, a in data["faqs"]:
        section13 += f'''
                <div class="bg-white border border-[#EDEDED] rounded-2xl p-6 lg:p-8 hover:border-[#2F6F73] transition-colors group cursor-pointer">
                    <div class="flex justify-between items-center">
                        <h3 class="text-lg font-bold text-[#1F3D5A] pr-4">{q}</h3>
                        <div class="w-8 h-8 shrink-0 rounded-full bg-[#FAFAFA] border border-[#EDEDED] flex items-center justify-center text-[#1F3D5A] group-hover:bg-[#2F6F73] group-hover:text-white transition-colors">
                            <i data-lucide="plus" class="w-4 h-4"></i>
                        </div>
                    </div>
                    <p class="text-[#4A4A4A] mt-4 text-[15px] leading-relaxed hidden">
                        {a}
                    </p>
                </div>
        '''
    section13 += '''
            </div>
        </div>
    </section>
    '''

    # SECTION 14: CTA
    section14 = f'''
    <section class="py-24 bg-[#1F3D5A] relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-r from-[#1F3D5A] via-[#2F6F73]/20 to-[#1F3D5A] z-0"></div>
        <div class="max-w-4xl mx-auto px-6 md:px-10 text-center relative z-10">
            <h2 class="text-4xl md:text-6xl font-black text-white mb-6">Have a Great Idea? <br/><span class="text-[#E5B93C]">Tell us about it.</span></h2>
            <p class="text-white/70 text-lg md:text-xl mb-12">Let\'s discuss your project and turn your ideas into a robust digital reality.</p>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
                <a href="../contact.html" class="w-full sm:w-auto px-10 py-5 bg-[#E5B93C] text-[#1F3D5A] font-black rounded-2xl hover:bg-white transition-colors">Schedule Free Consultation</a>
                <a href="../contact.html" class="w-full sm:w-auto px-10 py-5 bg-transparent border-2 border-white text-white font-black rounded-2xl hover:bg-white/10 transition-colors">Request Project Quote</a>
            </div>
        </div>
    </section>
    '''

    full_html = page_head + section1 + section2 + section3 + section4 + section5 + section6 + section7 + section8 + section9 + section10 + section11 + section12 + section13 + section14 + footer_content
    
    with open(f'services/{filename}', 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Built {filename}")

for filename, data in pages_data.items():
    generate_page(filename, data)

