import re
import os

pages_data = {
    "brand-strategy.html": {
        "title": "Brand Strategy Services",
        "short_title": "Brand Strategy",
        "subtitle": "Crafting compelling brand identities rooted in strategic thinking and visual excellence.",
        "image": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&q=80",
        "experts": "10+ Brand Experts",
        "icon": "pen-tool",
        "services": [
            ("Brand Audit", "Deep dive into your current brand positioning and market perception."),
            ("Logo Design", "Creating memorable, scalable logos that represent your core values."),
            ("Brand Guidelines", "Comprehensive documentation ensuring visual consistency across all channels."),
            ("Messaging", "Developing your unique voice, tone, and core messaging pillars."),
            ("Market Positioning", "Strategic analysis to position your brand effectively against competitors."),
            ("Visual Systems", "Creating cohesive visual languages including typography and color palettes.")
        ],
        "expertise": [
            ("Brand Research", "In-depth market and audience analysis."),
            ("Competitor Analysis", "Identifying gaps and opportunities in your competitive landscape."),
            ("Storytelling", "Crafting narratives that connect emotionally with your audience.")
        ],
        "why_choose": [
            ("Strategic Foundation", "We don't just design; we build strategies that drive business growth."),
            ("Market Differentiation", "Stand out in crowded markets with a unique, compelling identity."),
            ("Consistency", "Ensure every touchpoint reflects your brand's true essence.")
        ],
        "versatility": [
            ("Startups", "Building foundational brands from the ground up for early-stage companies."),
            ("Enterprise Rebranding", "Modernizing legacy brands while preserving their core equity."),
            ("Product Launches", "Creating impactful identities for new product lines and sub-brands.")
        ],
        "faqs": [
            ("What is included in a brand strategy?", "A comprehensive brand strategy includes audience research, competitive analysis, brand positioning, voice and tone guidelines, and a visual identity system."),
            ("How long does a rebranding process take?", "Typically, a full rebrand takes 6 to 12 weeks depending on the size of the organization and the complexity of the deliverables."),
            ("Do you provide brand guidelines?", "Yes, we deliver detailed brand guidelines covering logo usage, typography, color palettes, and photography styles.")
        ]
    },
    "cloud-solutions.html": {
        "title": "Cloud Solutions Services",
        "short_title": "Cloud Solutions",
        "subtitle": "Scalable, secure, and robust cloud infrastructure to accelerate your digital transformation.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80",
        "experts": "15+ Cloud Architects",
        "icon": "cloud",
        "services": [
            ("AWS/Azure/GCP Setup", "Expert configuration of major public cloud platforms."),
            ("Cloud Migration", "Seamless transition of legacy systems to modern cloud environments."),
            ("Serverless Architecture", "Building scalable applications without managing infrastructure."),
            ("Cloud Optimization", "Auditing and optimizing cloud spend and performance."),
            ("DevOps & CI/CD", "Automating deployment pipelines for faster, reliable releases."),
            ("Cloud Security", "Implementing robust security protocols and compliance measures.")
        ],
        "expertise": [
            ("Multi-cloud Architecture", "Designing resilient systems across multiple cloud providers."),
            ("Kubernetes", "Container orchestration for highly scalable microservices."),
            ("Infrastructure as Code", "Managing infrastructure via Terraform and CloudFormation.")
        ],
        "why_choose": [
            ("Scalability", "Infrastructure that grows seamlessly with your business demands."),
            ("Cost Efficiency", "Optimized resource allocation to minimize unnecessary cloud spend."),
            ("High Availability", "Resilient architectures ensuring maximum uptime and reliability.")
        ],
        "versatility": [
            ("SaaS", "Scalable multi-tenant architectures for growing software platforms."),
            ("Fintech", "Highly secure, compliant infrastructure for financial applications."),
            ("Healthcare", "HIPAA-compliant cloud solutions protecting sensitive patient data.")
        ],
        "faqs": [
            ("Which cloud platform do you recommend?", "We are cloud-agnostic and recommend AWS, Azure, or GCP based on your specific technical requirements, existing stack, and budget."),
            ("How do you ensure cloud security?", "We implement zero-trust architectures, end-to-end encryption, regular vulnerability assessments, and strict identity access management (IAM)."),
            ("Can you migrate our existing app with zero downtime?", "Yes, we utilize blue-green deployments and careful database syncing to ensure migrations happen with near-zero downtime.")
        ]
    },
    "digital-marketing.html": {
        "title": "Digital Marketing Services",
        "short_title": "Digital Marketing",
        "subtitle": "Data-driven marketing strategies to increase visibility, drive traffic, and boost conversions.",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80",
        "experts": "20+ Marketing Experts",
        "icon": "trending-up",
        "services": [
            ("Search Engine Optimization (SEO)", "Improving organic visibility and ranking on search engines."),
            ("Pay-Per-Click (PPC)", "Targeted Google Ads and Bing Ads campaigns for immediate ROI."),
            ("Social Media Optimization (SMO)", "Building brand presence and engagement on social platforms."),
            ("Content Marketing", "Creating valuable content that attracts and converts your target audience."),
            ("Conversion Rate Optimization", "Analyzing user behavior to improve website conversion rates."),
            ("Analytics & Reporting", "Detailed performance tracking and actionable data insights.")
        ],
        "expertise": [
            ("Keyword Research", "Identifying high-intent search terms to drive qualified traffic."),
            ("Ad Management", "Optimizing ad spend for maximum return on ad spend (ROAS)."),
            ("Social Media Strategy", "Crafting platform-specific strategies to maximize engagement.")
        ],
        "why_choose": [
            ("Data-Driven Decisions", "Every campaign is backed by rigorous data analysis and testing."),
            ("Transparent Reporting", "Clear, comprehensive dashboards showing your exact ROI."),
            ("Holistic Approach", "Integrating SEO, PPC, and Content for maximum combined impact.")
        ],
        "versatility": [
            ("E-commerce", "Driving targeted traffic and maximizing online sales conversions."),
            ("B2B", "Generating high-quality leads and nurturing them through the funnel."),
            ("Local Business", "Dominating local search results and driving foot traffic.")
        ],
        "faqs": [
            ("How long does SEO take to show results?", "SEO is a long-term strategy. You can typically expect to see noticeable improvements in rankings and traffic within 3 to 6 months."),
            ("Do you manage Google Ads budgets?", "Yes, we handle full campaign setup, ongoing bid management, A/B testing, and budget optimization for maximum ROI."),
            ("What metrics do you track?", "We track traffic, bounce rates, conversion rates, cost per acquisition (CPA), and overall return on ad spend (ROAS).")
        ]
    },
    "mobile-apps.html": {
        "title": "Mobile App Services",
        "short_title": "Mobile Apps",
        "subtitle": "Engaging, high-performance native and cross-platform mobile applications.",
        "image": "https://images.unsplash.com/photo-1512428559087-560552a1d9ab?auto=format&fit=crop&q=80",
        "experts": "15+ Mobile Devs",
        "icon": "smartphone",
        "services": [
            ("Native iOS Development", "High-performance applications built specifically for Apple devices using Swift."),
            ("Native Android Development", "Robust Android applications built with Kotlin for the Google ecosystem."),
            ("React Native Development", "Efficient cross-platform apps sharing a single JavaScript codebase."),
            ("Flutter Development", "Beautiful, natively compiled applications for mobile from a single codebase."),
            ("Mobile UI/UX Design", "Intuitive, user-centric interfaces designed specifically for mobile touchpoints."),
            ("App Deployment", "Complete management of App Store and Google Play submission processes.")
        ],
        "expertise": [
            ("Swift & Kotlin", "Deep expertise in native development languages and frameworks."),
            ("Mobile Backend", "Scalable backend APIs and real-time database integrations."),
            ("App Store Optimization", "Strategies to improve visibility and downloads in app stores.")
        ],
        "why_choose": [
            ("Native Performance", "We ensure smooth, 60fps animations and rapid load times."),
            ("User-Centric Design", "Interfaces optimized for engagement, retention, and ease of use."),
            ("End-to-End Delivery", "From conceptualization to deployment and post-launch support.")
        ],
        "versatility": [
            ("Consumer Apps", "Engaging, highly interactive applications for mass-market users."),
            ("Enterprise Mobility", "Secure internal applications optimizing corporate workflows."),
            ("On-Demand Services", "Real-time location-based applications for gig-economy businesses.")
        ],
        "faqs": [
            ("Should I build native or cross-platform?", "It depends on your requirements. Native offers the best performance and device integration, while cross-platform (React Native/Flutter) offers faster time-to-market and lower costs."),
            ("Will you help publish the app?", "Yes, we handle the entire submission process for both the Apple App Store and Google Play Store, ensuring all guidelines are met."),
            ("Do you build the backend as well?", "Absolutely. We provide end-to-end development, including scalable backend architecture, APIs, and admin panels.")
        ]
    },
    "ui-ux-design.html": {
        "title": "UI/UX Design Services",
        "short_title": "UI/UX Design",
        "subtitle": "Intuitive, user-centric designs that elevate digital products and drive engagement.",
        "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&q=80",
        "experts": "12+ Design Experts",
        "icon": "pen-tool",
        "services": [
            ("UX Research", "Understanding user behavior, needs, and pain points through data."),
            ("Information Architecture", "Structuring content logically to ensure intuitive navigation."),
            ("Wireframing", "Creating structural blueprints for web and mobile interfaces."),
            ("Interactive Prototyping", "Building clickable models to test and refine user flows."),
            ("UI Design", "Crafting visually stunning, brand-aligned user interfaces."),
            ("Design Systems", "Creating comprehensive component libraries for scalable design.")
        ],
        "expertise": [
            ("Figma Mastery", "Advanced utilization of Figma for collaborative, scalable design."),
            ("User Testing", "Validating design decisions through real user feedback."),
            ("Accessibility", "Ensuring products are usable by people of all abilities (WCAG compliance).")
        ],
        "why_choose": [
            ("Data-Informed Design", "Decisions based on user research, not just aesthetics."),
            ("Seamless Handoffs", "Clean, documented design files ready for engineering implementation."),
            ("Conversion Focused", "Designs optimized to reduce friction and increase user conversion.")
        ],
        "versatility": [
            ("SaaS Platforms", "Complex dashboard designs focusing on data visualization and usability."),
            ("E-commerce", "Frictionless shopping experiences optimized for maximum conversions."),
            ("Healthcare", "Accessible, clear interfaces for patient portals and telemedicine apps.")
        ],
        "faqs": [
            ("What tools do your designers use?", "Our primary design tool is Figma. We also use tools like Miro for brainstorming and user journey mapping, and various user testing platforms."),
            ("Do you provide a design system?", "Yes, for comprehensive projects, we deliver a fully documented design system including typography, colors, components, and usage guidelines."),
            ("Can you redesign our existing app?", "Absolutely. We often start with a UX audit to identify current pain points before proposing and implementing a comprehensive redesign.")
        ]
    },
    "web-development.html": {
        "title": "Web Development Services",
        "short_title": "Web Development",
        "subtitle": "Scalable, secure, and high-performance web applications built for modern businesses.",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80",
        "experts": "30+ Web Developers",
        "icon": "monitor",
        "services": [
            ("Custom Web Apps", "Tailor-made web applications solving complex business challenges."),
            ("Responsive Websites", "Fast, SEO-optimized corporate websites that work flawlessly on all devices."),
            ("E-Commerce Solutions", "Scalable online stores built on Shopify, WooCommerce, or custom stacks."),
            ("CMS Development", "Customized Content Management Systems like WordPress and Strapi."),
            ("Progressive Web Apps (PWA)", "Web applications that offer native mobile-like experiences."),
            ("API Integration", "Connecting your web application with third-party services and databases.")
        ],
        "expertise": [
            ("Frontend Frameworks", "Deep expertise in React.js, Vue.js, and Angular."),
            ("Backend Technologies", "Robust server-side development using Node.js, Python, and PHP."),
            ("Cloud Deployment", "Scalable hosting architectures utilizing AWS, Vercel, and Docker.")
        ],
        "why_choose": [
            ("Modern Tech Stack", "We utilize the latest, most reliable frameworks for maximum performance."),
            ("Security First", "Implementing best practices to protect your data and prevent vulnerabilities."),
            ("Scalable Architecture", "Building foundations that grow seamlessly alongside your user base.")
        ],
        "versatility": [
            ("E-Commerce", "High-conversion storefronts capable of handling massive traffic spikes."),
            ("Corporate", "Professional, brand-aligned websites showcasing corporate excellence."),
            ("Education", "E-learning platforms with video streaming and interactive assessments.")
        ],
        "faqs": [
            ("What tech stack do you use?", "We customize the stack to the project. We frequently use React/Next.js for the frontend and Node.js or Python for the backend, supported by AWS cloud infrastructure."),
            ("Will my website be mobile-friendly?", "Yes, all our web development projects are fully responsive and optimized for mobile, tablet, and desktop devices from day one."),
            ("Do you offer post-launch support?", "We offer ongoing maintenance, security updates, and feature enhancements through our flexible support packages.")
        ]
    }
}

