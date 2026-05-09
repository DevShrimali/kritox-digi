import re

with open('index.html', 'r') as f:
    content = f.read()

# 2. Add Partner Logos
partner_section = """
    <!-- Partner Logos Section -->
    <section class="py-16 bg-[#FAFAFA] border-t border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <h2 class="text-2xl md:text-3xl font-black text-brand-dark leading-tight mb-4">Our Technology <span class="text-brand-base">Partners</span></h2>
                <p class="text-sm md:text-base text-[#4A4A4A] leading-relaxed">Collaborating with industry leaders to deliver robust and scalable solutions.</p>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 md:gap-12 items-center justify-items-center opacity-70">
                <!-- Placeholder for partner logos (to be provided) -->
                <div class="h-16 flex items-center justify-center font-bold text-[#1F3D5A]/50 bg-white/50 w-full rounded-xl border border-[#EDEDED] border-dashed">Partner Logo</div>
                <div class="h-16 flex items-center justify-center font-bold text-[#1F3D5A]/50 bg-white/50 w-full rounded-xl border border-[#EDEDED] border-dashed">Partner Logo</div>
                <div class="h-16 flex items-center justify-center font-bold text-[#1F3D5A]/50 bg-white/50 w-full rounded-xl border border-[#EDEDED] border-dashed">Partner Logo</div>
                <div class="h-16 flex items-center justify-center font-bold text-[#1F3D5A]/50 bg-white/50 w-full rounded-xl border border-[#EDEDED] border-dashed">Partner Logo</div>
            </div>
        </div>
    </section>
"""
# Insert Partner Section after Client Logos Section
client_logos_end = r'</section>\s+<!-- Digital Solutions Section -->'
content = re.sub(r'(</section>\s+<!-- Digital Solutions Section -->)', r'</section>\n' + partner_section + r'\n    <!-- Digital Solutions Section -->', content)

