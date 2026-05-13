import os
import glob

components_template = """
    <!-- Inner Industries Variant -->
    <section class="py-24 bg-[#FAFAFA] border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-4">Industries We Serve</h2>
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
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="graduation-cap" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">EdTech</h3>
                </div>
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="wallet" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">FinTech</h3>
                </div>
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="truck" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">Logistics</h3>
                </div>
                <div class="bg-white p-6 md:p-8 rounded-2xl border border-[#EDEDED] text-center hover:border-[#2F6F73] hover:shadow-lg transition-all group">
                    <i data-lucide="utensils" class="w-10 h-10 mx-auto text-[#2F6F73] mb-4 group-hover:scale-110 transition-transform"></i>
                    <h3 class="font-bold text-[#1F3D5A]">Food & Bev</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- Inner Portfolio Variant -->
    <section class="py-24 bg-white border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-4">Our Recent Work</h2>
                <p class="text-[#4A4A4A] text-lg">Real outcomes driven by our technical expertise.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="group cursor-pointer rounded-3xl overflow-hidden border border-[#EDEDED] bg-[#FAFAFA] hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                    <div class="h-64 overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Fintech Project" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="p-8">
                        <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-2">FINTECH</p>
                        <h3 class="text-2xl font-bold text-[#1F3D5A] mb-3">Enterprise Financial Platform</h3>
                        <p class="text-[#4A4A4A] mb-6">A secure, scalable banking solution processing $5B+ annually.</p>
                        <span class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] group-hover:text-[#2F6F73] transition-colors">
                            View Case Study <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </span>
                    </div>
                </div>
                <div class="group cursor-pointer rounded-3xl overflow-hidden border border-[#EDEDED] bg-[#FAFAFA] hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                    <div class="h-64 overflow-hidden relative">
                        <img src="https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=800" alt="SaaS Project" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="p-8">
                        <p class="text-[12px] font-black text-[#2F6F73] uppercase tracking-[0.2em] mb-2">SAAS PLATFORM</p>
                        <h3 class="text-2xl font-bold text-[#1F3D5A] mb-3">B2B Workflow Automation</h3>
                        <p class="text-[#4A4A4A] mb-6">Empowering teams with seamless integrations and robust analytics.</p>
                        <span class="inline-flex items-center gap-2 font-bold text-[#1F3D5A] group-hover:text-[#2F6F73] transition-colors">
                            View Case Study <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </span>
                    </div>
                </div>
            </div>
            <div class="text-center mt-12">
                <a href="{prefix}case-studies/index.html" class="inline-flex items-center gap-2 px-8 py-4 bg-[#1F3D5A] text-white rounded-xl font-bold hover:bg-[#2F6F73] transition-colors">
                    See All Projects <i data-lucide="layout-grid" class="w-5 h-5"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Inner Testimonials Variant -->
    <section class="py-24 bg-brand-dark relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-[#1F3D5A] via-[#2F6F73]/20 to-[#1F3D5A] z-0 pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 relative z-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-white mb-4">Client Feedback</h2>
                <p class="text-white/80 text-lg">What our partners say about working with us.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur-sm border border-white/10 p-8 rounded-3xl flex flex-col">
                    <div class="flex items-center gap-1 text-[#E5B93C] mb-6">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-white/90 text-lg mb-8 leading-relaxed italic flex-grow">"The technical expertise and dedication shown by the team was outstanding. They delivered a complex platform on time and beyond our expectations."</p>
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
                    <p class="text-white/90 text-lg mb-8 leading-relaxed italic flex-grow">"Kritox transformed our outdated legacy systems into a modern, scalable architecture. A truly professional partner."</p>
                    <div class="flex items-center gap-4 mt-auto">
                        <div class="w-12 h-12 bg-[#2F6F73] rounded-full flex items-center justify-center text-white font-bold text-lg shrink-0">M</div>
                        <div>
                            <p class="text-white font-bold">Michael Chen</p>
                            <p class="text-white/60 text-sm">Founder, InnovateRetail</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white/10 backdrop-blur-sm border border-white/10 p-8 rounded-3xl flex flex-col">
                    <div class="flex items-center gap-1 text-[#E5B93C] mb-6">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i><i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-white/90 text-lg mb-8 leading-relaxed italic flex-grow">"Exceptional communication and high-quality code. They don't just write code; they understand the business objectives behind it."</p>
                    <div class="flex items-center gap-4 mt-auto">
                        <div class="w-12 h-12 bg-[#2F6F73] rounded-full flex items-center justify-center text-white font-bold text-lg shrink-0">A</div>
                        <div>
                            <p class="text-white font-bold">Amanda Rossi</p>
                            <p class="text-white/60 text-sm">Product Manager</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Inner Client Logos Variant -->
    <section class="py-16 bg-[#FAFAFA] border-b border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <p class="text-center text-[12px] font-black text-[#4A4A4A] uppercase tracking-[0.2em] mb-8">TRUSTED BY INNOVATIVE TEAMS WORLDWIDE</p>
            <div class="flex flex-wrap justify-center items-center gap-10 md:gap-16 opacity-60 grayscale mix-blend-multiply">
                <img src="{prefix}assets/client logo/hello healthy.png" alt="Hello Healthy" class="h-10 object-contain">
                <img src="{prefix}assets/client logo/HP Logo(PantoneU) copy.png" alt="HP" class="h-10 object-contain">
                <img src="{prefix}assets/client logo/Stern-logo-blue.png" alt="Stern" class="h-10 object-contain">
                <img src="{prefix}assets/client logo/logo-skedulo-navy.svg" alt="Skedulo" class="h-10 object-contain">
                <img src="{prefix}assets/client logo/smarteinc.png" alt="Smarteinc" class="h-10 object-contain">
                <img src="{prefix}assets/client logo/KBOnline.png" alt="KBOnline" class="h-10 object-contain">
            </div>
        </div>
    </section>
"""

def inject_in_file(filepath, is_inner_dir=True):
    with open(filepath, "r") as f:
        content = f.read()

    if "<!-- Inner Industries Variant -->" in content:
        print(f"Skipping {filepath} - already injected")
        return

    prefix = "../" if is_inner_dir else ""
    components = components_template.format(prefix=prefix)

    # Where to inject?
    # Preferred: Before "<!-- CTA Section -->"
    # Fallback: Before "<!-- Footer -->"
    
    if "<!-- CTA Section -->" in content:
        parts = content.split("<!-- CTA Section -->")
        new_content = parts[0] + components + "\n    <!-- CTA Section -->" + parts[1]
    elif "<!-- Footer -->" in content:
        parts = content.split("<!-- Footer -->")
        new_content = parts[0] + components + "\n<!-- Footer -->" + parts[1]
    else:
        print(f"Could not find injection point in {filepath}")
        return

    with open(filepath, "w") as f:
        f.write(new_content)
    print(f"Injected into {filepath}")

# 1. Services Page
inject_in_file("/Users/devshrimali/Documents/Work/AEC/kritox-digi/services.html", is_inner_dir=False)

# 2. Tech Pages
tech_dir = "/Users/devshrimali/Documents/Work/AEC/kritox-digi/tech"
for filename in os.listdir(tech_dir):
    if filename.endswith(".html"):
        inject_in_file(os.path.join(tech_dir, filename), is_inner_dir=True)

print("Done")
