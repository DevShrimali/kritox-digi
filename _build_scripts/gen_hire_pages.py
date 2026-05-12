import os
import re

stacks = [
    {"file": "hire-mean-stack.html", "name": "MEAN Stack", "icon": "server", "img": "https://images.unsplash.com/photo-1555099962-4199c345e5dd"},
    {"file": "hire-mern-stack.html", "name": "MERN Stack", "icon": "code", "img": "https://images.unsplash.com/photo-1633356122544-f134324a6cee"},
    {"file": "hire-full-stack.html", "name": "Full Stack", "icon": "layers", "img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97"},
    {"file": "hire-python.html", "name": "Python", "icon": "terminal", "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5"},
    {"file": "hire-web-developers.html", "name": "Web Developers", "icon": "monitor", "img": "https://images.unsplash.com/photo-1547658719-da2b51169166"},
    {"file": "hire-mobile-developers.html", "name": "Mobile Developers", "icon": "smartphone", "img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c"}
]

with open('tech/node.html', 'r') as f:
    template = f.read()

top_part = template.split('<!-- Node.js Hero Section -->')[0]

# Add Footer AND the CTA section from node.html back in.
footer_part = '<!-- Footer -->' + template.split('<!-- Footer -->')[1]

cta_section = """
    <!-- Have a Great Idea CTA -->
    <section class="bg-[#1F3D5A] py-24 relative overflow-hidden">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-0 right-[-10%] w-[40%] h-[100%] bg-[#2F6F73] blur-[150px] opacity-40"></div>
            <div class="absolute bottom-[-20%] left-[-10%] w-[30%] h-[50%] bg-[#E5B93C] blur-[150px] opacity-20"></div>
        </div>
        <div class="max-w-5xl mx-auto px-6 md:px-10 text-center relative z-10">
            <h2 class="text-4xl md:text-6xl font-black text-white mb-6">Have a Great Idea? <br/><span class="text-[#E5B93C]">Tell us about it.</span></h2>
            <p class="text-white/80 text-lg md:text-xl mb-12 max-w-2xl mx-auto">
                Ready to start your project? Or perhaps you have more questions about our services? We're here to help you every step of the way.
            </p>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
                <a href="../contact.html" class="w-full sm:w-auto px-8 py-4 bg-[#E5B93C] text-[#1F3D5A] font-bold text-lg rounded-xl hover:bg-white transition-colors text-center">
                    Schedule a Free Consultation
                </a>
                <a href="../contact.html" class="w-full sm:w-auto px-8 py-4 bg-transparent border-2 border-white text-white font-bold text-lg rounded-xl hover:bg-white/10 transition-colors text-center">
                    Request a Project Quote
                </a>
            </div>
        </div>
    </section>
"""

bottom_part = cta_section + footer_part

