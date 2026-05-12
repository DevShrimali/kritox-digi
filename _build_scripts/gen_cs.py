import os

template = """    <!-- 1. Hero Header -->
    <section class="bg-white pt-40 pb-12 md:pt-52 md:pb-16 border-b border-[#EDEDED]">
        <div class="max-w-5xl mx-auto px-6 md:px-10 text-center">
            <div class="inline-block px-4 py-1.5 border border-[#1F3D5A] text-[#1F3D5A] text-xs font-bold uppercase tracking-[0.15em] rounded-full mb-6 hover:bg-[#1F3D5A] hover:text-white transition-colors cursor-pointer">
                Case Study
            </div>
            <h1 class="font-black text-4xl md:text-5xl lg:text-6xl tracking-tight leading-[1.1] mb-8 text-[#1A1A1A] max-w-4xl mx-auto" style="font-family: 'Plus Jakarta Sans', sans-serif;">
                {TITLE}
            </h1>
            <p class="text-xl text-[#4A4A4A] max-w-3xl mx-auto leading-relaxed">
                {SUBTITLE}
            </p>
        </div>
    </section>

    <!-- 2. Large Featured Image -->
    <section class="bg-white pt-16 pb-16">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="relative rounded-[2rem] overflow-hidden shadow-[0_20px_50px_rgba(31,61,90,0.1)] group">
                <img src="{IMAGE}?auto=format&fit=crop&q=80" alt="{TITLE}" class="w-full h-[500px] md:h-[700px] object-cover group-hover:scale-105 transition-transform duration-1000 ease-out">
                <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent pointer-events-none"></div>
            </div>
        </div>
    </section>

    <!-- Content & Sidebar -->
    <section class="bg-white pb-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-20">
            
            <!-- Left: Main Article (70%) -->
            <div class="lg:col-span-8">
                <article class="text-[#2A2A2A] text-lg leading-[1.8] font-medium">
                    
                    <!-- 3. The Challenge -->
                    <h2 class="text-3xl md:text-4xl font-black text-[#1A1A1A] mb-8 tracking-tight">The Challenge</h2>
                    <p class="mb-8 text-[#4A4A4A]">
                        {CHALLENGE_1}
                    </p>
                    <p class="mb-16 text-[#4A4A4A]">
                        {CHALLENGE_2}
                    </p>

                    <!-- Stylized Pull Quote -->
                    <blockquote class="relative my-16 p-10 bg-[#FAFAFA] rounded-2xl border-l-4 border-[#2F6F73]">
                        <i data-lucide="quote" class="w-10 h-10 text-[#2F6F73]/20 absolute top-6 left-6"></i>
                        <p class="relative z-10 text-xl md:text-2xl text-[#1F3D5A] font-bold italic leading-relaxed">
                            {QUOTE}
                        </p>
                    </blockquote>

                    <!-- 4. The Solution -->
                    <h2 class="text-3xl md:text-4xl font-black text-[#1A1A1A] mt-16 mb-8 tracking-tight">The Solution</h2>
                    <p class="mb-8 text-[#4A4A4A]">
                        {SOLUTION_1}
                    </p>
                    <p class="mb-16 text-[#4A4A4A]">
                        {SOLUTION_2}
                    </p>

                    <!-- 5. Business Impact & Results (Stats Grid) -->
                    <h2 class="text-3xl md:text-4xl font-black text-[#1A1A1A] mt-16 mb-8 tracking-tight">Business Impact</h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
                        <div class="bg-[#FAFAFA] p-8 rounded-2xl border border-[#EDEDED]">
                            <p class="text-4xl font-black text-[#2F6F73] mb-2">{STAT_1_VAL}</p>
                            <p class="text-[#4A4A4A] font-bold text-sm uppercase tracking-wider">{STAT_1_LABEL}</p>
                        </div>
                        <div class="bg-[#FAFAFA] p-8 rounded-2xl border border-[#EDEDED]">
                            <p class="text-4xl font-black text-[#E5B93C] mb-2">{STAT_2_VAL}</p>
                            <p class="text-[#4A4A4A] font-bold text-sm uppercase tracking-wider">{STAT_2_LABEL}</p>
                        </div>
                        <div class="bg-[#FAFAFA] p-8 rounded-2xl border border-[#EDEDED]">
                            <p class="text-4xl font-black text-[#1F3D5A] mb-2">{STAT_3_VAL}</p>
                            <p class="text-[#4A4A4A] font-bold text-sm uppercase tracking-wider">{STAT_3_LABEL}</p>
                        </div>
                    </div>

                </article>
            </div>
            
            <!-- Right: Project Sidebar (30%) -->
            <aside class="lg:col-span-4">
                <div class="sticky top-32">
                    <div class="bg-[#FAFAFA] p-8 rounded-2xl border border-[#EDEDED] shadow-sm mb-8">
                        <h3 class="text-xs font-black uppercase tracking-[0.2em] text-[#1A1A1A] mb-8 pb-4 border-b border-[#EDEDED]">Project Overview</h3>
                        
                        <div class="space-y-6">
                            <div>
                                <p class="text-xs font-bold uppercase tracking-wider text-[#4A4A4A] mb-1">Client</p>
                                <p class="text-[#1A1A1A] font-semibold">{CLIENT_NAME}</p>
                            </div>
                            <div>
                                <p class="text-xs font-bold uppercase tracking-wider text-[#4A4A4A] mb-1">Industry</p>
                                <p class="text-[#1A1A1A] font-semibold">{INDUSTRY}</p>
                            </div>
                            <div>
                                <p class="text-xs font-bold uppercase tracking-wider text-[#4A4A4A] mb-1">Services Provided</p>
                                <ul class="space-y-2 mt-2">
                                    <li class="flex items-center gap-2 text-sm text-[#1A1A1A] font-medium"><i data-lucide="check-circle-2" class="w-4 h-4 text-[#2F6F73]"></i> UI/UX Design</li>
                                    <li class="flex items-center gap-2 text-sm text-[#1A1A1A] font-medium"><i data-lucide="check-circle-2" class="w-4 h-4 text-[#2F6F73]"></i> {SERVICE_2}</li>
                                    <li class="flex items-center gap-2 text-sm text-[#1A1A1A] font-medium"><i data-lucide="check-circle-2" class="w-4 h-4 text-[#2F6F73]"></i> {SERVICE_3}</li>
                                </ul>
                            </div>
                            <div>
                                <p class="text-xs font-bold uppercase tracking-wider text-[#4A4A4A] mb-2">Core Tech Stack</p>
                                <div class="flex flex-wrap gap-2">
                                    <span class="px-3 py-1 bg-white border border-[#EDEDED] text-[#1A1A1A] text-[11px] font-bold rounded-md">{TECH_1}</span>
                                    <span class="px-3 py-1 bg-white border border-[#EDEDED] text-[#1A1A1A] text-[11px] font-bold rounded-md">{TECH_2}</span>
                                    <span class="px-3 py-1 bg-white border border-[#EDEDED] text-[#1A1A1A] text-[11px] font-bold rounded-md">{TECH_3}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-[#1F3D5A] p-8 rounded-2xl shadow-sm text-white">
                        <h4 class="font-black text-2xl mb-3">Want similar results?</h4>
                        <p class="text-white/80 text-sm mb-6">Let's discuss how we can transform your digital infrastructure.</p>
                        <a href="contact.html" class="block text-center w-full px-4 py-3 rounded-lg bg-[#E5B93C] text-[#1F3D5A] font-bold hover:brightness-110 transition-colors">Start a Project</a>
                    </div>
                </div>
            </aside>
        </div>
    </section>

    <!-- 6. More Case Studies Carousel -->
    <section class="py-24 bg-[#FAFAFA] overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 mb-16">
            <div class="text-center max-w-4xl mx-auto">
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6 tracking-tight">More Case Studies</h2>
            </div>
        </div>

        <div class="relative">
            <div class="pointer-events-none absolute left-0 top-0 h-full w-24 md:w-40 z-10"
                style="background: linear-gradient(to right, #FAFAFA 0%, rgba(250,250,250,0) 100%);"></div>

            <div class="bleed-carousel-container carousel-container carousel-seamless flex gap-6 overflow-x-auto snap-x snap-mandatory no-scrollbar pb-10 cursor-grab">
                <!-- Item 1 -->
                <a href="cs-fintech.html" class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-[0_8px_28px_rgba(31,61,90,0.08)] hover:shadow-xl hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Financial Services" draggable="false" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] md:text-[32px] font-bold leading-tight mb-4">Fintech Mobile<br>Application</h3>
                        <div class="space-y-2 mb-8">
                            <p class="text-[14px]"><span class="font-bold text-[16px]">40%</span> <span class="text-white/80">Active Users</span></p>
                        </div>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW
                            <div class="flex items-center ml-4 group-hover:translate-x-2 transition-transform duration-300">
                                <div class="w-8 h-[2px] bg-white -mr-1"></div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><path d="m9 18 6-6-6-6"/></svg>
                            </div>
                        </div>
                    </div>
                </a>

                <!-- Item 2 -->
                <a href="cs-saas.html" class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-[0_8px_28px_rgba(31,61,90,0.08)] hover:shadow-xl hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Affordable & Safe Housing" draggable="false" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] md:text-[32px] font-bold leading-tight mb-4">Enterprise SaaS<br>Platform</h3>
                        <div class="space-y-2 mb-8">
                            <p class="text-[14px]"><span class="font-bold text-[16px]">3x</span> <span class="text-white/80">Efficiency</span></p>
                        </div>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW
                            <div class="flex items-center ml-4 group-hover:translate-x-2 transition-transform duration-300">
                                <div class="w-8 h-[2px] bg-white -mr-1"></div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><path d="m9 18 6-6-6-6"/></svg>
                            </div>
                        </div>
                    </div>
                </a>
                
                <!-- Item 3 -->
                <a href="cs-ecommerce.html" class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-[0_8px_28px_rgba(31,61,90,0.08)] hover:shadow-xl hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Visa, Consular & Citizen Services" draggable="false" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] md:text-[32px] font-bold leading-tight mb-4">E-Commerce Web<br>Portal</h3>
                        <div class="space-y-2 mb-8">
                            <p class="text-[14px]"><span class="font-bold text-[16px]">45%</span> <span class="text-white/80">Conversion Rate</span></p>
                        </div>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW
                            <div class="flex items-center ml-4 group-hover:translate-x-2 transition-transform duration-300">
                                <div class="w-8 h-[2px] bg-white -mr-1"></div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><path d="m9 18 6-6-6-6"/></svg>
                            </div>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </section>
"""

