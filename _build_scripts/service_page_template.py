import os

pages = [
    {
        "slug": "service-react",
        "category": "Web Development",
        "title": "React & Next.js Development",
        "tagline": "Build blazing-fast, SEO-ready web applications with the world's most popular frontend frameworks.",
        "icon": "code-2",
        "accent": "#2F6F73",
        "hero_img": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?auto=format&fit=crop&w=1200&q=80",
        "what": "We build enterprise-grade React and Next.js applications that are fast, scalable, and built for growth. From single-page apps to server-side rendered platforms, our engineers craft interfaces that users love.",
        "features": [
            ("Server-Side Rendering (SSR)", "Superior SEO and initial load performance via Next.js SSR and Static Site Generation."),
            ("Component Architecture", "Reusable, maintainable component libraries with Storybook-driven development."),
            ("State Management", "Scalable state with Redux, Zustand, or React Query — chosen for your use case."),
            ("API Integration", "Seamless REST & GraphQL integration with type-safe clients."),
            ("Performance Optimization", "Core Web Vitals tuned: lazy loading, code splitting, image optimization."),
            ("Testing & CI/CD", "Jest, Cypress, and automated pipelines for zero-regression deployments."),
        ],
        "tech": ["React 18", "Next.js 14", "TypeScript", "Tailwind CSS", "Redux", "GraphQL", "Vercel"],
        "cta_text": "Start Your React Project",
    },
    {
        "slug": "service-nodejs",
        "category": "Backend Development",
        "title": "Node.js & Go Backend Development",
        "tagline": "High-performance, event-driven backends that scale to millions of requests without breaking a sweat.",
        "icon": "server",
        "accent": "#1F3D5A",
        "hero_img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80",
        "what": "Our backend engineers build robust APIs, microservices, and real-time systems using Node.js and Go. Whether you need a REST API, WebSocket server, or distributed processing pipeline, we architect solutions built for performance.",
        "features": [
            ("RESTful & GraphQL APIs", "Well-documented, versioned APIs designed for long-term maintainability."),
            ("Microservices Architecture", "Loosely coupled services that scale independently with Docker & Kubernetes."),
            ("Real-time Systems", "WebSocket and event-driven architectures for chat, notifications, and live data."),
            ("Authentication & Security", "JWT, OAuth2, and zero-trust security practices built in from day one."),
            ("Database Integration", "Expert ORM/ODM setup with PostgreSQL, MongoDB, Redis, and more."),
            ("Performance Tuning", "Profiling, caching strategies, and load testing to ensure peak performance."),
        ],
        "tech": ["Node.js", "Express", "Fastify", "Go (Golang)", "PostgreSQL", "Redis", "Docker", "Kubernetes"],
        "cta_text": "Build Your Backend",
    },
    {
        "slug": "service-php",
        "category": "Web Development",
        "title": "PHP & Laravel Development",
        "tagline": "Reliable, battle-tested PHP development powering millions of websites and enterprise applications worldwide.",
        "icon": "layers",
        "accent": "#2F6F73",
        "hero_img": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1200&q=80",
        "what": "From custom web applications to complex enterprise platforms, our PHP and Laravel specialists deliver clean, maintainable code. We leverage the full power of the Laravel ecosystem for rapid, secure development.",
        "features": [
            ("Laravel Framework", "Elegant MVC architecture with Eloquent ORM, queues, jobs, and notifications built-in."),
            ("Custom CMS & Portals", "Tailor-made CMS, admin dashboards, and client portals beyond what off-the-shelf provides."),
            ("API Development", "RESTful and GraphQL APIs with Laravel Sanctum/Passport authentication."),
            ("E-Commerce Platforms", "WooCommerce, Magento customization and bespoke e-commerce with Laravel."),
            ("Database Architecture", "Optimized MySQL/PostgreSQL schema design with migrations and seeders."),
            ("Legacy Migration", "Modernize existing PHP codebases and migrate to Laravel with zero downtime."),
        ],
        "tech": ["PHP 8.3", "Laravel 11", "Livewire", "Filament", "MySQL", "Redis", "AWS", "Forge"],
        "cta_text": "Start a PHP Project",
    },
    {
        "slug": "service-python",
        "category": "Backend & AI Development",
        "title": "Python & Django Development",
        "tagline": "From data pipelines to full-stack web apps — Python is the language of scale, AI, and rapid delivery.",
        "icon": "terminal",
        "accent": "#1F3D5A",
        "hero_img": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?auto=format&fit=crop&w=1200&q=80",
        "what": "Python's versatility makes it the go-to choice for web backends, data engineering, and AI. Our Python engineers build everything from Django-powered platforms to FastAPI microservices and machine learning pipelines.",
        "features": [
            ("Django & DRF", "Robust, secure web applications with Django's batteries-included approach and REST Framework."),
            ("FastAPI Microservices", "Async, high-performance APIs with automatic OpenAPI documentation."),
            ("Data Engineering", "ETL pipelines, data processing workflows, and analytics platforms at scale."),
            ("ML Model Deployment", "Serve your ML models as production APIs with FastAPI and containerization."),
            ("Automation & Scripting", "Internal tooling, workflow automation, and scheduled data tasks."),
            ("Third-Party Integrations", "Payment gateways, CRMs, ERPs, and SaaS platforms connected seamlessly."),
        ],
        "tech": ["Python 3.12", "Django", "FastAPI", "Celery", "PostgreSQL", "TensorFlow", "Docker", "AWS Lambda"],
        "cta_text": "Start a Python Project",
    },
    {
        "slug": "service-ai",
        "category": "Artificial Intelligence",
        "title": "AI & Machine Learning Solutions",
        "tagline": "Transform your business with intelligent systems that learn, adapt, and deliver measurable results.",
        "icon": "cpu",
        "accent": "#E5B93C",
        "hero_img": "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?auto=format&fit=crop&w=1200&q=80",
        "what": "We design, train, and deploy AI solutions that solve real business problems. From natural language processing and computer vision to generative AI integrations, our AI engineers make intelligence accessible and production-ready.",
        "features": [
            ("Generative AI Integration", "LLM integrations (GPT-4, Claude, Gemini) with fine-tuning and RAG pipelines."),
            ("Machine Learning Models", "Custom model training, evaluation, and deployment for classification, prediction, and recommendation."),
            ("Computer Vision", "Image recognition, object detection, and video analytics for industrial and consumer use."),
            ("NLP & Chatbots", "Intelligent chatbots, document understanding, and sentiment analysis systems."),
            ("AI Consulting", "Strategy workshops, proof-of-concept builds, and production roadmaps."),
            ("MLOps & Monitoring", "End-to-end ML pipelines with drift detection, retraining triggers, and observability."),
        ],
        "tech": ["Python", "TensorFlow", "PyTorch", "OpenAI API", "LangChain", "Pinecone", "AWS SageMaker", "MLflow"],
        "cta_text": "Explore AI Solutions",
    },
    {
        "slug": "service-react-native",
        "category": "Mobile Development",
        "title": "React Native App Development",
        "tagline": "One codebase. Two platforms. Native performance that users can't tell from a fully native app.",
        "icon": "smartphone",
        "accent": "#2F6F73",
        "hero_img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=1200&q=80",
        "what": "Our React Native team builds cross-platform mobile applications that share up to 95% code between iOS and Android, without sacrificing performance or user experience. Ship faster, maintain less.",
        "features": [
            ("Cross-Platform Efficiency", "Single codebase deployed to iOS and Android, dramatically reducing time and cost."),
            ("Native Modules", "Access native device APIs — camera, GPS, biometrics, push notifications — with native modules."),
            ("Expo & Bare Workflow", "Flexible project setup from managed Expo to fully customized bare React Native."),
            ("Offline-First Architecture", "Local-first data sync with SQLite and background sync for seamless offline experiences."),
            ("Performance Optimization", "JS bundle splitting, Hermes engine, and Reanimated for 60fps animations."),
            ("App Store Deployment", "Full end-to-end submission to Google Play and Apple App Store."),
        ],
        "tech": ["React Native", "Expo", "TypeScript", "Redux", "React Navigation", "Reanimated", "Firebase", "Fastlane"],
        "cta_text": "Build Your Mobile App",
    },
    {
        "slug": "service-flutter",
        "category": "Mobile Development",
        "title": "Flutter App Development",
        "tagline": "Beautiful, natively compiled apps for mobile, web, and desktop from a single Dart codebase.",
        "icon": "layers",
        "accent": "#1F3D5A",
        "hero_img": "https://images.unsplash.com/photo-1551650975-87deedd944c3?auto=format&fit=crop&w=1200&q=80",
        "what": "Flutter's custom rendering engine enables pixel-perfect UI on every platform. Our Flutter specialists build stunning apps for iOS, Android, and web — all from one codebase — with exceptional performance and design fidelity.",
        "features": [
            ("Custom UI Design", "Pixel-perfect designs rendered with Flutter's own Skia/Impeller engine, not native widgets."),
            ("Multi-Platform", "Deploy to iOS, Android, web, and desktop from a single Dart codebase."),
            ("State Management", "Riverpod, Bloc, or Provider — chosen for your app's complexity and team preference."),
            ("Firebase Integration", "Auth, Firestore, Analytics, and Cloud Functions integrated out of the box."),
            ("Platform Channels", "Native code integration for platform-specific features on both iOS and Android."),
            ("Performance", "60/120fps guaranteed with Flutter's hardware-accelerated rendering pipeline."),
        ],
        "tech": ["Flutter", "Dart", "Riverpod", "Bloc", "Firebase", "Dio", "SQLite", "Fastlane"],
        "cta_text": "Start a Flutter Project",
    },
    {
        "slug": "service-vuejs",
        "category": "Web Development",
        "title": "Vue.js & Nuxt Development",
        "tagline": "Progressive, approachable, and performant — Vue.js makes complex UIs feel effortless to build.",
        "icon": "monitor",
        "accent": "#2F6F73",
        "hero_img": "https://images.unsplash.com/photo-1593720219276-0b1eacd0aef4?auto=format&fit=crop&w=1200&q=80",
        "what": "Vue.js is the progressive framework of choice for teams that value developer experience and clean, readable code. Our Vue engineers build everything from interactive dashboards to full-stack Nuxt applications with SSR.",
        "features": [
            ("Nuxt.js SSR/SSG", "Server-side rendering and static site generation for SEO and performance."),
            ("Vue 3 Composition API", "Modern, scalable component logic with the Composition API and script setup."),
            ("Pinia State Management", "Lightweight, intuitive state management with TypeScript support."),
            ("Component Libraries", "Integration with Vuetify, PrimeVue, and custom design systems."),
            ("API Integration", "Axios, Fetch, and GraphQL clients wired to your backend."),
            ("Micro-Frontend Architecture", "Vue components embedded in multi-framework enterprise applications."),
        ],
        "tech": ["Vue 3", "Nuxt 3", "TypeScript", "Pinia", "Vite", "Vuetify", "Tailwind CSS", "Vercel"],
        "cta_text": "Build with Vue.js",
    },
    {
        "slug": "service-wordpress",
        "category": "Web Development",
        "title": "WordPress Development",
        "tagline": "The world's most popular CMS, engineered to enterprise standards by our WordPress specialists.",
        "icon": "globe",
        "accent": "#2F6F73",
        "hero_img": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?auto=format&fit=crop&w=1200&q=80",
        "what": "Beyond out-of-the-box WordPress, we build custom themes, complex plugins, and enterprise-grade WooCommerce stores. Our WordPress team delivers performance-optimized, secure, and highly scalable solutions.",
        "features": [
            ("Custom Theme Development", "Bespoke WordPress themes built to your exact brand and functional requirements."),
            ("Plugin Development", "Custom plugins for unique business logic, integrations, and workflows."),
            ("WooCommerce Stores", "Full-featured e-commerce with custom payment gateways, product logic, and reporting."),
            ("Headless WordPress", "WordPress as a CMS backend with React/Next.js frontend for best-of-both-worlds flexibility."),
            ("Performance & Security", "Caching layers, CDN setup, security hardening, and managed hosting configuration."),
            ("Migration & Updates", "Safe migration from other platforms and seamless major version upgrades."),
        ],
        "tech": ["WordPress 6.x", "WooCommerce", "PHP 8", "ACF Pro", "Elementor", "Gutenberg", "Cloudflare", "WP Engine"],
        "cta_text": "Start a WordPress Project",
    },
]