# 5. Testimonials (Leverage Edu style - clean, quote focused, no stars)
testimonial_section = """<!-- Testimonials -->
    <section class="py-24 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-4xl md:text-5xl font-extrabold mb-6 text-[#1F3D5A]">Client Success <span class="text-brand-base">Stories</span></h2>
                <p class="text-lg text-[#4A4A4A]">Hear from the leaders who trusted us to build their digital future.</p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8">
                <!-- Testimonial 1 -->
                <div class="bg-white p-8 rounded-3xl border border-[#EDEDED] shadow-sm hover:shadow-lg transition-all flex flex-col h-full relative overflow-hidden group">
                    <div class="absolute top-0 right-0 p-6 opacity-5 group-hover:opacity-10 transition-opacity">
                        <i data-lucide="quote" class="w-24 h-24 text-brand-dark"></i>
                    </div>
                    <div class="flex items-center gap-4 mb-6 z-10">
                        <div class="w-16 h-16 rounded-full bg-slate-200 shrink-0 overflow-hidden">
                            <img src="https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg?auto=compress&cs=tinysrgb&w=150" alt="Alex" class="w-full h-full object-cover">
                        </div>
                        <div>
                            <h4 class="font-bold text-lg text-[#1F3D5A]">Alex Rivera</h4>
                            <p class="text-sm text-[#4A4A4A]">CTO, FinLaunch</p>
                        </div>
                    </div>
                    <p class="text-[15px] text-[#4A4A4A] leading-relaxed italic mb-6 flex-grow z-10">
                        "The level of detail in their UX audit was astounding. They found bottlenecks in our funnel that we'd missed for years. A truly transformative partnership."
                    </p>
                    <div class="pt-6 border-t border-[#EDEDED] mt-auto z-10">
                        <p class="text-xs font-bold uppercase tracking-widest text-brand-base">Enterprise Web Platform</p>
                    </div>
                </div>

                <!-- Testimonial 2 -->
                <div class="bg-white p-8 rounded-3xl border border-[#EDEDED] shadow-sm hover:shadow-lg transition-all flex flex-col h-full relative overflow-hidden group">
                    <div class="absolute top-0 right-0 p-6 opacity-5 group-hover:opacity-10 transition-opacity">
                        <i data-lucide="quote" class="w-24 h-24 text-brand-dark"></i>
                    </div>
                    <div class="flex items-center gap-4 mb-6 z-10">
                        <div class="w-16 h-16 rounded-full bg-slate-200 shrink-0 overflow-hidden">
                            <img src="https://images.pexels.com/photos/1181686/pexels-photo-1181686.jpeg?auto=compress&cs=tinysrgb&w=150" alt="Sarah" class="w-full h-full object-cover">
                        </div>
                        <div>
                            <h4 class="font-bold text-lg text-[#1F3D5A]">Sarah Chen</h4>
                            <p class="text-sm text-[#4A4A4A]">Founder, Lume Labs</p>
                        </div>
                    </div>
                    <p class="text-[15px] text-[#4A4A4A] leading-relaxed italic mb-6 flex-grow z-10">
                        "Kritox didn't just build a site; they built a brand identity that doubled our conversion rate in the first three months. Absolutely outstanding execution."
                    </p>
                    <div class="pt-6 border-t border-[#EDEDED] mt-auto z-10">
                        <p class="text-xs font-bold uppercase tracking-widest text-brand-base">Native Mobile Apps</p>
                    </div>
                </div>

                <!-- Testimonial 3 -->
                <div class="bg-white p-8 rounded-3xl border border-[#EDEDED] shadow-sm hover:shadow-lg transition-all flex flex-col h-full relative overflow-hidden group">
                    <div class="absolute top-0 right-0 p-6 opacity-5 group-hover:opacity-10 transition-opacity">
                        <i data-lucide="quote" class="w-24 h-24 text-brand-dark"></i>
                    </div>
                    <div class="flex items-center gap-4 mb-6 z-10">
                        <div class="w-16 h-16 rounded-full bg-slate-200 shrink-0 overflow-hidden">
                            <img src="https://images.pexels.com/photos/1222271/pexels-photo-1222271.jpeg?auto=compress&cs=tinysrgb&w=150" alt="David" class="w-full h-full object-cover">
                        </div>
                        <div>
                            <h4 class="font-bold text-lg text-[#1F3D5A]">David Miller</h4>
                            <p class="text-sm text-[#4A4A4A]">VP, RealEdge</p>
                        </div>
                    </div>
                    <p class="text-[15px] text-[#4A4A4A] leading-relaxed italic mb-6 flex-grow z-10">
                        "Reliable, communicative, and exceptionally skilled. It's rare to find an agency that actually cares about your ROI as much as their own bottom line."
                    </p>
                    <div class="pt-6 border-t border-[#EDEDED] mt-auto z-10">
                        <p class="text-xs font-bold uppercase tracking-widest text-brand-base">B2B SaaS Portal</p>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
content = re.sub(r'<!-- Testimonials -->\s*<section class="py-24 bg-\[#FAFAFA\]">.*?(?=<!-- Portfolio Section -->)', testimonial_section + '\n\n    ', content, flags=re.DOTALL)

# 6. Case Studies (Leverage Edu style)
case_studies_section = """<!-- Case Studies Section -->
    <section id="portfolio" class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <!-- Header -->
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
                <div class="max-w-2xl">
                    <p class="text-[13px] font-black text-brand-base uppercase tracking-[0.2em] mb-4">CASE STUDIES</p>
                    <h2 class="text-3xl md:text-5xl font-black text-brand-dark tracking-tight">Our Proven Impact</h2>
                </div>
                <a href="#" class="inline-flex items-center gap-2 font-bold text-brand-base hover:text-brand-dark transition-colors">
                    Explore All Case Studies <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </a>
            </div>

            <!-- Case Studies Grid (Leverage Edu Style: Clean, Image-heavy, Metrics) -->
            <div class="grid lg:grid-cols-2 gap-10">
                <!-- Case Study 1 -->
                <div class="group cursor-pointer rounded-[2rem] bg-[#F8FAFC] border border-[#EDEDED] overflow-hidden hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                    <div class="relative h-64 md:h-80 overflow-hidden bg-slate-200">
                        <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fintech App" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <div class="absolute top-6 left-6 bg-white px-4 py-1.5 rounded-full text-xs font-bold text-brand-dark shadow-sm">Fintech</div>
                    </div>
                    <div class="p-8 md:p-10">
                        <h3 class="text-2xl md:text-3xl font-extrabold text-brand-dark mb-4">PayFlow Mobile App</h3>
                        <p class="text-[#4A4A4A] mb-8 leading-relaxed">Redesigned the entire user experience for a leading fintech platform, resulting in seamless transactions and a highly intuitive analytics dashboard.</p>
                        
                        <div class="grid grid-cols-2 gap-6 border-t border-[#EDEDED] pt-6">
                            <div>
                                <p class="text-3xl font-black text-brand-base mb-1">+140%</p>
                                <p class="text-xs font-bold text-[#4A4A4A] uppercase tracking-wider">User Retention</p>
                            </div>
                            <div>
                                <p class="text-3xl font-black text-brand-base mb-1">2.5M</p>
                                <p class="text-xs font-bold text-[#4A4A4A] uppercase tracking-wider">Active Users</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Case Study 2 -->
                <div class="group cursor-pointer rounded-[2rem] bg-[#F8FAFC] border border-[#EDEDED] overflow-hidden hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                    <div class="relative h-64 md:h-80 overflow-hidden bg-slate-200">
                        <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800" alt="E-Commerce" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <div class="absolute top-6 left-6 bg-white px-4 py-1.5 rounded-full text-xs font-bold text-brand-dark shadow-sm">E-Commerce</div>
                    </div>
                    <div class="p-8 md:p-10">
                        <h3 class="text-2xl md:text-3xl font-extrabold text-brand-dark mb-4">Lumina Storefront</h3>
                        <p class="text-[#4A4A4A] mb-8 leading-relaxed">Built an elegant and high-performance e-commerce platform for a luxury brand, featuring scalable backend architecture and AR product viewing.</p>
                        
                        <div class="grid grid-cols-2 gap-6 border-t border-[#EDEDED] pt-6">
                            <div>
                                <p class="text-3xl font-black text-brand-base mb-1">3x</p>
                                <p class="text-xs font-bold text-[#4A4A4A] uppercase tracking-wider">Sales Conversion</p>
                            </div>
                            <div>
                                <p class="text-3xl font-black text-brand-base mb-1">-40%</p>
                                <p class="text-xs font-bold text-[#4A4A4A] uppercase tracking-wider">Cart Abandonment</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
content = re.sub(r'<!-- Portfolio Section -->\s*<section id="portfolio" class="py-24 bg-white">.*?(?=<!-- Blog Section -->)', case_studies_section + '\n\n    ', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