case_studies = [
    {
        "id": "cs-fintech",
        "title": "Fintech Mobile Application",
        "subtitle": "Revolutionizing Digital Banking with a modern, high-performance mobile application.",
        "image": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg",
        "challenge_1": "Our client, a leading financial institution, was facing severe challenges with their legacy mobile application. The app was slow, unintuitive, and suffered from frequent downtime, leading to a significant drop in user engagement and satisfaction.",
        "challenge_2": "They needed a complete overhaul to regain their competitive edge in the rapidly evolving fintech landscape, requiring strict adherence to financial security compliances and the ability to process thousands of transactions per second.",
        "quote": "\"Kritox transformed our digital presence. Our customers now enjoy a seamless banking experience that has directly increased our daily active usage.\"",
        "solution_1": "We partnered with their internal teams to design and develop a robust, scalable, and highly intuitive mobile application from the ground up.",
        "solution_2": "Utilizing React Native for a seamless cross-platform experience, and a modern microservices architecture on AWS, we ensured lightning-fast performance and bank-grade security. Real-time sockets were implemented for instant transaction alerts.",
        "stat_1_val": "40%",
        "stat_1_label": "Active Users",
        "stat_2_val": "$5B+",
        "stat_2_label": "Processed",
        "stat_3_val": "99.99%",
        "stat_3_label": "Uptime",
        "client_name": "GlobalBank Inc.",
        "industry": "Financial Services",
        "service_2": "Mobile Development",
        "service_3": "Cloud Architecture",
        "tech_1": "React Native",
        "tech_2": "Node.js",
        "tech_3": "AWS"
    },
    {
        "id": "cs-saas",
        "title": "Enterprise SaaS Platform",
        "subtitle": "Unifying operational workflows for a massive global enterprise scale.",
        "image": "https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg",
        "challenge_1": "The client's existing B2B platform was fragmented across multiple legacy systems, making cross-departmental data sharing nearly impossible.",
        "challenge_2": "Operational bottlenecks were costing the company millions annually in wasted hours. They needed a centralized, multi-tenant SaaS solution capable of integrating with over 500 third-party APIs seamlessly.",
        "quote": "\"The new SaaS platform reduced our internal reporting times from days to mere seconds.\"",
        "solution_1": "We engineered a highly scalable multi-tenant architecture using Next.js for the frontend and Go for the backend microservices, prioritizing speed and API reliability.",
        "solution_2": "A custom GraphQL gateway was implemented to federate data across all 500+ integrations, providing a single, unified dashboard for enterprise managers to oversee global operations in real-time.",
        "stat_1_val": "500+",
        "stat_1_label": "Integrations",
        "stat_2_val": "10M+",
        "stat_2_label": "API Calls / Day",
        "stat_3_val": "3x",
        "stat_3_label": "Efficiency",
        "client_name": "OpFlow Dynamics",
        "industry": "B2B SaaS",
        "service_2": "Backend Engineering",
        "service_3": "API Gateway Design",
        "tech_1": "Next.js",
        "tech_2": "Golang",
        "tech_3": "GraphQL"
    },
    {
        "id": "cs-ecommerce",
        "title": "E-Commerce Web Portal",
        "subtitle": "Driving conversion rates through a lightning-fast headless commerce architecture.",
        "image": "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg",
        "challenge_1": "A premium retail brand was struggling with a monolithic Magento setup that took over 6 seconds to load pages during high-traffic flash sales.",
        "challenge_2": "The slow load times resulted in massive cart abandonment rates. They needed an architecture that could handle sudden massive spikes in traffic while delivering a sub-second page load globally.",
        "quote": "\"Moving to a headless architecture was the best business decision we made. Our conversion rates skyrocketed overnight.\"",
        "solution_1": "We decoupled their frontend from the backend logic by implementing a modern Headless Commerce approach.",
        "solution_2": "Using Shopify Plus as the headless backend and a custom React frontend deployed on the edge via Vercel, we achieved instant page loads. We also implemented advanced caching and a CDN to serve media globally without latency.",
        "stat_1_val": "250K+",
        "stat_1_label": "Monthly Orders",
        "stat_2_val": "1.5s",
        "stat_2_label": "Load Time",
        "stat_3_val": "45%",
        "stat_3_label": "Conv. Increase",
        "client_name": "Luxe Retail",
        "industry": "E-Commerce",
        "service_2": "Frontend Engineering",
        "service_3": "Headless Migration",
        "tech_1": "React",
        "tech_2": "Shopify Plus",
        "tech_3": "Vercel"
    },
    {
        "id": "cs-cloud",
        "title": "Cloud Migration & DevOps",
        "subtitle": "Zero-downtime migration of massive on-premise infrastructure to the cloud.",
        "image": "https://images.pexels.com/photos/1779487/pexels-photo-1779487.jpeg",
        "challenge_1": "A healthcare provider was operating on costly, aging on-premise servers that were becoming increasingly difficult to maintain and secure.",
        "challenge_2": "They needed to migrate their entire infrastructure to the cloud to reduce hardware costs and improve scalability, but strict healthcare compliance meant they couldn't afford a single minute of downtime or data loss during the transition.",
        "quote": "\"The migration was so flawless our internal staff didn't even notice when the switch to the cloud occurred.\"",
        "solution_1": "We designed a phased, zero-downtime migration strategy utilizing advanced containerization and CI/CD pipelines.",
        "solution_2": "By containerizing their applications with Docker and orchestrating them via Kubernetes on Google Cloud, we created a redundant environment. Traffic was slowly routed to the new cloud infrastructure ensuring zero interruption to patient services.",
        "stat_1_val": "40%",
        "stat_1_label": "Servers Migrated",
        "stat_2_val": "Zero",
        "stat_2_label": "Downtime",
        "stat_3_val": "$10M+",
        "stat_3_label": "Saved",
        "client_name": "HealthCorp Data",
        "industry": "Healthcare Tech",
        "service_2": "Cloud Migration",
        "service_3": "DevOps Setup",
        "tech_1": "Docker",
        "tech_2": "Kubernetes",
        "tech_3": "GCP"
    }
]

for cs in case_studies:
    content = template
    for key, value in cs.items():
        content = content.replace(f"{{{key.upper()}}}", value)
    
    with open(f"_build_scripts/{cs['id']}_content.html", "w") as f:
        f.write(content)

print("Generated case study details templates.")
