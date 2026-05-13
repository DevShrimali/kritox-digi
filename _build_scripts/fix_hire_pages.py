import os
import glob
import re

# We will just parse the existing HTML and replace the FAQs section.
# Actually, since I have the page data from my previous script, I can just recreate the pages!

PAGES = [
    {
        "file": "hire-full-stack.html",
        "tech": "Full Stack",
        "title": "Hire Dedicated Full Stack Developers",
        "subtitle": "Master both frontend and backend for end-to-end excellence.",
        "desc": "Hire Full Stack developers who master both frontend and backend — delivering end-to-end digital products with React, Node.js, Python, PHP and more.",
        "img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
        "services": [
            {"title": "Custom Web App Development", "desc": "End-to-end web apps using modern React/Vue frontends paired with Node.js, Python or PHP backends.", "icon": "layout"},
            {"title": "REST & GraphQL APIs", "desc": "Robust, versioned API design connecting your frontend to any data source or third-party service.", "icon": "server"},
            {"title": "Database Architecture", "desc": "Scalable schema design across SQL (PostgreSQL, MySQL) and NoSQL (MongoDB, Redis) databases.", "icon": "database"},
            {"title": "Mobile App Development", "desc": "Cross-platform mobile apps with React Native or Flutter backed by robust cloud APIs.", "icon": "smartphone"},
            {"title": "Cloud & DevOps", "desc": "CI/CD pipelines, Dockerised deployments and AWS/GCP cloud infrastructure setup.", "icon": "cloud"},
            {"title": "Legacy Migration", "desc": "Safe migration of legacy monoliths to modern microservices or serverless architectures.", "icon": "refresh-cw"}
        ],
        "faq": [
            {"q": "What technologies do your full stack developers specialize in?", "a": "Our developers are proficient in modern stacks including MERN, MEAN, and Python/Django, along with various database and cloud technologies."},
            {"q": "How do you ensure project consistency?", "a": "By handling both frontend and backend, our developers ensure a seamless flow of data and a consistent architectural approach throughout the project."},
            {"q": "Can I hire a full stack developer for an existing project?", "a": "Yes, our developers can jump into ongoing projects, audit existing code, and start delivering value from day one."}
        ]
    },
    {
        "file": "hire-mean-stack.html",
        "tech": "MEAN Stack",
        "title": "Hire Dedicated MEAN Stack Developers",
        "subtitle": "Build scalable, JavaScript-powered web applications.",
        "desc": "Hire dedicated MEAN Stack developers to build scalable, JavaScript-powered web applications using MongoDB, Express.js, Angular and Node.js.",
        "img": "https://images.unsplash.com/photo-1555099962-4199c345e5dd",
        "services": [
            {"title": "MEAN Stack Application Development", "desc": "Full-cycle MEAN applications from architecture design to production deployment.", "icon": "server"},
            {"title": "Angular Frontend Development", "desc": "Enterprise-grade Angular UIs with lazy loading, RxJS and NgRx state management.", "icon": "code"},
            {"title": "MongoDB Database Design", "desc": "Schema design, indexing strategy and aggregation pipelines for NoSQL data.", "icon": "database"},
            {"title": "Real-time Applications", "desc": "Socket.io-powered real-time features: live dashboards, chats and notifications.", "icon": "zap"},
            {"title": "REST & GraphQL APIs", "desc": "Express.js APIs with JWT auth, rate limiting and OpenAPI documentation.", "icon": "cloud"},
            {"title": "MEAN Stack Migration", "desc": "Move from legacy LAMP or MEAN v1 apps to modern MEAN stack architecture.", "icon": "refresh-cw"}
        ],
        "faq": [
            {"q": "Why choose MEAN stack for my project?", "a": "MEAN stack offers a unified language (JavaScript) across the entire stack, which speeds up development and improves team collaboration."},
            {"q": "Do you provide support for Angular upgrades?", "a": "Yes, we specialize in migrating and upgrading Angular applications to the latest versions while maintaining performance."},
            {"q": "Is MongoDB suitable for enterprise applications?", "a": "Absolutely. MongoDB's scalability and flexibility make it ideal for high-growth enterprise applications handling varied data types."}
        ]
    },
    {
        "file": "hire-mern-stack.html",
        "tech": "MERN Stack",
        "title": "Hire Dedicated MERN Stack Developers",
        "subtitle": "High-performance single-page applications and APIs.",
        "desc": "Hire dedicated MERN Stack developers to build high-performance single-page applications and APIs using MongoDB, Express.js, React and Node.js.",
        "img": "https://images.unsplash.com/photo-1633356122544-f134324a6cee",
        "services": [
            {"title": "MERN SPA Development", "desc": "Blazing-fast single-page applications with React 18, server components and Suspense.", "icon": "code"},
            {"title": "Node.js & Express APIs", "desc": "RESTful and GraphQL APIs with Passport.js auth, caching and rate limiting.", "icon": "server"},
            {"title": "MongoDB & Mongoose", "desc": "Efficient schema design, virtual fields and aggregation pipelines for data-heavy apps.", "icon": "database"},
            {"title": "React Component Libraries", "desc": "Reusable design systems with Storybook, Tailwind CSS or Material UI.", "icon": "layout"},
            {"title": "Next.js Applications", "desc": "SSR and SSG with Next.js for SEO-optimised MERN applications.", "icon": "zap"},
            {"title": "Migration to MERN", "desc": "Migrate from jQuery, PHP or legacy frameworks to the modern MERN stack.", "icon": "refresh-cw"}
        ],
        "faq": [
            {"q": "What is the difference between MERN and MEAN stack?", "a": "The primary difference is the frontend framework: MERN uses React, while MEAN uses Angular. React is often preferred for its flexibility and virtual DOM."},
            {"q": "Can you build SEO-friendly apps with MERN?", "a": "Yes, by utilizing Next.js for Server-Side Rendering (SSR), we can ensure your MERN applications are highly SEO-optimized."},
            {"q": "Do you offer MERN stack maintenance?", "a": "Yes, we provide ongoing maintenance, security patches, and performance tuning for all MERN stack projects."}
        ]
    },
    {
        "file": "hire-mobile-developers.html",
        "tech": "Mobile Developers",
        "title": "Hire Expert Mobile App Developers",
        "subtitle": "Native and Cross-platform mobile experiences.",
        "desc": "Hire dedicated mobile developers to build high-performance, user-centric mobile applications for iOS and Android platforms.",
        "img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c",
        "services": [
            {"title": "Native iOS Development", "desc": "Premium iPhone and iPad apps built with Swift and SwiftUI for the best performance.", "icon": "smartphone"},
            {"title": "Native Android Development", "desc": "Scalable Android apps built with Kotlin and Jetpack Compose for maximum reach.", "icon": "monitor"},
            {"title": "Cross-Platform Apps", "desc": "Cost-effective apps for both iOS and Android using Flutter or React Native.", "icon": "layers"},
            {"title": "Mobile App UI/UX", "desc": "Intuitive mobile interfaces designed for high engagement and seamless navigation.", "icon": "layout"},
            {"title": "Backend for Mobile", "desc": "Scalable cloud backends and APIs optimized specifically for mobile consumption.", "icon": "server"},
            {"title": "App Store Optimization", "desc": "Technical setup and metadata optimization for better visibility on App Store & Play Store.", "icon": "search"}
        ],
        "faq": [
            {"q": "Should I choose Native or Cross-platform?", "a": "It depends on your requirements. Native is best for high performance and hardware access, while Cross-platform is more cost-effective for reaching both platforms quickly."},
            {"q": "Do you assist with App Store submissions?", "a": "Yes, we handle the entire submission process, including metadata setup, screenshots, and compliance checks for both stores."},
            {"q": "Can you update an existing mobile app?", "a": "Yes, we can take over legacy mobile apps, refactor code, and add new features while maintaining current users."}
        ]
    },
    {
        "file": "hire-python.html",
        "tech": "Python Developers",
        "title": "Hire Dedicated Python Developers",
        "subtitle": "Experts in AI, Data Science, and Robust Backends.",
        "desc": "Hire Python developers to build scalable backends, data-driven applications, and cutting-edge AI integrations.",
        "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5",
        "services": [
            {"title": "Python Backend Systems", "desc": "High-performance server-side logic using Django, Flask, or FastAPI.", "icon": "server"},
            {"title": "AI & ML Integration", "desc": "Integrating machine learning models and AI capabilities into your existing products.", "icon": "zap"},
            {"title": "Data Science & Analytics", "desc": "Building tools for data processing, visualization, and predictive analytics with Python.", "icon": "bar-chart"},
            {"title": "Web Scraping & Automation", "desc": "Custom scrapers and automation scripts to streamline your business workflows.", "icon": "repeat"},
            {"title": "API Development", "desc": "Building robust RESTful and GraphQL APIs for web and mobile consumption.", "icon": "cloud"},
            {"title": "Scientific Computing", "desc": "Complex mathematical modeling and scientific analysis tools built with NumPy and SciPy.", "icon": "database"}
        ],
        "faq": [
            {"q": "Why is Python great for backend development?", "a": "Python's clear syntax, vast libraries, and strong community support make it ideal for building complex, maintainable backends quickly."},
            {"q": "Can you help with AI model deployment?", "a": "Yes, our Python experts specialize in taking models from research to production-ready APIs."},
            {"q": "Is Python suitable for high-traffic sites?", "a": "Absolutely. With proper architecture and frameworks like FastAPI or Django, Python powers some of the largest sites in the world."}
        ]
    },
    {
        "file": "hire-web-developers.html",
        "tech": "Web Developers",
        "title": "Hire Dedicated Web Developers",
        "subtitle": "Modern, scalable web solutions for the digital age.",
        "desc": "Hire web developers to build responsive, high-performing websites and web applications tailored to your business.",
        "img": "https://images.unsplash.com/photo-1547658719-da2b51169166",
        "services": [
            {"title": "Custom Website Development", "desc": "Unique, high-performance websites built from the ground up to match your brand.", "icon": "monitor"},
            {"title": "Frontend Development", "desc": "Responsive and interactive user interfaces built with React, Vue, or modern HTML/CSS.", "icon": "layout"},
            {"title": "Backend Development", "desc": "Robust server-side logic and database management for complex web applications.", "icon": "server"},
            {"title": "E-commerce Solutions", "desc": "Custom shopping experiences and secure payment integrations for online businesses.", "icon": "shopping-cart"},
            {"title": "Progressive Web Apps", "desc": "Web applications that feel like native apps, with offline capabilities and push notifications.", "icon": "zap"},
            {"title": "Web Performance Tuning", "desc": "Optimizing existing websites for speed, Core Web Vitals, and better user experience.", "icon": "activity"}
        ],
        "faq": [
            {"q": "Do you build responsive websites?", "a": "Yes, every website we build is mobile-first and fully responsive across all device sizes."},
            {"q": "Can you work with my existing design?", "a": "Absolutely. We can take your designs (Figma, Sketch, etc.) and convert them into pixel-perfect, performant code."},
            {"q": "Do you provide website maintenance?", "a": "Yes, we offer various support and maintenance packages to keep your website secure and up-to-date."}
        ]
    }
]

