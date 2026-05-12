import os

# --- TEMPLATE 1: FRONTEND & MOBILE (Visual, UI-focused) ---
template_frontend = """    <!-- Frontend Hero Section -->
    <section class="relative bg-white text-[#1F3D5A] pt-40 pb-20 md:pt-48 md:pb-24 border-b border-[#EDEDED] overflow-hidden">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-[#2F6F73] rounded-full blur-[150px] opacity-[0.1]"></div>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
                <p class="text-xs font-black uppercase tracking-[0.2em] text-[#E5B93C] mb-4">Frontend Engineering</p>
                <h1 class="font-black text-5xl md:text-7xl tracking-tight leading-[1.05] mb-6 text-[#1F3D5A]">
                    {TITLE} <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2F6F73] to-[#E5B93C]">Development.</span>
                </h1>
                <p class="text-lg text-[#4A4A4A] leading-relaxed mb-8">
                    {DESC}
                </p>
                <a href="contact.html" class="inline-flex items-center gap-2 font-bold text-white bg-[#1F3D5A] px-8 py-4 rounded-xl hover:bg-[#2F6F73] transition-colors">
                    Start Your Project <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </a>
            </div>
            <div class="relative">
                <img src="{IMAGE}?auto=format&fit=crop&q=80" alt="{TITLE}" class="rounded-[2rem] shadow-2xl w-full h-[500px] object-cover">
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border border-[#EDEDED] flex items-center gap-4">
                    <div class="w-12 h-12 bg-[#2F6F73]/10 text-[#2F6F73] rounded-xl flex items-center justify-center shrink-0">
                        <i data-lucide="layout" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <p class="text-[#1F3D5A] font-black text-xl">Pixel-Perfect</p>
                        <p class="text-[#4A4A4A] text-sm font-medium">UI/UX Delivery</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Component Showcase Grid -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-12 text-center">Core Capabilities</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-white p-8 rounded-2xl border border-[#EDEDED]">
                    <i data-lucide="smartphone" class="w-8 h-8 text-[#E5B93C] mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">Responsive Design</h3>
                    <p class="text-[#4A4A4A]">Fluid interfaces that work flawlessly across all devices and screen sizes.</p>
                </div>
                <div class="bg-white p-8 rounded-2xl border border-[#EDEDED]">
                    <i data-lucide="zap" class="w-8 h-8 text-[#2F6F73] mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">State Management</h3>
                    <p class="text-[#4A4A4A]">Complex global state handling for real-time applications.</p>
                </div>
                <div class="bg-white p-8 rounded-2xl border border-[#EDEDED]">
                    <i data-lucide="mouse-pointer-click" class="w-8 h-8 text-[#1F3D5A] mb-4"></i>
                    <h3 class="text-xl font-bold mb-3">Micro-Interactions</h3>
                    <p class="text-[#4A4A4A]">Engaging animations and transitions that delight users.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Visual Portfolio Banner -->
    <section class="bg-[#1F3D5A] py-24 text-white text-center">
        <div class="max-w-4xl mx-auto px-6">
            <h2 class="text-3xl md:text-5xl font-black mb-8">Ready to elevate your user experience?</h2>
            <p class="text-white/70 text-lg mb-10">Our design-engineering hybrid approach ensures no details are lost between design handoff and final production.</p>
            <a href="case-study.html" class="inline-block bg-white text-[#1F3D5A] font-bold px-8 py-4 rounded-xl hover:bg-[#FAFAFA] transition-all">View Our Portfolio</a>
        </div>
    </section>
"""