def get_sections(name, img):
    return f"""
    <!-- Hero Section (CMARIX Pattern) -->
    <section class="inner-hero border-b border-[#EDEDED] relative py-12 md:py-20 bg-[#FAFAFA]">
        <div class="absolute inset-0 pointer-events-none overflow-hidden">
            <div class="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-[#2F6F73] rounded-full blur-[150px] opacity-[0.05]"></div>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center relative z-10">
            <div>
                <nav class="inner-breadcrumb !mt-0 mb-6" aria-label="Breadcrumb">
                    <a href="../index.html">Home</a>
                    <i data-lucide="chevron-right"></i>
                    <a href="../career.html">Hire Developers</a>
                    <i data-lucide="chevron-right"></i>
                    <span class="text-[#2F6F73]">{name}</span>
                </nav>
                <p class="text-xs font-black uppercase tracking-[0.2em] text-[#E5B93C] mb-4">Elite Talent, Fast</p>
                <h1 class="font-black tracking-tight leading-[1.05] mb-6 text-[2.5rem] md:text-[3.5rem] text-[#1F3D5A]">
                    Hire {name} Developers <span class="block text-[1.8rem] md:text-[2.2rem] mt-2 text-[#2F6F73] font-extrabold">with Full Stack Integration Capabilities</span>
                </h1>
                <p class="text-lg text-[#4A4A4A] leading-relaxed mb-8">
                    Hire {name} developers to build scalable, service-oriented architecture (SOA) applications. Our dedicated development team specializes in providing end-to-end software solutions customized to your business needs.
                </p>
                
                <div class="flex flex-wrap items-center gap-6">
                    <a href="../contact.html" class="inline-flex items-center gap-2 font-bold text-white bg-[#1F3D5A] px-8 py-4 rounded-xl hover:bg-[#2F6F73] transition-colors">
                        Hire {name} Experts <i data-lucide="arrow-right" class="w-5 h-5"></i>
                    </a>
                </div>
            </div>
            <div class="relative">
                <img src="{img}?auto=format&fit=crop&q=80&w=1000" alt="Hire {name} Developers" class="rounded-[2rem] shadow-2xl w-full h-[500px] object-cover">
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border border-[#EDEDED] flex flex-col gap-2">
                    <div class="flex items-center gap-2">
                        <i data-lucide="star" class="w-5 h-5 text-[#E5B93C] fill-current"></i>
                        <span class="font-bold text-[#1F3D5A] text-lg">Top Rated</span>
                    </div>
                    <p class="text-[#4A4A4A] text-sm font-medium">95% Client Retention</p>
                </div>
                <div class="absolute -top-6 -right-6 bg-[#1F3D5A] p-6 rounded-2xl shadow-xl text-white flex flex-col items-center">
                    <span class="font-black text-3xl text-[#E5B93C]">5+</span>
                    <span class="text-sm font-semibold text-white/80 uppercase tracking-widest mt-1">Years Avg Exp</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Custom Services -->
    <section class="bg-white py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">OUR EXPERTISE</p>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6">Custom Services Our {name} Developers Provide</h2>
                <p class="text-[#4A4A4A] text-lg">From ideation to deployment, our {name} developers offer a comprehensive suite of services tailored to your unique requirements.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-[#FAFAFA] p-8 rounded-[2rem] border border-[#EDEDED] hover:shadow-lg transition-all duration-300">
                    <div class="w-14 h-14 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6">
                        <i data-lucide="layout" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Custom App Development</h3>
                    <p class="text-[#4A4A4A] leading-relaxed">End-to-end custom application development matching your business goals and user expectations.</p>
                </div>
                <div class="bg-[#FAFAFA] p-8 rounded-[2rem] border border-[#EDEDED] hover:shadow-lg transition-all duration-300">
                    <div class="w-14 h-14 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6">
                        <i data-lucide="server" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">API Integration</h3>
                    <p class="text-[#4A4A4A] leading-relaxed">Seamless integration of third-party APIs and custom backend endpoints to extend functionality.</p>
                </div>
                <div class="bg-[#FAFAFA] p-8 rounded-[2rem] border border-[#EDEDED] hover:shadow-lg transition-all duration-300">
                    <div class="w-14 h-14 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6">
                        <i data-lucide="refresh-cw" class="w-7 h-7"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Migration & Upgrades</h3>
                    <p class="text-[#4A4A4A] leading-relaxed">Secure and efficient migration of legacy systems to modern {name} architectures.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Dedicated Hiring Models -->
    <section class="bg-[#111111] py-24 border-b border-white/10 text-white selection-style relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                <defs><pattern id="grid-dark" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="white" stroke-width="1"/></pattern></defs>
                <rect width="100%" height="100%" fill="url(#grid-dark)" />
            </svg>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <p class="text-[12px] font-black text-[#E5B93C] uppercase tracking-[0.2em] mb-4">FLEXIBLE ENGAGEMENT</p>
                <h2 class="text-3xl md:text-5xl font-black mb-6 tracking-tight text-white">Dedicated Hiring Models</h2>
                <p class="text-lg text-white/60 leading-relaxed max-w-3xl mx-auto">
                    Choose an engagement model that fits your budget, timeline, and project requirements. We offer flexible options to scale your team efficiently.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-black/40 border border-white/20 rounded-3xl p-8 hover:bg-white/5 transition-all">
                    <h3 class="text-2xl font-bold text-white mb-2">Dedicated Team</h3>
                    <p class="text-[#E5B93C] font-semibold mb-6">Full-time engagement</p>
                    <p class="text-white/60 text-sm mb-8 leading-relaxed">Hire an entire team of {name} experts who work exclusively on your project as an extension of your in-house team.</p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> 160 Hours/Month</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> Direct Control</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> No Hidden Costs</li>
                    </ul>
                    <a href="../contact.html" class="block text-center bg-white text-black font-bold py-3 rounded-xl hover:bg-[#E5B93C] transition-colors">Choose Model</a>
                </div>
                <div class="bg-black/40 border border-white/20 rounded-3xl p-8 hover:bg-white/5 transition-all relative transform md:-translate-y-4 shadow-2xl border-[#E5B93C]/50">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#E5B93C] text-black text-xs font-black px-4 py-1 rounded-full uppercase tracking-widest">Most Popular</div>
                    <h3 class="text-2xl font-bold text-white mb-2">Time & Material</h3>
                    <p class="text-[#E5B93C] font-semibold mb-6">Hourly engagement</p>
                    <p class="text-white/60 text-sm mb-8 leading-relaxed">Ideal for ongoing projects with evolving requirements. Pay only for the actual hours worked by our {name} developers.</p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> Pay As You Go</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> High Flexibility</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> Agile Approach</li>
                    </ul>
                    <a href="../contact.html" class="block text-center bg-[#E5B93C] text-black font-bold py-3 rounded-xl hover:bg-white transition-colors">Choose Model</a>
                </div>
                <div class="bg-black/40 border border-white/20 rounded-3xl p-8 hover:bg-white/5 transition-all">
                    <h3 class="text-2xl font-bold text-white mb-2">Fixed Cost</h3>
                    <p class="text-[#E5B93C] font-semibold mb-6">Project-based engagement</p>
                    <p class="text-white/60 text-sm mb-8 leading-relaxed">Best for projects with clearly defined scopes, deliverables, and timelines. Complete your {name} project within a fixed budget.</p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> Defined Milestones</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> Fixed Budget</li>
                        <li class="flex items-center gap-2 text-white/80 text-sm"><i data-lucide="check" class="w-4 h-4 text-[#E5B93C]"></i> Minimal Risk</li>
                    </ul>
                    <a href="../contact.html" class="block text-center bg-white text-black font-bold py-3 rounded-xl hover:bg-[#E5B93C] transition-colors">Choose Model</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="bg-[#FAFAFA] py-24 border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="order-2 lg:order-1 relative">
                <div class="absolute inset-0 bg-[#2F6F73] rounded-[2rem] transform -translate-x-4 translate-y-4"></div>
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80" alt="Why Choose Us" class="relative rounded-[2rem] shadow-xl w-full h-[500px] object-cover">
            </div>
            <div class="order-1 lg:order-2">
                <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">THE KRITOX ADVANTAGE</p>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6">Why Choose Us for {name} Development?</h2>
                <p class="text-[#4A4A4A] text-lg leading-relaxed mb-8">
                    Partnering with Kritox Digital means choosing a team of seasoned professionals dedicated to delivering excellence. Our {name} developers bring a wealth of experience and a track record of successful project completions.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="check-circle" class="w-6 h-6 text-[#2F6F73]"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] mb-1">Pre-vetted Talent</h4>
                            <p class="text-sm text-[#4A4A4A]">Top 1% of {name} experts meticulously screened.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="clock" class="w-6 h-6 text-[#2F6F73]"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] mb-1">Fast Onboarding</h4>
                            <p class="text-sm text-[#4A4A4A]">Start your project within 48 hours of engagement.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="shield" class="w-6 h-6 text-[#2F6F73]"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] mb-1">Strict NDA</h4>
                            <p class="text-sm text-[#4A4A4A]">Your intellectual property is completely protected.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-[#EDEDED] flex items-center justify-center shrink-0">
                            <i data-lucide="headphones" class="w-6 h-6 text-[#2F6F73]"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] mb-1">24/7 Support</h4>
                            <p class="text-sm text-[#4A4A4A]">Continuous communication across all time zones.</p>
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
                    <div class="flex text-[#E5B93C] mb-4">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-[#4A4A4A] italic flex-1 mb-6">"The {name} developers from Kritox Digital were exceptional. They integrated perfectly with our internal team and delivered the features ahead of schedule."</p>
                    <div class="flex items-center gap-4 mt-auto border-t border-[#EDEDED] pt-6">
                        <div class="w-12 h-12 rounded-full bg-brand-base/10 text-brand-base font-bold flex items-center justify-center text-lg">JD</div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A]">John Doe</h4>
                            <p class="text-xs text-[#4A4A4A] uppercase tracking-wider font-semibold">CTO, TechCorp</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-3xl shadow-xl flex flex-col h-full">
                    <div class="flex text-[#E5B93C] mb-4">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-[#4A4A4A] italic flex-1 mb-6">"Hiring a dedicated team was the best decision. Their expertise in {name} is unmatched and the communication was transparent throughout."</p>
                    <div class="flex items-center gap-4 mt-auto border-t border-[#EDEDED] pt-6">
                        <div class="w-12 h-12 rounded-full bg-brand-base/10 text-brand-base font-bold flex items-center justify-center text-lg">SS</div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A]">Sarah Smith</h4>
                            <p class="text-xs text-[#4A4A4A] uppercase tracking-wider font-semibold">Product Manager, Innovate Inc.</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-3xl shadow-xl flex flex-col h-full hidden lg:flex">
                    <div class="flex text-[#E5B93C] mb-4">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-[#4A4A4A] italic flex-1 mb-6">"Kritox delivered an outstanding {name} application that transformed our digital presence. Highly recommend their dedicated developers."</p>
                    <div class="flex items-center gap-4 mt-auto border-t border-[#EDEDED] pt-6">
                        <div class="w-12 h-12 rounded-full bg-brand-base/10 text-brand-base font-bold flex items-center justify-center text-lg">MJ</div>
                        <div>
                            <h4 class="font-bold text-[#1F3D5A]">Michael Johnson</h4>
                            <p class="text-xs text-[#4A4A4A] uppercase tracking-wider font-semibold">CEO, StartUp Solutions</p>
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
                <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">OUR WORK</p>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Recent {name} Projects</h2>
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
                        <p class="text-white/80 mb-6">Built with {name}</p>
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
                        <p class="text-white/80 mb-6">Built with {name}</p>
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
                        <p class="text-white/80 mb-6">Built with {name}</p>
                        <div class="flex items-center uppercase tracking-widest text-[12px] font-bold">
                            EXPLORE NOW <i data-lucide="arrow-right" class="w-4 h-4 ml-2 group-hover:translate-x-2 transition-transform"></i>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="max-w-7xl mx-auto px-6 md:px-10 mt-6 relative z-20 pointer-events-auto flex items-center justify-between">
                <div class="flex gap-3">
                    <button id="portfolio-carousel-prev" class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-[#1F3D5A] hover:bg-[#2F6F73] hover:text-white transition-all"><i data-lucide="chevron-left"></i></button>
                    <button id="portfolio-carousel-next" class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-[#1F3D5A] hover:bg-[#2F6F73] hover:text-white transition-all"><i data-lucide="chevron-right"></i></button>
                </div>
                <a href="../case-studies/index.html" class="inline-flex items-center justify-center gap-2 px-8 py-3 bg-[#1F3D5A] text-white font-bold rounded-2xl hover:bg-[#2F6F73] transition-colors">View All Case Studies</a>
            </div>
        </div>
    </section>

    <!-- Hire Stack Developers with Integration Capabilities -->
    <section class="bg-[#FAFAFA] py-24 border-t border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10 text-center">
            <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6">Hire {name} Developers with Full Stack Capabilities</h2>
            <p class="text-lg text-[#4A4A4A] max-w-3xl mx-auto mb-10">Ready to transform your vision into a robust digital product? Our pre-vetted {name} developers seamlessly integrate into your workflow to deliver excellence.</p>
            <a href="../contact.html" class="inline-flex items-center gap-2 bg-[#2F6F73] text-white px-10 py-5 rounded-2xl font-black text-lg hover:bg-[#1F3D5A] transition-colors shadow-xl">
                Let's Discuss Your Project <i data-lucide="arrow-right"></i>
            </a>
        </div>
    </section>

    <!-- FAQs Section -->
    <section class="bg-white py-24 border-t border-[#EDEDED]">
        <div class="max-w-4xl mx-auto px-6 md:px-10">
            <div class="text-center mb-16">
                <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-4">FAQ</p>
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6 tracking-tight">Frequently Asked Questions</h2>
            </div>
            
            <div class="space-y-4">
                <details class="group bg-[#FAFAFA] rounded-2xl border border-[#EDEDED] open:bg-white open:border-[#2F6F73] transition-colors" open>
                    <summary class="flex justify-between items-center font-bold text-lg cursor-pointer list-none p-6 text-[#1F3D5A]">
                        How quickly can I hire a {name} developer?
                        <span class="transition group-open:rotate-180">
                            <i data-lucide="chevron-down" class="w-5 h-5"></i>
                        </span>
                    </summary>
                    <div class="text-[#4A4A4A] text-sm px-6 pb-6 leading-relaxed">
                        We can typically onboard a {name} developer to your project within 48 to 72 hours of signing the agreement.
                    </div>
                </details>
                <details class="group bg-[#FAFAFA] rounded-2xl border border-[#EDEDED] open:bg-white open:border-[#2F6F73] transition-colors">
                    <summary class="flex justify-between items-center font-bold text-lg cursor-pointer list-none p-6 text-[#1F3D5A]">
                        Do you sign NDAs?
                        <span class="transition group-open:rotate-180">
                            <i data-lucide="chevron-down" class="w-5 h-5"></i>
                        </span>
                    </summary>
                    <div class="text-[#4A4A4A] text-sm px-6 pb-6 leading-relaxed">
                        Yes, we ensure full confidentiality and intellectual property protection by signing an NDA before we start discussing your project details.
                    </div>
                </details>
                <details class="group bg-[#FAFAFA] rounded-2xl border border-[#EDEDED] open:bg-white open:border-[#2F6F73] transition-colors">
                    <summary class="flex justify-between items-center font-bold text-lg cursor-pointer list-none p-6 text-[#1F3D5A]">
                        Can I scale the team up or down?
                        <span class="transition group-open:rotate-180">
                            <i data-lucide="chevron-down" class="w-5 h-5"></i>
                        </span>
                    </summary>
                    <div class="text-[#4A4A4A] text-sm px-6 pb-6 leading-relaxed">
                        Absolutely. Our engagement models are highly flexible, allowing you to easily scale your dedicated {name} development team based on changing project requirements.
                    </div>
                </details>
            </div>
        </div>
    </section>
    """

for stack in stacks:
    new_content = top_part + get_sections(stack["name"], stack["img"]) + '\n' + bottom_part
    with open(f"tech/{stack['file']}", 'w') as f:
        f.write(new_content)

print("Hire pages generated successfully with FAQs!")