def generate_page(filename, data):
    # Base layout using inner-hero banner and 11 requested sections
    html = f'''
    <!-- {data["short_title"]} Hero Section -->
    <section class="inner-hero border-b border-[#EDEDED] pt-32 pb-24 md:pt-40 md:pb-24 overflow-hidden relative" style="background-color: #FAFAFA; padding-top: 10rem;">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-[#2F6F73] rounded-full blur-[150px] opacity-[0.07]"></div>
            <div class="absolute bottom-[-10%] left-[-5%] w-[30%] h-[30%] bg-[#E5B93C] rounded-full blur-[120px] opacity-[0.05]"></div>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center relative z-10">
            <div>
                <p class="text-xs font-black uppercase tracking-[0.2em] text-[#E5B93C] mb-4">Professional Services</p>
                <h1 class="font-black inner-hero-title tracking-tight leading-[1.05] mb-6 text-[2.5rem] md:text-[3.25rem] text-[#1F3D5A]">
                    {data["title"].replace(" Services", ' <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2F6F73] to-[#E5B93C]">Services.</span>')}
                </h1>

                <p class="text-lg text-[#4A4A4A] leading-relaxed mb-8">
                    {data["subtitle"]}
                </p>
                <div class="flex flex-wrap items-center gap-6">
                    <a href="../contact.html" class="inline-flex items-center gap-2 font-bold text-white bg-[#1F3D5A] px-8 py-4 rounded-xl hover:bg-[#2F6F73] transition-colors">
                        Get Free Quote <i data-lucide="arrow-right" class="w-5 h-5"></i>
                    </a>
                    
                    <div class="flex items-center gap-3">
                        <div class="flex text-[#E5B93C]">
                            <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                            <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                            <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                            <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                            <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        </div>
                        <div class="text-sm font-bold text-[#1F3D5A]">
                            4.9/5 <span class="text-[#4A4A4A] font-normal">Ratings</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="relative">
                <img src="{data["image"]}" alt="{data["short_title"]} Services" class="rounded-[2rem] shadow-2xl w-full h-[400px] md:h-[500px] object-cover">
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border border-[#EDEDED] flex items-center gap-4">
                    <div class="w-12 h-12 bg-[#2F6F73]/10 text-[#2F6F73] rounded-xl flex items-center justify-center shrink-0">
                        <i data-lucide="{data["icon"]}" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <p class="text-[#1F3D5A] font-black text-xl">{data["short_title"]}</p>
                        <p class="text-[#4A4A4A] text-sm font-medium">Expert Solutions</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- STATS/FACTS BAR -->
    <section class="bg-[#1F3D5A] py-8 relative z-20 shadow-xl">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center divide-x divide-white/10">
                <div class="px-4">
                    <p class="text-3xl font-black text-white mb-1">{data["experts"]}</p>
                    <p class="text-sm text-white/70 font-medium">Dedicated Experts</p>
                </div>
                <div class="px-4">
                    <p class="text-3xl font-black text-white mb-1">5+ Years</p>
                    <p class="text-sm text-white/70 font-medium">Average Experience</p>
                </div>
                <div class="px-4">
                    <p class="text-3xl font-black text-white mb-1">95%</p>
                    <p class="text-sm text-white/70 font-medium">Talent Retention Rate</p>
                </div>
                <div class="px-4">
                    <p class="text-3xl font-black text-[#E5B93C] mb-1">15 Days</p>
                    <p class="text-sm text-white/70 font-medium">Risk Free Trial</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 1. Comprehensive Services -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Comprehensive <span class="text-[#2F6F73]">{data["short_title"]}</span> Services</h2>
                <p class="text-[#4A4A4A] text-lg leading-relaxed">
                    End-to-end solutions tailored to meet your unique business objectives.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
'''
    for i, srv in enumerate(data["services"]):
        icon = ["check-circle", "zap", "star", "target", "shield", "layers", "cpu", "globe"][i % 8]
        html += f'''
                <div class="bg-[#FAFAFA] p-8 rounded-2xl border border-[#EDEDED] hover:shadow-lg transition-shadow">
                    <div class="w-12 h-12 bg-[#2F6F73]/10 text-[#2F6F73] rounded-xl flex items-center justify-center mb-6">
                        <i data-lucide="{icon}" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-3">{srv[0]}</h3>
                    <p class="text-[#4A4A4A] leading-relaxed text-sm">
                        {srv[1]}
                    </p>
                </div>
'''
    
    html += f'''
            </div>
        </div>
    </section>

    <!-- 2. Expertise & 3. Why Choose (Split Layout) -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
            
            <!-- Expertise -->
            <div>
                <h2 class="text-3xl md:text-4xl font-black text-[#1F3D5A] mb-6 tracking-tight">Our Expertise</h2>
                <p class="text-[#4A4A4A] text-lg leading-relaxed mb-8">
                    Technical mastery and proven methodologies that guarantee success.
                </p>
                <div class="space-y-6">
'''
    for exp in data["expertise"]:
        html += f'''
                    <div class="flex gap-4">
                        <div class="w-10 h-10 rounded-full bg-white border border-[#EDEDED] shadow-sm flex items-center justify-center shrink-0 text-[#2F6F73]">
                            <i data-lucide="check" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] mb-1">{exp[0]}</h4>
                            <p class="text-sm text-[#4A4A4A]">{exp[1]}</p>
                        </div>
                    </div>
'''
    
    html += f'''
                </div>
            </div>

            <!-- Why Choose -->
            <div class="bg-white p-8 md:p-10 rounded-[2rem] border border-[#EDEDED] shadow-xl relative overflow-hidden">
                <div class="absolute top-0 right-0 w-32 h-32 bg-[#2F6F73] rounded-bl-full opacity-5"></div>
                <h2 class="text-3xl md:text-4xl font-black text-[#1F3D5A] mb-8 tracking-tight relative z-10">Why Choose Us</h2>
                
                <ul class="space-y-8 relative z-10">
'''
    for i, why in enumerate(data["why_choose"]):
        color = ["#E5B93C", "#2F6F73", "#1F3D5A"][i % 3]
        html += f'''
                    <li class="relative pl-8">
                        <div class="absolute left-0 top-1 w-2 h-2 rounded-full bg-[{color}]"></div>
                        <h4 class="font-bold text-[#1F3D5A] text-lg mb-2">{why[0]}</h4>
                        <p class="text-[#4A4A4A] text-sm leading-relaxed">{why[1]}</p>
                    </li>
'''

    html += f'''
                </ul>
            </div>
        </div>
    </section>

    <!-- 4. Versatility Across Industries -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Versatility Across Industries</h2>
                <p class="text-[#4A4A4A] text-lg leading-relaxed">
                    Delivering high-impact {data["short_title"]} solutions tailored to your sector's unique challenges.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
'''
    for ind in data["versatility"]:
        html += f'''
                <div class="group border border-[#EDEDED] rounded-2xl p-8 hover:border-[#2F6F73] hover:shadow-lg transition-all text-center">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-3 group-hover:text-[#2F6F73] transition-colors">{ind[0]}</h3>
                    <p class="text-sm text-[#4A4A4A]">{ind[1]}</p>
                </div>
'''
    html += f'''
            </div>
        </div>
    </section>

    <!-- 5. Development Process -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Our Development Process</h2>
                <p class="text-[#4A4A4A] text-lg leading-relaxed">
                    A streamlined, transparent workflow ensuring quality delivery from day one.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-5 gap-6 relative">
                <!-- Connecting Line for Desktop -->
                <div class="hidden md:block absolute top-10 left-10 right-10 h-0.5 bg-[#EDEDED] z-0"></div>
                
                <!-- Steps -->
                <div class="relative z-10 flex flex-col items-center text-center group">
                    <div class="w-20 h-20 rounded-full bg-white text-[#1F3D5A] flex items-center justify-center mb-6 shadow-xl border-4 border-[#FAFAFA] group-hover:border-[#2F6F73] transition-colors">
                        <i data-lucide="search" class="w-8 h-8"></i>
                    </div>
                    <h3 class="font-black text-[#1F3D5A] text-xl mb-2">1. Discovery</h3>
                </div>
                <div class="relative z-10 flex flex-col items-center text-center group">
                    <div class="w-20 h-20 rounded-full bg-white text-[#1F3D5A] flex items-center justify-center mb-6 shadow-xl border-4 border-[#FAFAFA] group-hover:border-[#E5B93C] transition-colors">
                        <i data-lucide="pen-tool" class="w-8 h-8"></i>
                    </div>
                    <h3 class="font-black text-[#1F3D5A] text-xl mb-2">2. Strategy</h3>
                </div>
                <div class="relative z-10 flex flex-col items-center text-center group">
                    <div class="w-20 h-20 rounded-full bg-[#1F3D5A] text-white flex items-center justify-center mb-6 shadow-xl border-4 border-[#FAFAFA] group-hover:border-[#2F6F73] transition-colors">
                        <i data-lucide="braces" class="w-8 h-8"></i>
                    </div>
                    <h3 class="font-black text-[#1F3D5A] text-xl mb-2">3. Execution</h3>
                </div>
                <div class="relative z-10 flex flex-col items-center text-center group">
                    <div class="w-20 h-20 rounded-full bg-white text-[#1F3D5A] flex items-center justify-center mb-6 shadow-xl border-4 border-[#FAFAFA] group-hover:border-[#E5B93C] transition-colors">
                        <i data-lucide="rocket" class="w-8 h-8"></i>
                    </div>
                    <h3 class="font-black text-[#1F3D5A] text-xl mb-2">4. Launch</h3>
                </div>
                <div class="relative z-10 flex flex-col items-center text-center group">
                    <div class="w-20 h-20 rounded-full bg-white text-[#1F3D5A] flex items-center justify-center mb-6 shadow-xl border-4 border-[#FAFAFA] group-hover:border-[#2F6F73] transition-colors">
                        <i data-lucide="life-buoy" class="w-8 h-8"></i>
                    </div>
                    <h3 class="font-black text-[#1F3D5A] text-xl mb-2">5. Support</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Why Us with Kritox -->
    <section class="py-24 bg-white border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6">Why Kritox Digital for <span class="text-[#2F6F73]">{data["short_title"]}</span>?</h2>
                <p class="text-lg text-[#4A4A4A]">We combine enterprise-grade execution with startup agility.</p>
            </div>
            
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="award" class="w-8 h-8 mb-4 text-[#E5B93C]"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Award-Winning</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Recognized globally for digital excellence.</p>
                </div>
                <div class="bg-white border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="users" class="w-8 h-8 mb-4 text-[#2F6F73]"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Top 1% Talent</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Rigorous vetting process ensures elite quality.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="shield-check" class="w-8 h-8 mb-4 text-[#1F3D5A]"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">ISO Certified</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Strict adherence to global security standards.</p>
                </div>
                <div class="bg-white border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="smile" class="w-8 h-8 mb-4 text-[#E5B93C]"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">95% Retention</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Clients stay because we consistently deliver.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- INNER VARIANTS (7, 8, 9, 10) -->
    <!-- Industries (INNER PAGE VARIANT) -->
    <section class="py-24 bg-[#FAFAFA] border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-4">Industries We Empower</h2>
                <p class="text-[#4A4A4A] text-lg">Domain expertise across diverse business sectors.</p>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="heart-pulse" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">Healthcare</h3>
                </div>
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="shopping-bag" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">E-Commerce</h3>
                </div>
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="plane" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">Travel</h3>
                </div>
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="building-2" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">Real Estate</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- Portfolio (INNER PAGE VARIANT) -->
    <section class="py-24 bg-white border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-4">Our Recent Work</h2>
                <p class="text-[#4A4A4A] text-lg">Real outcomes driven by our technical expertise.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="group cursor-pointer rounded-3xl overflow-hidden border border-[#EDEDED] bg-[#FAFAFA] hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                    <div class="h-64 overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Project" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="p-8">
                        <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-2">{data["short_title"].upper()}</p>
                        <h3 class="text-2xl font-bold text-[#1F3D5A] mb-3">Enterprise Solution</h3>
                        <p class="text-[#4A4A4A] mb-6">A secure, scalable platform solving complex industry challenges.</p>
                        <span class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] group-hover:text-[#2F6F73] transition-colors">
                            View Case Study <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </span>
                    </div>
                </div>
                <div class="group cursor-pointer rounded-3xl overflow-hidden border border-[#EDEDED] bg-[#FAFAFA] hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                    <div class="h-64 overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Project" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="p-8">
                        <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-2">{data["short_title"].upper()}</p>
                        <h3 class="text-2xl font-bold text-[#1F3D5A] mb-3">B2B Workflow Automation</h3>
                        <p class="text-[#4A4A4A] mb-6">Empowering teams with seamless integrations and robust analytics.</p>
                        <span class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] group-hover:text-[#2F6F73] transition-colors">
                            View Case Study <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </span>
                    </div>
                </div>
            </div>
            <div class="text-center mt-12">
                <a href="../case-studies/index.html" class="inline-flex items-center gap-2 px-8 py-4 bg-[#1F3D5A] text-white rounded-xl font-bold hover:bg-[#2F6F73] transition-colors">
                    See All Projects <i data-lucide="layout-grid" class="w-5 h-5"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Testimonials (INNER PAGE VARIANT) -->
    <section class="py-24 bg-brand-dark relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-[#1F3D5A] via-[#2F6F73]/20 to-[#1F3D5A] z-0 pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-white mb-4">Client Feedback</h2>
                <p class="text-white/80 text-lg">What our partners say about working with us on {data["short_title"]} projects.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                <div class="bg-white/10 backdrop-blur-sm border border-white/10 p-8 rounded-3xl flex flex-col">
                    <div class="flex items-center gap-1 text-[#E5B93C] mb-6">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-white/90 text-lg mb-8 leading-relaxed italic flex-grow">"The technical expertise and dedication shown by the team was outstanding. They delivered beyond our expectations."</p>
                    <div class="flex items-center gap-4 mt-auto">
                        <div class="w-12 h-12 bg-[#2F6F73] rounded-full flex items-center justify-center text-white font-bold text-lg shrink-0">S</div>
                        <div>
                            <p class="text-white font-bold">Sarah Jenkins</p>
                            <p class="text-white/60 text-sm">CTO, TechFlow</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white/10 backdrop-blur-sm border border-white/10 p-8 rounded-3xl flex flex-col">
                    <div class="flex items-center gap-1 text-[#E5B93C] mb-6">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-white/90 text-lg mb-8 leading-relaxed italic flex-grow">"Kritox transformed our outdated systems into a modern architecture. A truly professional partner."</p>
                    <div class="flex items-center gap-4 mt-auto">
                        <div class="w-12 h-12 bg-[#2F6F73] rounded-full flex items-center justify-center text-white font-bold text-lg shrink-0">M</div>
                        <div>
                            <p class="text-white font-bold">Michael Chen</p>
                            <p class="text-white/60 text-sm">Founder, InnovateRetail</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Client Logos (INNER PAGE VARIANT) -->
    <section class="py-16 bg-[#FAFAFA] border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <p class="text-center text-[12px] font-black text-[#4A4A4A] uppercase tracking-[0.2em] mb-8">TRUSTED BY INNOVATIVE TEAMS WORLDWIDE</p>
            <div class="flex flex-wrap justify-center items-center gap-10 md:gap-16 opacity-60 grayscale mix-blend-multiply">
                <img src="../assets/client logo/hello healthy.png" alt="Hello Healthy" class="h-10 object-contain">
                <img src="../assets/client logo/HP Logo(PantoneU) copy.png" alt="HP" class="h-10 object-contain">
                <img src="../assets/client logo/Stern-logo-blue.png" alt="Stern" class="h-10 object-contain">
                <img src="../assets/client logo/logo-skedulo-navy.svg" alt="Skedulo" class="h-10 object-contain">
                <img src="../assets/client logo/smarteinc.png" alt="Smarteinc" class="h-10 object-contain">
                <img src="../assets/client logo/KBOnline.png" alt="KBOnline" class="h-10 object-contain">
            </div>
        </div>
    </section>

    <!-- 11. FAQs -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-4xl mx-auto px-6 md:px-10">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Frequently Asked Questions</h2>
            </div>
            
            <div class="faq-content-pane space-y-4">
'''
    for f in data["faqs"]:
        html += f'''
                <div class="bg-white border border-[#EDEDED] rounded-2xl p-6 lg:p-8 hover:border-[#2F6F73] transition-colors group cursor-pointer">
                    <div class="flex justify-between items-center">
                        <h3 class="text-lg md:text-xl font-bold text-[#1F3D5A] pr-4">{f[0]}</h3>
                        <div class="w-8 h-8 shrink-0 rounded-full bg-[#FAFAFA] border border-[#EDEDED] flex items-center justify-center text-[#1F3D5A] group-hover:bg-[#2F6F73] group-hover:text-white transition-colors">
                            <i data-lucide="plus" class="w-4 h-4"></i>
                        </div>
                    </div>
                    <p class="text-[#4A4A4A] mt-4 text-[15px] leading-relaxed hidden">
                        {f[1]}
                    </p>
                </div>
'''

    html += f'''
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="bg-[#1F3D5A] py-24 text-white text-center">
        <div class="max-w-3xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black mb-6">Have a Great Idea?</h2>
            <p class="text-white/70 text-lg mb-10 leading-relaxed">Tell us about it. We are ready to transform your ideas into reality with our robust {data["short_title"]} solutions.</p>
            <a href="../contact.html" class="inline-flex items-center gap-2 bg-white text-[#1F3D5A] font-bold px-8 py-4 rounded-xl hover:bg-[#E5B93C] transition-all">
                Let's Discuss <i data-lucide="arrow-right" class="w-5 h-5"></i>
            </a>
        </div>
    </section>
'''
    
    with open('_build_scripts/head_template.html', 'r', encoding='utf-8') as f:
        head = f.read()
    
    with open('_build_scripts/footer_template.html', 'r', encoding='utf-8') as f:
        footer = f.read()

    full_html = head + html + footer

    # Update active states in navbar (optional, but good practice)
    # The navbar might not easily be modifiable here via simple replace without breaking.

    path = os.path.join('services', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Generated {filename}")

for filename, data in pages_data.items():
    generate_page(filename, data)