# --- TEMPLATE 2: BACKEND & INFRA (Data-focused, dark mode hero, metrics) ---
template_backend = """    <!-- Backend Hero Section (Dark) -->
    <section class="relative bg-[#1F3D5A] text-white pt-40 pb-20 md:pt-48 md:pb-24 border-b border-white/10 overflow-hidden">
        <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20"></div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10 text-center">
            <p class="text-xs font-black uppercase tracking-[0.2em] text-[#E5B93C] mb-4">Infrastructure & Backend</p>
            <h1 class="font-black text-5xl md:text-7xl tracking-tight leading-[1.05] mb-6">
                {TITLE} <span class="text-[#2F6F73]">Architecture.</span>
            </h1>
            <p class="text-lg text-white/70 max-w-3xl mx-auto leading-relaxed mb-12">
                {DESC}
            </p>
            
            <!-- Metrics Bar -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-4xl mx-auto">
                <div class="bg-white/5 border border-white/10 rounded-xl p-6 backdrop-blur-sm">
                    <p class="text-3xl font-black text-[#E5B93C] mb-1">99.99%</p>
                    <p class="text-xs font-bold text-white/60 uppercase">Uptime SLA</p>
                </div>
                <div class="bg-white/5 border border-white/10 rounded-xl p-6 backdrop-blur-sm">
                    <p class="text-3xl font-black text-[#2F6F73] mb-1"><50ms</p>
                    <p class="text-xs font-bold text-white/60 uppercase">Latency</p>
                </div>
                <div class="bg-white/5 border border-white/10 rounded-xl p-6 backdrop-blur-sm">
                    <p class="text-3xl font-black text-[#E5B93C] mb-1">10M+</p>
                    <p class="text-xs font-bold text-white/60 uppercase">Req / Min</p>
                </div>
                <div class="bg-white/5 border border-white/10 rounded-xl p-6 backdrop-blur-sm">
                    <p class="text-3xl font-black text-[#2F6F73] mb-1">AES-256</p>
                    <p class="text-xs font-bold text-white/60 uppercase">Encryption</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Architecture Diagram Mockup Section -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="order-last lg:order-first">
                <div class="bg-[#FAFAFA] p-8 rounded-[2rem] border border-[#EDEDED] relative h-[400px] flex items-center justify-center overflow-hidden">
                    <!-- Abstract diagram -->
                    <div class="absolute left-10 top-1/2 -translate-y-1/2 w-20 h-20 bg-[#1F3D5A] rounded-xl shadow-lg flex items-center justify-center text-white z-10"><i data-lucide="globe" class="w-8 h-8"></i></div>
                    <div class="w-full h-0.5 bg-[#EDEDED] absolute top-1/2 -translate-y-1/2 z-0"></div>
                    <div class="w-32 h-32 bg-[#2F6F73] rounded-full shadow-lg flex items-center justify-center text-white z-10 relative"><i data-lucide="server" class="w-12 h-12"></i></div>
                    <div class="absolute right-10 top-1/4 w-20 h-20 bg-[#E5B93C] rounded-xl shadow-lg flex items-center justify-center text-white z-10"><i data-lucide="database" class="w-8 h-8"></i></div>
                    <div class="absolute right-10 bottom-1/4 w-20 h-20 bg-[#E5B93C] rounded-xl shadow-lg flex items-center justify-center text-white z-10"><i data-lucide="cloud" class="w-8 h-8"></i></div>
                </div>
            </div>
            <div>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Scalable by Design</h2>
                <p class="text-[#4A4A4A] text-lg leading-relaxed mb-6">
                    We build resilient backend systems designed to handle massive throughput without breaking a sweat. From monolithic refactors to distributed microservices, our infrastructure patterns guarantee stability.
                </p>
                <ul class="space-y-4 mb-8">
                    <li class="flex items-center gap-3 text-[#4A4A4A] font-medium"><i data-lucide="shield-check" class="w-5 h-5 text-[#2F6F73]"></i> Enterprise-grade security</li>
                    <li class="flex items-center gap-3 text-[#4A4A4A] font-medium"><i data-lucide="database" class="w-5 h-5 text-[#2F6F73]"></i> ACID-compliant data integrity</li>
                    <li class="flex items-center gap-3 text-[#4A4A4A] font-medium"><i data-lucide="activity" class="w-5 h-5 text-[#2F6F73]"></i> Real-time monitoring & logging</li>
                </ul>
                <a href="contact.html" class="inline-flex items-center justify-center px-8 py-4 bg-[#1F3D5A] text-white font-bold text-lg rounded-xl hover:brightness-110 transition-colors shadow-lg shadow-[#1F3D5A]/20">
                    Audit Your Infrastructure
                </a>
            </div>
        </div>
    </section>
"""

