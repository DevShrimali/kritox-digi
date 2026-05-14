import re
import glob

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the 5 cards with 6 cards
cards_html = """
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Card 1 -->
                <div class="group bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="monitor" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Web Development</h3>
                    <p class="text-[#4A4A4A] text-sm mb-8 flex-1 leading-relaxed">
                        Scalable, high-performance web applications built with modern frameworks to drive your business forward.
                    </p>
                    <a href="services/web-development.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Card 2 -->
                <div class="group bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="layout" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">UI/UX Design</h3>
                    <p class="text-[#4A4A4A] text-sm mb-8 flex-1 leading-relaxed">
                        User-centered, conversion-focused design systems that provide intuitive and engaging experiences.
                    </p>
                    <a href="services/ui-ux-design.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Card 3 -->
                <div class="group bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="smartphone" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Mobile Apps</h3>
                    <p class="text-[#4A4A4A] text-sm mb-8 flex-1 leading-relaxed">
                        High-quality iOS & Android native experiences designed for performance and seamless interactions.
                    </p>
                    <a href="services/mobile-apps.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Card 4 -->
                <div class="group bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="bar-chart-3" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Digital Marketing</h3>
                    <p class="text-[#4A4A4A] text-sm mb-8 flex-1 leading-relaxed">
                        Data-driven growth strategies, SEO, and brand positioning to maximize your online visibility.
                    </p>
                    <a href="services/digital-marketing.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>

                <!-- Card 5 -->
                <div class="group bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="zap" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Brand Strategy</h3>
                    <p class="text-[#4A4A4A] text-sm mb-8 flex-1 leading-relaxed">
                        Comprehensive brand identity, positioning, and messaging to help you stand out in the market.
                    </p>
                    <a href="services/brand-strategy.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
                
                <!-- Card 6 -->
                <div class="group bg-[#FAFAFA] border border-[#EDEDED] rounded-3xl p-8 hover:bg-white hover:border-[#2F6F73] hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center">
                    <div class="w-16 h-16 bg-[#2F6F73]/10 text-[#2F6F73] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i data-lucide="cloud" class="w-8 h-8"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-[#1F3D5A] mb-4">Cloud Solutions</h3>
                    <p class="text-[#4A4A4A] text-sm mb-8 flex-1 leading-relaxed">
                        Secure infrastructure and DevOps optimization for scalable, high-availability deployments.
                    </p>
                    <a href="services/cloud-solutions.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#1F3D5A] text-white hover:bg-[#2F6F73] transition-colors font-bold text-sm">
                        Explore More <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>"""

new_content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6">.*?</div>\s*</div>\s*</section>', cards_html + '\n        </div>\n    </section>', content, flags=re.DOTALL)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated services.html cards")