with open('tech/mobile.html', 'r') as f:
    full_html = f.read()

navbar_part = full_html.split('<!-- Navbar -->')[1].split('</nav>')[0] + '</nav>'
footer_part = full_html.split('<!-- Footer -->')[1]

def generate_page(data):
    services_html = ""
    for s in data["services"]:
        services_html += f'''
                <div class="bg-[#FAFAFA] p-8 rounded-[2rem] border border-[#EDEDED] hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
                    <div class="w-14 h-14 bg-brand-base/10 text-brand-base rounded-2xl flex items-center justify-center mb-6">
                        <i data-lucide="{s['icon']}" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-xl font-bold text-brand-dark mb-4">{s['title']}</h3>
                    <p class="text-neutral-dark leading-relaxed text-sm">{s['desc']}</p>
                </div>'''

    faq_html = ""
    for i, f in enumerate(data["faq"]):
        if i == 0:
            faq_html += f'''
                <div class="bg-white border border-[#2F6F73] shadow-md rounded-2xl p-6 lg:p-8 group cursor-pointer transition-colors">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-lg md:text-xl font-bold text-[#1F3D5A] pr-4">{f['q']}</h3>
                        <div class="w-8 h-8 shrink-0 rounded-full bg-[#2F6F73] flex items-center justify-center text-white transition-colors">
                            <i data-lucide="minus" class="w-4 h-4"></i>
                        </div>
                    </div>
                    <p class="text-[#4A4A4A] text-[15px] leading-relaxed">
                        {f['a']}
                    </p>
                </div>'''
        else:
            faq_html += f'''
                <div class="bg-white border border-[#EDEDED] rounded-2xl p-6 lg:p-8 hover:border-[#2F6F73] transition-colors group cursor-pointer">
                    <div class="flex justify-between items-center">
                        <h3 class="text-lg md:text-xl font-bold text-[#1F3D5A] pr-4">{f['q']}</h3>
                        <div class="w-8 h-8 shrink-0 rounded-full bg-[#FAFAFA] border border-[#EDEDED] flex items-center justify-center text-[#1F3D5A] group-hover:bg-[#2F6F73] group-hover:text-white transition-colors">
                            <i data-lucide="plus" class="w-4 h-4"></i>
                        </div>
                    </div>
                    <p class="text-[#4A4A4A] mt-4 text-[15px] leading-relaxed hidden">
                        {f['a']}
                    </p>
                </div>'''

    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']} | Kritox Digital</title>
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script src="../js/tailwind-config.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
    <link rel="icon" type="image/png" href="../assets/favicon.png">