# --- TEMPLATE 3: SPECIALIZED (AI, DevOps - abstract, pipeline focused) ---
template_specialized = """    <!-- Specialized Hero Section -->
    <section class="relative bg-[#FAFAFA] text-[#1F3D5A] pt-40 pb-20 md:pt-48 md:pb-24 border-b border-[#EDEDED] overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10 text-center">
            <div class="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-white shadow-xl mb-8 border border-[#EDEDED] text-[#2F6F73]">
                <i data-lucide="cpu" class="w-10 h-10"></i>
            </div>
            <h1 class="font-black text-5xl md:text-7xl tracking-tight leading-[1.05] mb-6">
                {TITLE} <br/> <span class="text-[#2F6F73]">Solutions.</span>
            </h1>
            <p class="text-lg text-[#4A4A4A] max-w-2xl mx-auto leading-relaxed mb-10">
                {DESC}
            </p>
        </div>
    </section>

    <!-- Workflow/Pipeline Timeline -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-16 text-center">The Pipeline</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 relative">
                <div class="hidden md:block absolute top-1/2 left-0 w-full h-0.5 bg-[#EDEDED] -translate-y-1/2 z-0"></div>
                
                <div class="relative z-10 flex flex-col items-center text-center">
                    <div class="w-16 h-16 rounded-full bg-[#1F3D5A] text-white flex items-center justify-center mb-6 shadow-xl border-4 border-white">
                        <i data-lucide="code" class="w-6 h-6"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">1. Ingestion</h3>
                    <p class="text-sm text-[#4A4A4A]">Securely pulling source code or raw data into the workflow.</p>
                </div>
                
                <div class="relative z-10 flex flex-col items-center text-center">
                    <div class="w-16 h-16 rounded-full bg-[#2F6F73] text-white flex items-center justify-center mb-6 shadow-xl border-4 border-white">
                        <i data-lucide="cpu" class="w-6 h-6"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">2. Processing</h3>
                    <p class="text-sm text-[#4A4A4A]">Compiling, training models, and running automated test suites.</p>
                </div>
                
                <div class="relative z-10 flex flex-col items-center text-center">
                    <div class="w-16 h-16 rounded-full bg-[#E5B93C] text-white flex items-center justify-center mb-6 shadow-xl border-4 border-white">
                        <i data-lucide="shield-check" class="w-6 h-6"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">3. Validation</h3>
                    <p class="text-sm text-[#4A4A4A]">Security audits, QA gates, and inference validations.</p>
                </div>

                <div class="relative z-10 flex flex-col items-center text-center">
                    <div class="w-16 h-16 rounded-full bg-[#1F3D5A] text-white flex items-center justify-center mb-6 shadow-xl border-4 border-white">
                        <i data-lucide="rocket" class="w-6 h-6"></i>
                    </div>
                    <h3 class="font-bold text-[#1F3D5A] text-lg mb-2">4. Deployment</h3>
                    <p class="text-sm text-[#4A4A4A]">Zero-downtime releases to production environments.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="bg-[#1F3D5A] py-24 text-white text-center">
        <div class="max-w-3xl mx-auto px-6 md:px-10">
            <h2 class="text-3xl md:text-5xl font-black mb-6">Security First Approach</h2>
            <p class="text-white/70 text-lg mb-10 leading-relaxed">Whether it's CI/CD pipelines or AI data lakes, we enforce strict compliance, role-based access controls, and end-to-end encryption across all specialized systems.</p>
            <a href="contact.html" class="inline-block bg-white text-[#1F3D5A] font-bold px-8 py-4 rounded-xl hover:bg-[#FAFAFA] transition-all">Secure Your Systems</a>
        </div>
    </section>
"""

pages_data = [
    {
        "id": "tech-react",
        "title": "React & Next.js",
        "desc": "We specialize in crafting interactive, high-performance user interfaces and full-stack web applications using modern React and Next.js.",
        "image": "https://images.unsplash.com/photo-1633356122544-f134324a6cee",
        "template": template_frontend
    },
    {
        "id": "tech-node",
        "title": "Node & Go",
        "desc": "We build lightning-fast, highly scalable backend architectures and microservices using Node.js and Golang to power your enterprise applications.",
        "image": "https://images.unsplash.com/photo-1555099962-4199c345e5dd",
        "template": template_backend
    },
    {
        "id": "tech-databases",
        "title": "Databases",
        "desc": "Secure, optimized, and scalable data storage solutions using relational and NoSQL databases like PostgreSQL and MongoDB.",
        "image": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d",
        "template": template_backend
    },
    {
        "id": "tech-aws",
        "title": "AWS & GCP",
        "desc": "Reliable and infinitely scalable cloud infrastructure deployments, architecture, and management on AWS and Google Cloud Platform.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa",
        "template": template_backend
    },
    {
        "id": "tech-mobile",
        "title": "React Native & Flutter",
        "desc": "Cross-platform mobile application development that delivers native-like performance and stunning UX on both iOS and Android.",
        "image": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42",
        "template": template_frontend
    },
    {
        "id": "tech-ai",
        "title": "AI & ML",
        "desc": "Intelligent systems, predictive analytics, and generative AI integrations that automate workflows and unlock new business capabilities.",
        "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995",
        "template": template_specialized
    },
    {
        "id": "tech-docker",
        "title": "Docker & Kubernetes",
        "desc": "Containerized application deployments and orchestration ensuring consistent, resilient, and highly available environments.",
        "image": "https://images.unsplash.com/photo-1605745341112-85968b19335b",
        "template": template_backend
    },
    {
        "id": "tech-cicd",
        "title": "CI/CD & DevOps",
        "desc": "Automated delivery pipelines, infrastructure as code, and continuous integration to accelerate your time-to-market safely.",
        "image": "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb",
        "template": template_specialized
    }
]

for page in pages_data:
    content = page["template"].replace("{TITLE}", page["title"])
    content = content.replace("{DESC}", page["desc"])
    content = content.replace("{IMAGE}", page["image"])
    
    with open(f"_build_scripts/{page['id']}_content.html", "w") as f:
        f.write(content)

print("Generated completely customized layout HTML files.")
