import re

with open('services.html', 'r') as f:
    content = f.read()

# The new body sections
new_sections = """
    <!-- Services Hero Section -->
    <section class="inner-hero border-b border-[#EDEDED] relative py-12 md:py-16">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-[#2F6F73] rounded-full blur-[150px] opacity-[0.1]"></div>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center relative z-10">
            <div>
                <p class="text-xs font-black uppercase tracking-[0.2em] text-[#E5B93C] mb-4">What We Do</p>
                <h1 class="font-black tracking-tight leading-[1.05] mb-6 text-[2.5rem] md:text-[3.5rem] text-[#1F3D5A]">
                    Our <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2F6F73] to-[#E5B93C]">Services.</span>
                </h1>
                <p class="text-lg text-[#4A4A4A] leading-relaxed mb-8">
                    Comprehensive digital solutions to help your business grow, innovate, and lead in the modern digital landscape. We build for the future.
                </p>
                
                <div class="flex flex-wrap items-center gap-6 mt-8">
                    <a href="contact.html" class="inline-flex items-center gap-2 font-bold text-white bg-[#1F3D5A] px-8 py-4 rounded-xl hover:bg-[#2F6F73] transition-colors">
                        Request a Quote <i data-lucide="arrow-right" class="w-5 h-5"></i>
                    </a>
                    <a href="#portfolio" class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] bg-white border border-[#EDEDED] px-8 py-4 rounded-xl hover:bg-[#FAFAFA] transition-colors">
                        Our Portfolio <i data-lucide="layout-grid" class="w-5 h-5"></i>
                    </a>
                </div>
            </div>
            <div class="relative">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1000" alt="Our Services" class="rounded-[2rem] shadow-2xl w-full h-[400px] object-cover">
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border border-[#EDEDED] flex items-center gap-4">
                    <div class="w-12 h-12 bg-[#2F6F73]/10 text-[#2F6F73] rounded-xl flex items-center justify-center shrink-0">
                        <i data-lucide="award" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <p class="text-[#1F3D5A] font-black text-xl">Top Rated</p>
                        <p class="text-[#4A4A4A] text-sm font-medium">Digital Agency</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- What Services We Provide (Dark Theme) -->
    <section class="bg-[#111111] py-24 border-b border-white/10 text-white selection-style relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black mb-6 tracking-tight text-white/40">
                    What Services <span class="text-white">We Provide</span>
                </h2>
                <p class="text-lg text-white/60 leading-relaxed max-w-3xl mx-auto">
                    From designing intuitive user experiences to building robust backend systems, we at Kritox Digital provide Design, Web Development, E-Commerce, and AI/ML services. We do not only offer services; your users are always kept in the hands of advanced design and development, allowing you to reimagine what's possible while caring for innovation, scalability, and meaningful results.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Card 1 -->
                <div class="group bg-black/40 border border-dashed border-white/20 rounded-3xl p-8 hover:bg-white/5 hover:border-white/40 transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-white/5 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="pen-tool" class="w-8 h-8 text-[#FF3B5C]"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">Design</h3>
                    <p class="text-white/60 text-sm mb-8 flex-1 leading-relaxed">
                        We take pride in designing user-friendly designs which inspires our clients by incorporating structural functionality into beautifully appealing designs.
                    </p>
                    <a href="tech/uiux.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-white/20 text-white hover:bg-white hover:text-black transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Card 2 -->
                <div class="group bg-black/40 border border-dashed border-white/20 rounded-3xl p-8 hover:bg-white/5 hover:border-white/40 transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-white/5 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="cpu" class="w-8 h-8 text-white"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">AI/ML</h3>
                    <p class="text-white/60 text-sm mb-8 flex-1 leading-relaxed">
                        Our experts deliver everything from AI/ML to advanced image and speech recognition systems. Innovation starts with intelligent systems.
                    </p>
                    <a href="tech/ai.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-white/20 text-white hover:bg-white hover:text-black transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Card 3 -->
                <div class="group bg-black/40 border border-dashed border-white/20 rounded-3xl p-8 hover:bg-white/5 hover:border-white/40 transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-white/5 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="monitor" class="w-8 h-8 text-[#00E5FF]"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">Web Dev</h3>
                    <p class="text-white/60 text-sm mb-8 flex-1 leading-relaxed">
                        We build robust and highly scalable web architectures that perform well under heavy loads, using modern frameworks like React and Node.js.
                    </p>
                    <a href="tech/react.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-white/20 text-white hover:bg-white hover:text-black transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Card 4 -->
                <div class="group bg-black/40 border border-dashed border-white/20 rounded-3xl p-8 hover:bg-white/5 hover:border-white/40 transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-white/5 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="shopping-cart" class="w-8 h-8 text-[#FFC107]"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">E-Commerce</h3>
                    <p class="text-white/60 text-sm mb-8 flex-1 leading-relaxed">
                        End-to-end ecommerce solutions designed for massive scale and secure transactions to boost your online sales globally.
                    </p>
                    <a href="contact.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-white/20 text-white hover:bg-white hover:text-black transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Hire a Dedicated Resource -->
    <section class="bg-brand-base py-20 relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                        <path d="M 40 0 L 0 0 0 40" fill="none" stroke="white" stroke-width="1"/>
                    </pattern>
                </defs>
                <rect width="100%" height="100%" fill="url(#grid)" />
            </svg>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
            <div class="max-w-2xl text-center md:text-left">
                <h2 class="text-3xl md:text-4xl font-black text-white mb-4">Hire a Dedicated Resource</h2>
                <p class="text-lg text-white/90">
                    Extend your engineering capacity immediately by hiring our pre-vetted, elite-level developers. Save on hiring costs and start building within days.
                </p>
            </div>
            <a href="career.html" class="shrink-0 inline-flex items-center gap-2 bg-brand-dark text-white font-bold text-lg px-8 py-4 rounded-xl hover:bg-white hover:text-brand-dark transition-colors shadow-xl">
                Hire Now <i data-lucide="arrow-right" class="w-5 h-5"></i>
            </a>
        </div>
    </section>

    <!-- Categories of Services -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">TECHNOLOGIES</p>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Categories of Services</h2>
                <p class="text-lg text-[#4A4A4A] leading-relaxed">
                    We offer a wide range of services spanning multiple tech stacks. Choose the right category to explore how we can help your business.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Frontend -->
                <div class="bg-white p-8 rounded-[2rem] border border-[#EDEDED] hover:shadow-xl transition-all duration-300">
                    <div class="w-14 h-14 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6">
                        <i data-lucide="layout" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Frontend Development</h3>
                    <p class="text-[#4A4A4A] mb-6">Creating highly interactive and fast user interfaces using modern frameworks.</p>
                    <ul class="space-y-3 mb-8">
                        <li><a href="tech/react.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> React.js Development</a></li>
                        <li><a href="tech/angular.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> Angular Development</a></li>
                        <li><a href="tech/vue.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> Vue.js Development</a></li>
                    </ul>
                </div>

                <!-- Backend -->
                <div class="bg-white p-8 rounded-[2rem] border border-[#EDEDED] hover:shadow-xl transition-all duration-300">
                    <div class="w-14 h-14 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6">
                        <i data-lucide="server" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Backend Development</h3>
                    <p class="text-[#4A4A4A] mb-6">Building scalable APIs, microservices, and secure databases for your platform.</p>
                    <ul class="space-y-3 mb-8">
                        <li><a href="tech/node.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> Node.js Development</a></li>
                        <li><a href="tech/python.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> Python Development</a></li>
                        <li><a href="tech/laravel.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> Laravel Development</a></li>
                    </ul>
                </div>

                <!-- Mobile & Cloud -->
                <div class="bg-white p-8 rounded-[2rem] border border-[#EDEDED] hover:shadow-xl transition-all duration-300">
                    <div class="w-14 h-14 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6">
                        <i data-lucide="smartphone" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Mobile & Cloud</h3>
                    <p class="text-[#4A4A4A] mb-6">Cross-platform mobile apps and cloud-native deployments.</p>
                    <ul class="space-y-3 mb-8">
                        <li><a href="tech/mobile.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> React Native & Flutter</a></li>
                        <li><a href="tech/aws.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> AWS & GCP Solutions</a></li>
                        <li><a href="tech/cicd.html" class="flex items-center gap-2 text-[#1F3D5A] font-semibold hover:text-[#2F6F73]"><i data-lucide="chevron-right" class="w-4 h-4"></i> CI/CD & DevOps</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="py-24 bg-white overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 mb-16">
            <!-- Header -->
            <div class="text-center max-w-4xl mx-auto">
                <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">CASE STUDIES</p>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Our Portfolio</h2>
                <p class="text-lg text-[#4A4A4A] leading-relaxed max-w-3xl mx-auto">
                    Explore our latest projects and see how we've helped businesses achieve their digital goals through innovative design and development.
                </p>
            </div>
        </div>

        <div class="relative">
            <div class="pointer-events-none absolute left-0 top-0 h-full w-24 md:w-40 z-10" style="background: linear-gradient(to right, #ffffff 0%, rgba(255,255,255,0) 100%);"></div>

            <div id="portfolio-carousel" class="bleed-carousel-container carousel-container carousel-seamless carousel-no-hover-pause flex gap-6 overflow-x-auto snap-x snap-mandatory no-scrollbar pb-10 cursor-grab active:cursor-grabbing">
                <!-- Item 1 -->
                <div class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-[0_8px_28px_rgba(31,61,90,0.08)] hover:shadow-xl hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Financial Services" draggable="false" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] md:text-[32px] font-bold leading-tight mb-4">Fintech Mobile<br>Application</h3>
                        <div class="space-y-2 mb-8">
                            <p class="text-[14px]"><span class="font-bold text-[16px]">40%</span> <span class="text-white/80">Active Users</span></p>
                            <p class="text-[14px]"><span class="font-bold text-[16px]">$5B+</span> <span class="text-white/80">Transactions Processed</span></p>
                        </div>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW
                            <div class="flex items-center ml-4 group-hover:translate-x-2 transition-transform duration-300">
                                <div class="w-8 h-[2px] bg-white -mr-1"></div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><path d="m9 18 6-6-6-6"/></svg>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Item 2 -->
                <div class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-[0_8px_28px_rgba(31,61,90,0.08)] hover:shadow-xl hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Enterprise SaaS" draggable="false" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] md:text-[32px] font-bold leading-tight mb-4">Enterprise SaaS<br>Platform</h3>
                        <div class="space-y-2 mb-8">
                            <p class="text-[14px]"><span class="font-bold text-[16px]">500+</span> <span class="text-white/80">B2B Integrations</span></p>
                            <p class="text-[14px]"><span class="font-bold text-[16px]">10M+</span> <span class="text-white/80">Daily API Calls</span></p>
                        </div>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW
                            <div class="flex items-center ml-4 group-hover:translate-x-2 transition-transform duration-300">
                                <div class="w-8 h-[2px] bg-white -mr-1"></div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><path d="m9 18 6-6-6-6"/></svg>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[460px] md:min-h-[500px] relative rounded-[1rem] overflow-hidden group cursor-pointer shadow-[0_8px_28px_rgba(31,61,90,0.08)] hover:shadow-xl hover:-translate-y-2 transition-all duration-500">
                    <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800" alt="E-Commerce Web Portal" draggable="false" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 select-none">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>
                    <div class="absolute inset-0 p-6 md:p-8 flex flex-col justify-end text-white z-10">
                        <h3 class="text-[28px] md:text-[32px] font-bold leading-tight mb-4">E-Commerce Web<br>Portal</h3>
                        <div class="space-y-2 mb-8">
                            <p class="text-[14px]"><span class="font-bold text-[16px]">250K+</span> <span class="text-white/80">Monthly Orders</span></p>
                            <p class="text-[14px]"><span class="font-bold text-[16px]">45%</span> <span class="text-white/80">Conversion Increase</span></p>
                        </div>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW
                            <div class="flex items-center ml-4 group-hover:translate-x-2 transition-transform duration-300">
                                <div class="w-8 h-[2px] bg-white -mr-1"></div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><path d="m9 18 6-6-6-6"/></svg>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="max-w-7xl mx-auto px-6 md:px-10 mt-6 relative z-20 pointer-events-auto flex items-center justify-between">
                <div class="flex gap-3">
                    <button id="portfolio-carousel-prev" class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-[#1F3D5A] hover:bg-[#2F6F73] hover:text-white hover:border-[#2F6F73] transition-all group">
                        <svg class="w-5 h-5 transition-transform group-hover:-translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                    </button>
                    <button id="portfolio-carousel-next" class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-[#1F3D5A] hover:bg-[#2F6F73] hover:text-white hover:border-[#2F6F73] transition-all group">
                        <svg class="w-5 h-5 transition-transform group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                    </button>
                </div>
                <a href="case-studies/index.html" class="inline-flex items-center justify-center gap-2 px-8 py-3 bg-[#1F3D5A] text-white font-bold rounded-2xl hover:bg-[#2F6F73] transition-colors shadow-lg shadow-[#1F3D5A]/20 text-sm">View All <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><path d="m9 18 6-6-6-6"/></svg></a>
            </div>
        </div>
    </section>

    <!-- CTA Having Quick Form -->
    <section class="bg-[#FAFAFA] py-24 border-t border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="bg-white rounded-[3rem] p-10 md:p-16 shadow-xl border border-[#EDEDED] relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-br from-[#2F6F73]/5 to-transparent"></div>
                
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 relative z-10">
                    <div>
                        <p class="text-sm font-bold tracking-widest uppercase text-[#2F6F73] mb-4">Let's Connect</p>
                        <h2 class="text-4xl md:text-5xl font-black text-[#1F3D5A] mb-6">Have a Great Idea?<br>Tell us about it.</h2>
                        <p class="text-lg text-[#4A4A4A] mb-8 leading-relaxed">
                            Share your project details with us, and our experts will get back to you with a free consultation and project estimate within 24 hours.
                        </p>
                        <div class="space-y-6 mb-8">
                            <div class="flex items-center gap-4">
                                <div class="w-12 h-12 rounded-full bg-[#FAFAFA] flex items-center justify-center border border-[#EDEDED] shrink-0">
                                    <i data-lucide="mail" class="w-5 h-5 text-[#2F6F73]"></i>
                                </div>
                                <div>
                                    <p class="text-sm text-[#4A4A4A] font-semibold">Email Us</p>
                                    <a href="mailto:info@kritox.com" class="text-lg font-bold text-[#1F3D5A]">info@kritox.com</a>
                                </div>
                            </div>
                            <div class="flex items-center gap-4">
                                <div class="w-12 h-12 rounded-full bg-[#FAFAFA] flex items-center justify-center border border-[#EDEDED] shrink-0">
                                    <i data-lucide="phone" class="w-5 h-5 text-[#2F6F73]"></i>
                                </div>
                                <div>
                                    <p class="text-sm text-[#4A4A4A] font-semibold">Call Us</p>
                                    <a href="tel:+123456789" class="text-lg font-bold text-[#1F3D5A]">+1 234 567 89</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white p-8 rounded-3xl shadow-sm border border-[#EDEDED]">
                        <form class="space-y-6">
                            <div>
                                <label class="block text-sm font-bold text-[#1F3D5A] mb-2">Name</label>
                                <input type="text" class="w-full px-5 py-4 rounded-xl border border-[#EDEDED] bg-[#FAFAFA] focus:bg-white focus:border-[#2F6F73] focus:outline-none transition-colors" placeholder="John Doe">
                            </div>
                            <div>
                                <label class="block text-sm font-bold text-[#1F3D5A] mb-2">Email</label>
                                <input type="email" class="w-full px-5 py-4 rounded-xl border border-[#EDEDED] bg-[#FAFAFA] focus:bg-white focus:border-[#2F6F73] focus:outline-none transition-colors" placeholder="john@example.com">
                            </div>
                            <div>
                                <label class="block text-sm font-bold text-[#1F3D5A] mb-2">Project Details</label>
                                <textarea rows="4" class="w-full px-5 py-4 rounded-xl border border-[#EDEDED] bg-[#FAFAFA] focus:bg-white focus:border-[#2F6F73] focus:outline-none transition-colors" placeholder="Tell us about your requirements..."></textarea>
                            </div>
                            <button type="submit" class="w-full py-4 bg-[#1F3D5A] text-white font-bold text-lg rounded-xl hover:bg-[#2F6F73] transition-colors shadow-lg shadow-[#1F3D5A]/20">
                                Submit Request
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Extract everything before the Hero Section and everything from Footer onwards
top_part = content.split('<!-- Services Hero Section -->')[0]
bottom_part = '<!-- Footer -->' + content.split('<!-- Footer -->')[1]

new_content = top_part + new_sections + '\n' + bottom_part

with open('services.html', 'w') as f:
    f.write(new_content)

print("Updated services.html successfully!")