</head>

<body class="bg-white text-brand-dark selection-style">

    <!-- Navbar -->
    <!-- Navbar -->{navbar_part}

    <!-- Hero Section -->
    <section class="inner-hero border-b border-[#EDEDED]">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-brand-base rounded-full blur-[150px] opacity-[0.07]"></div>
            <div class="absolute bottom-[-10%] left-[-5%] w-[30%] h-[30%] bg-brand-accent rounded-full blur-[120px] opacity-[0.05]"></div>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center relative z-10">
            <div>
                <p class="text-xs font-black uppercase tracking-[0.2em] text-brand-accent mb-4">Elite Talent, Fast</p>
                <h1 class="font-black inner-hero-title tracking-tight leading-[1.05] mb-6">
                    {data['title']} <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-base to-brand-accent">Experts.</span>
                </h1>
                <p class="text-lg text-neutral-dark leading-relaxed mb-8">
                    {data['desc']}
                </p>
                
                <div class="flex flex-wrap items-center gap-6">
                    <a href="../contact.html" class="inline-flex items-center gap-2 font-bold text-white bg-brand-dark px-8 py-4 rounded-xl hover:bg-brand-base transition-colors shadow-lg">
                        Hire {data['tech']} Experts <i data-lucide="arrow-right" class="w-5 h-5"></i>
                    </a>
                </div>
            </div>
            <div class="relative">
                <img src="{data['img']}?auto=format&fit=crop&q=80&w=1000" alt="Hire {data['tech']}" class="rounded-[2rem] shadow-2xl w-full h-[500px] object-cover">
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border border-[#EDEDED] flex flex-col gap-2">
                    <div class="flex items-center gap-2">
                        <i data-lucide="star" class="w-5 h-5 text-brand-accent fill-current"></i>
                        <span class="font-bold text-brand-dark text-lg">Top Rated</span>
                    </div>
                    <p class="text-neutral-dark text-sm font-medium">95% Client Retention</p>
                </div>
                <div class="absolute -top-6 -right-6 bg-brand-dark p-6 rounded-2xl shadow-xl text-white flex flex-col items-center">
                    <span class="font-black text-3xl text-brand-accent">5+</span>
                    <span class="text-sm font-semibold text-white/80 uppercase tracking-widest mt-1">Years Avg Exp</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Custom Services -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <p class="text-[12px] font-black text-brand-base uppercase tracking-[0.2em] mb-4">OUR EXPERTISE</p>
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6">Custom Services Our {data['tech']} Provide</h2>
                <p class="text-neutral-dark text-lg">From ideation to deployment, our developers offer a comprehensive suite of services tailored to your unique requirements.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                {services_html}
            </div>
        </div>
    </section>

    <!-- Dedicated Hiring Models -->
    <section class="bg-brand-dark py-24 border-b border-white/10 text-white selection-style relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <defs><pattern id="grid-dark" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="white" stroke-width="1"/></pattern></defs>
                <rect width="100%" height="100%" fill="url(#grid-dark)" />
            </svg>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <p class="text-[12px] font-black text-brand-accent uppercase tracking-[0.2em] mb-4">FLEXIBLE ENGAGEMENT</p>
                <h2 class="text-3xl md:text-5xl font-black mb-6 tracking-tight text-white">Dedicated Hiring Models</h2>
                <p class="text-lg text-white/60 leading-relaxed max-w-3xl mx-auto">
                    Choose an engagement model that fits your budget, timeline, and project requirements. We offer flexible options to scale your team efficiently.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-white/10 border border-white/20 rounded-3xl p-8 hover:bg-white/15 transition-all">
                    <h3 class="text-2xl font-bold text-white mb-2">Dedicated Team</h3>
                    <p class="text-brand-accent font-semibold mb-6">Full-time engagement</p>
                    <p class="text-white/60 text-sm mb-8 leading-relaxed">Hire an entire team of {data['tech']} experts who work exclusively on your project as an extension of your in-house team.</p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> 160 Hours/Month</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> Direct Control</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> No Hidden Costs</li>
                    </ul>
                    <a href="../contact.html" class="block text-center bg-white text-black font-bold py-3 rounded-xl hover:bg-brand-accent transition-colors">Choose Model</a>
                </div>
                <div class="bg-white/10 border border-white/20 rounded-3xl p-8 hover:bg-white/15 transition-all relative transform md:-translate-y-4 shadow-2xl border-brand-accent/50">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-brand-accent text-black text-xs font-black px-4 py-1 rounded-full uppercase tracking-widest">Most Popular</div>
                    <h3 class="text-2xl font-bold text-white mb-2">Time & Material</h3>
                    <p class="text-brand-accent font-semibold mb-6">Hourly engagement</p>
                    <p class="text-white/60 text-sm mb-8 leading-relaxed">Ideal for ongoing projects with evolving requirements. Pay only for the actual hours worked by our {data['tech']} developers.</p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> Pay As You Go</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> High Flexibility</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> Agile Approach</li>
                    </ul>
                    <a href="../contact.html" class="block text-center bg-brand-accent text-black font-bold py-3 rounded-xl hover:bg-white transition-colors">Choose Model</a>
                </div>
                <div class="bg-white/10 border border-white/20 rounded-3xl p-8 hover:bg-white/15 transition-all">
                    <h3 class="text-2xl font-bold text-white mb-2">Fixed Cost</h3>
                    <p class="text-brand-accent font-semibold mb-6">Project-based engagement</p>
                    <p class="text-white/60 text-sm mb-8 leading-relaxed">Best for projects with clearly defined scopes, deliverables, and timelines. Complete your {data['tech']} project within a fixed budget.</p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> Defined Milestones</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> Fixed Budget</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-brand-accent"></i> Minimal Risk</li>
                    </ul>
                    <a href="../contact.html" class="block text-center bg-white text-black font-bold py-3 rounded-xl hover:bg-brand-accent transition-colors">Choose Model</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="order-2 lg:order-1 relative">
                <div class="absolute inset-0 bg-brand-base rounded-[2rem] transform -translate-x-4 translate-y-4"></div>
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80" alt="Why Choose Us" class="relative rounded-[2rem] shadow-xl w-full h-[500px] object-cover">
            </div>
            <div class="order-1 lg:order-2">
                <p class="text-[12px] font-black text-brand-base uppercase tracking-[0.2em] mb-4">THE KRITOX ADVANTAGE</p>
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6">Why Choose Us for {data['tech']} Development?</h2>
                <p class="text-neutral-dark text-lg leading-relaxed mb-8">
                    Partnering with Kritox Digital means choosing a team of seasoned professionals dedicated to delivering excellence. Our developers bring a wealth of experience and a track record of successful project completions.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="check-circle" class="w-6 h-6 text-brand-base"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-dark mb-1">Pre-vetted Talent</h4>
                            <p class="text-sm text-neutral-dark">Top 1% of experts meticulously screened for your project.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="clock" class="w-6 h-6 text-brand-base"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-dark mb-1">Fast Onboarding</h4>
                            <p class="text-sm text-neutral-dark">Start your project within 48 hours of engagement.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="shield" class="w-6 h-6 text-brand-base"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-dark mb-1">Strict NDA</h4>
                            <p class="text-sm text-neutral-dark">Your intellectual property is completely protected at all times.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="headphones" class="w-6 h-6 text-brand-base"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-brand-dark mb-1">24/7 Support</h4>
                            <p class="text-sm text-neutral-dark">Continuous communication across all global time zones.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="bg-brand-base py-24 relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <p class="text-[12px] font-black text-white uppercase tracking-[0.2em] mb-4">CLIENT REVIEWS</p>
                <h2 class="text-3xl md:text-5xl font-black text-white mb-6">What Our Clients Say</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bg-white p-8 rounded-3xl shadow-xl flex flex-col h-full">
                    <div class="flex text-brand-accent mb-4">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-neutral-dark italic flex-1 mb-6">"The {data['tech']} developers from Kritox Digital were exceptional. They integrated perfectly with our internal team and delivered ahead of schedule."</p>
                    <div class="flex items-center gap-4 mt-auto border-t border-[#EDEDED] pt-6">
                        <div class="w-12 h-12 rounded-full bg-brand-base/10 text-brand-base font-bold flex items-center justify-center text-lg">JD</div>
                        <div>
                            <h4 class="font-bold text-brand-dark">John Doe</h4>
                            <p class="text-xs text-neutral-dark uppercase tracking-wider font-semibold">CTO, TechCorp</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-3xl shadow-xl flex flex-col h-full">
                    <div class="flex text-brand-accent mb-4">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-neutral-dark italic flex-1 mb-6">"Hiring a dedicated team was the best decision. Their expertise in {data['tech']} is unmatched and the communication was transparent throughout."</p>
                    <div class="flex items-center gap-4 mt-auto border-t border-[#EDEDED] pt-6">
                        <div class="w-12 h-12 rounded-full bg-brand-base/10 text-brand-base font-bold flex items-center justify-center text-lg">SS</div>
                        <div>
                            <h4 class="font-bold text-brand-dark">Sarah Smith</h4>
                            <p class="text-xs text-neutral-dark uppercase tracking-wider font-semibold">Product Manager, Innovate Inc.</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-3xl shadow-xl flex flex-col h-full hidden lg:flex">
                    <div class="flex text-brand-accent mb-4">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-neutral-dark italic flex-1 mb-6">"Kritox delivered an outstanding {data['tech']} application that transformed our digital presence. Highly recommend their dedicated developers."</p>
                    <div class="flex items-center gap-4 mt-auto border-t border-[#EDEDED] pt-6">
                        <div class="w-12 h-12 rounded-full bg-brand-base/10 text-brand-base font-bold flex items-center justify-center text-lg">MJ</div>
                        <div>
                            <h4 class="font-bold text-brand-dark">Michael Johnson</h4>
                            <p class="text-xs text-neutral-dark uppercase tracking-wider font-semibold">CEO, StartUp Solutions</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="py-24 bg-white overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 mb-16">
            <div class="text-center max-w-4xl mx-auto">
                <p class="text-[12px] font-black text-brand-base uppercase tracking-[0.2em] mb-4">OUR WORK</p>
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6 tracking-tight">Recent {data['tech']} Projects</h2>
            </div>
        </div>

        <div class="relative">
            <div class="pointer-events-none absolute left-0 top-0 h-full w-24 md:w-40 z-10" style="background: linear-gradient(to right, #ffffff 0%, rgba(255,255,255,0) 100%);"></div>

            <div id="portfolio-carousel" class="bleed-carousel-container carousel-container carousel-seamless flex gap-6 overflow-x-auto snap-x snap-mandatory no-scrollbar pb-10 cursor-grab active:cursor-grabbing">
                <div class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-lg hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Project 1" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] font-bold leading-tight mb-2">Fintech Platform</h3>
                        <p class="text-white/80 mb-6">Built with {data['tech']}</p>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-2 transition-transform"></i>
                        </div>
                    </div>
                </div>
                <div class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-lg hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Project 2" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] font-bold leading-tight mb-2">Enterprise SaaS</h3>
                        <p class="text-white/80 mb-6">Built with {data['tech']}</p>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-2 transition-transform"></i>
                        </div>
                    </div>
                </div>
                <div class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-lg hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Project 3" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] font-bold leading-tight mb-2">E-Commerce Portal</h3>
                        <p class="text-white/80 mb-6">Built with {data['tech']}</p>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-2 transition-transform"></i>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="max-w-7xl mx-auto px-6 md:px-10 mt-6 relative z-20 pointer-events-auto flex items-center justify-between">
                <div class="flex gap-3">
                    <button id="portfolio-carousel-prev" class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-brand-dark hover:bg-brand-base hover:text-white transition-all"><i data-lucide="chevron-left"></i></button>
                    <button id="portfolio-carousel-next" class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-brand-dark hover:bg-brand-base hover:text-white transition-all"><i data-lucide="chevron-right"></i></button>
                </div>
                <a href="../case-studies/index.html" class="inline-flex items-center justify-center gap-2 px-8 py-3 bg-brand-dark text-white font-bold rounded-2xl hover:bg-brand-base transition-colors">View All Case Studies</a>
            </div>
        </div>
    </section>

    <!-- Hire Stack Developers with Integration Capabilities -->
    <section class="bg-[#FAFAFA] py-24 border-t border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 text-center">
            <h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6">Hire {data['tech']} with Full Stack Integration Capabilities</h2>
            <p class="text-lg text-neutral-dark max-w-3xl mx-auto mb-10">Ready to transform your vision into a robust digital product? Our pre-vetted {data['tech']} developers seamlessly integrate into your workflow to deliver excellence.</p>
            <a href="../contact.html" class="inline-flex items-center gap-2 bg-brand-base text-white px-10 py-5 rounded-2xl font-black text-lg hover:bg-brand-dark transition-colors shadow-xl">
                Let's Discuss Your Project <i data-lucide="arrow-right"></i>
            </a>
        </div>
    </section>

    <!-- FAQs Section -->
    <section class="bg-white py-24 border-t border-[#EDEDED]">
        <div class="max-w-4xl mx-auto px-6 md:px-10">
            <div class="text-center mb-16">
                <p class="text-[12px] font-black text-brand-base uppercase tracking-[0.2em] mb-4">FAQ</p>
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6 tracking-tight">Frequently Asked Questions</h2>
            </div>
            
            <div class="space-y-4">
                {faq_html}
            </div>
        </div>
    </section>

    <!-- Have a Great Idea CTA -->
    <section class="bg-brand-dark py-24 relative overflow-hidden">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-0 right-[-10%] w-[40%] h-[100%] bg-brand-base blur-[150px] opacity-40"></div>
            <div class="absolute bottom-[-20%] left-[-10%] w-[30%] h-[50%] bg-brand-accent blur-[150px] opacity-20"></div>
        </div>
        <div class="max-w-5xl mx-auto px-6 md:px-10 text-center relative z-10">
            <h2 class="text-4xl md:text-6xl font-black text-white mb-6">Have a Great Idea? <br/><span class="text-brand-accent">Tell us about it.</span></h2>
            <p class="text-white/80 text-lg md:text-xl mb-12 max-w-2xl mx-auto">
                Ready to start your project? Or perhaps you have more questions about our services? We're here to help you every step of the way.
            </p>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
                <a href="../contact.html" class="w-full sm:w-auto px-8 py-4 bg-brand-accent text-brand-dark font-bold text-lg rounded-xl hover:bg-white transition-colors text-center">
                    Schedule a Free Consultation
                </a>
                <a href="../contact.html" class="w-full sm:w-auto px-8 py-4 bg-transparent border-2 border-white text-white font-bold text-lg rounded-xl hover:bg-white/10 transition-colors text-center">
                    Request a Project Quote
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <!-- Footer -->{footer_part}

    <script src="../js/main.js" defer></script>
</body>

</html>
'''

for page_data in PAGES:
    filename = page_data["file"]
    filepath = os.path.join("hire", filename)
    with open(filepath, "w") as f:
        f.write(generate_page(page_data))

print("All 6 hire pages FAQ aligned successfully!")