def make_feature_html(features):
    html = ""
    for title, desc in features:
        html += f'''
                    <div class="group p-6 bg-[#FAFAFA] rounded-2xl border border-[#EDEDED] hover:shadow-md hover:border-[#2F6F73]/30 transition-all">
                        <div class="flex items-start gap-4">
                            <div class="w-8 h-8 rounded-lg bg-[#1F3D5A] flex items-center justify-center shrink-0 mt-0.5">
                                <i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-[#1F3D5A] text-[16px] mb-1">{title}</h3>
                                <p class="text-[#4A4A4A] text-[14px] leading-relaxed">{desc}</p>
                            </div>
                        </div>
                    </div>'''
    return html

def make_tech_pills(tech_list):
    html = ""
    for t in tech_list:
        html += f'<span class="px-4 py-2 bg-white border border-[#EDEDED] text-[#1F3D5A] text-[13px] font-bold rounded-full shadow-sm">{t}</span>\n                    '
    return html

template = """
    <!-- Service Hero -->
    <section class="relative bg-[#1F3D5A] pt-40 pb-0 text-white overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 flex flex-col lg:flex-row items-center gap-12 pb-16">
            <div class="flex-1 text-center lg:text-left">
                <div class="inline-flex items-center gap-2 bg-white/10 border border-white/20 px-4 py-1.5 rounded-full text-xs font-black uppercase tracking-[0.15em] text-[#E5B93C] mb-6">
                    <i data-lucide="{icon}" class="w-3 h-3"></i> {category}
                </div>
                <h1 class="text-4xl md:text-6xl font-black leading-tight tracking-tight mb-6">{title}</h1>
                <p class="text-xl text-white/80 max-w-2xl mb-10 leading-relaxed">{tagline}</p>
                <div class="flex flex-wrap gap-4 justify-center lg:justify-start">
                    <a href="contact.html" class="inline-flex items-center gap-2 bg-[#E5B93C] text-[#1F3D5A] font-bold px-8 py-4 rounded-xl hover:brightness-110 transition-all">
                        {cta_text} <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                    <a href="case-study.html" class="inline-flex items-center gap-2 bg-white/10 border border-white/20 text-white font-bold px-8 py-4 rounded-xl hover:bg-white/20 transition-all">
                        View Case Studies
                    </a>
                </div>
            </div>
            <div class="flex-1 relative hidden lg:block">
                <div class="rounded-[2rem] overflow-hidden shadow-2xl">
                    <img src="{hero_img}" class="w-full h-80 object-cover" alt="{title}">
                    <div class="absolute inset-0 bg-gradient-to-l from-[#1F3D5A]/60 to-transparent pointer-events-none rounded-[2rem]"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- What We Do -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="grid lg:grid-cols-2 gap-16 items-center">
                <div>
                    <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">WHAT WE DO</p>
                    <h2 class="text-4xl md:text-5xl font-black text-[#1F3D5A] mb-8 tracking-tight leading-tight">Expert {title}</h2>
                    <p class="text-[18px] text-[#4A4A4A] leading-relaxed mb-8">{what}</p>
                    <a href="contact.html" class="inline-flex items-center gap-2 font-bold text-[#2F6F73] hover:gap-4 transition-all">
                        Get a Free Consultation <i data-lucide="arrow-right" class="w-5 h-5"></i>
                    </a>
                </div>
                <div class="grid grid-cols-3 gap-4">
                    <div class="col-span-3 bg-[#1F3D5A] rounded-2xl p-8 text-white">
                        <div class="flex items-center gap-4 mb-4">
                            <div class="w-12 h-12 bg-[#E5B93C] rounded-xl flex items-center justify-center">
                                <i data-lucide="{icon}" class="w-6 h-6 text-[#1F3D5A]"></i>
                            </div>
                            <h3 class="text-xl font-bold">Why Kritox for {category}?</h3>
                        </div>
                        <div class="grid grid-cols-3 gap-6 mt-6">
                            <div class="text-center">
                                <p class="text-3xl font-black text-[#E5B93C]">50+</p>
                                <p class="text-white/70 text-sm mt-1">Projects Delivered</p>
                            </div>
                            <div class="text-center border-x border-white/20">
                                <p class="text-3xl font-black text-[#E5B93C]">5+</p>
                                <p class="text-white/70 text-sm mt-1">Years Experience</p>
                            </div>
                            <div class="text-center">
                                <p class="text-3xl font-black text-[#E5B93C]">100%</p>
                                <p class="text-white/70 text-sm mt-1">Client Satisfaction</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Key Features -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <p class="text-[12px] font-black text-[#1F3D5A] uppercase tracking-[0.2em] mb-4">CAPABILITIES</p>
                <h2 class="text-4xl md:text-5xl font-black text-[#1F3D5A] tracking-tight">What's included</h2>
            </div>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {features_html}
            </div>
        </div>
    </section>

    <!-- Tech Stack -->
    <section class="bg-white py-20 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 text-center">
            <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-6">TECH STACK</p>
            <h2 class="text-3xl font-black text-[#1F3D5A] mb-10">Tools & Technologies</h2>
            <div class="flex flex-wrap justify-center gap-3">
                    {tech_pills}
            </div>
        </div>
    </section>

    <!-- Process Steps -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <p class="text-[12px] font-black text-[#1F3D5A] uppercase tracking-[0.2em] mb-4">OUR PROCESS</p>
                <h2 class="text-4xl md:text-5xl font-black text-[#1F3D5A] tracking-tight">How We Work</h2>
            </div>
            <div class="grid md:grid-cols-4 gap-8">
                <div class="text-center">
                    <div class="w-14 h-14 rounded-2xl bg-[#1F3D5A] flex items-center justify-center mx-auto mb-5">
                        <i data-lucide="lightbulb" class="w-6 h-6 text-[#E5B93C]"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">Discovery</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We map your requirements, user journeys, and technical constraints.</p>
                </div>
                <div class="text-center">
                    <div class="w-14 h-14 rounded-2xl bg-[#2F6F73] flex items-center justify-center mx-auto mb-5">
                        <i data-lucide="pen-tool" class="w-6 h-6 text-white"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">Design & Prototype</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">Architecture blueprints and interactive prototypes before a line is coded.</p>
                </div>
                <div class="text-center">
                    <div class="w-14 h-14 rounded-2xl bg-[#1F3D5A] flex items-center justify-center mx-auto mb-5">
                        <i data-lucide="code-2" class="w-6 h-6 text-[#E5B93C]"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">Build & Test</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">Agile sprints with continuous integration, code review, and QA.</p>
                </div>
                <div class="text-center">
                    <div class="w-14 h-14 rounded-2xl bg-[#E5B93C] flex items-center justify-center mx-auto mb-5">
                        <i data-lucide="rocket" class="w-6 h-6 text-[#1F3D5A]"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">Launch & Support</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">Zero-downtime deployment with ongoing monitoring and maintenance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="bg-[#1F3D5A] py-24 text-center">
        <div class="max-w-4xl mx-auto px-6 md:px-10">
            <h2 class="text-4xl md:text-5xl font-black text-white mb-6 tracking-tight">Ready to start your {category} project?</h2>
            <p class="text-lg text-white/70 mb-10 max-w-2xl mx-auto">Let's turn your vision into a high-performing product. Our team is ready to jump in.</p>
            <div class="flex flex-wrap gap-4 justify-center">
                <a href="contact.html" class="inline-flex items-center gap-2 bg-[#E5B93C] text-[#1F3D5A] font-bold px-8 py-4 rounded-xl hover:brightness-110 transition-all">
                    {cta_text} <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
                <a href="case-study.html" class="inline-flex items-center gap-2 bg-white/10 border border-white/20 text-white font-bold px-8 py-4 rounded-xl hover:bg-white/20 transition-all">
                    See Our Work
                </a>
            </div>
        </div>
    </section>
"""

for page in pages:
    features_html = make_feature_html(page['features'])
    tech_pills = make_tech_pills(page['tech'])
    content = template.format(
        slug=page['slug'],
        category=page['category'],
        title=page['title'],
        tagline=page['tagline'],
        icon=page['icon'],
        accent=page['accent'],
        hero_img=page['hero_img'],
        what=page['what'],
        features_html=features_html,
        tech_pills=tech_pills,
        cta_text=page['cta_text'],
    )
    with open(f"_build_scripts/{page['slug']}_content.html", 'w') as f:
        f.write(content)
    print(f"Created {page['slug']}_content.html")

