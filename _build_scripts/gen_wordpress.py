import re

with open("tech/wordpress.html", "r") as f:
    content = f.read()

wordpress_html = """
    <!-- WordPress Hero Section -->
    <section class="relative bg-[#FFFBF0] text-[#1F3D5A] pt-20 pb-10 md:pt-24 md:pb-12 border-b border-[#EDEDED] overflow-hidden">
        <div class="absolute inset-0 pointer-events-none">
            <div class="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-[#2F6F73] rounded-full blur-[150px] opacity-[0.07]"></div>
            <div class="absolute bottom-[-10%] left-[-5%] w-[30%] h-[30%] bg-[#E5B93C] rounded-full blur-[120px] opacity-[0.05]"></div>
        </div>
        <div class="max-w-7xl mx-auto px-6 md:px-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
                <p class="text-xs font-black uppercase tracking-[0.2em] text-[#E5B93C] mb-4">Custom WordPress Solutions</p>
                <h1 class="font-black inner-hero-title tracking-tight leading-[1.05] mb-6">
                    WordPress <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#2F6F73] to-[#E5B93C]">Development.</span>
                </h1>
                <p class="text-lg text-[#4A4A4A] leading-relaxed mb-8">
                    Want to launch a 100% responsive WordPress website? We're a bespoke and trusted WordPress development agency helping clients to launch a website with ease. Our custom solutions perform and grow with your business.
                </p>
                <div class="flex flex-wrap gap-4">
                    <a href="../../contact.html" class="inline-flex items-center gap-2 font-bold text-white bg-[#1F3D5A] px-8 py-4 rounded-xl hover:bg-[#2F6F73] transition-colors">
                        Get Free Quote <i data-lucide="arrow-right" class="w-5 h-5"></i>
                    </a>
                </div>
            </div>
            <div class="relative">
                <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&q=80" alt="WordPress Development" class="rounded-[2rem] shadow-2xl w-full h-[500px] object-cover">
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border border-[#EDEDED] flex items-center gap-4">
                    <div class="w-12 h-12 bg-[#2F6F73]/10 text-[#2F6F73] rounded-xl flex items-center justify-center shrink-0">
                        <i data-lucide="layout-template" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <p class="text-[#1F3D5A] font-black text-xl">Trusted</p>
                        <p class="text-[#4A4A4A] text-sm font-medium">Bespoke Agency</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose WordPress -->
    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-[#1F3D5A] mb-6">Why Choose <span class="text-[#2F6F73]">WordPress?</span></h2>
                <p class="text-lg text-[#4A4A4A]">WordPress is trusted by millions of brand owners worldwide. Whatever you're looking for, WordPress provides you with complete flexibility.</p>
            </div>
            
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="credit-card" class="w-8 h-8 text-[#E5B93C] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">No Licensing Fees</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">When you choose white label WordPress development, you don't need to pay licensing fees. Just pay for premium themes or custom development.</p>
                </div>
                <div class="bg-white border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="pen-tool" class="w-8 h-8 text-[#2F6F73] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Extreme Customization</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">With millions of themes, WordPress offers full customization flexibility. Add any functionalities to reflect your business's unique style.</p>
                </div>
                <div class="bg-white border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="search" class="w-8 h-8 text-[#1F3D5A] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">SEO & Lead Friendly</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">WordPress adheres to SEO practices and comes with plugins. This helps you to drive traffic. More visibility equals more leads.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="smartphone" class="w-8 h-8 text-[#E5B93C] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Responsive Themes</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">More than 64% of all site traffic comes from smart devices. WordPress offers responsive themes that look great anywhere.</p>
                </div>
                <div class="bg-white border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="layout-dashboard" class="w-8 h-8 text-[#2F6F73] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Easy To Manage</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">A user-friendly dashboard enables you to manage things from one place. From page edit to image update, handle it with ease.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="users" class="w-8 h-8 text-[#1F3D5A] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Big Community Support</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Passionate community support means you can find your answer with just a message or search away.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="blocks" class="w-8 h-8 text-[#E5B93C] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Third-Party Integrations</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Boost your email campaigns or add in-depth analytics easily. Integrations are straightforward with WordPress.</p>
                </div>
                <div class="bg-white border border-[#EDEDED] rounded-[2rem] py-8 px-6 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <i data-lucide="trending-down" class="w-8 h-8 text-[#2F6F73] mb-4"></i>
                    <h3 class="text-lg font-black text-[#1F3D5A] mb-3">Lower Setup Cost</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Choose when & how much to invest. Start with shared hosting and then scale your investment as your business grows.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- WordPress Services Section -->
    <section class="py-24 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="flex flex-col md:flex-row md:items-end gap-6 md:gap-10 mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark leading-tight shrink-0">
                    <span class="text-brand-base">Bespoke</span> WordPress<br>Development Services.
                </h2>
                <div class="hidden md:block h-[1.5px] bg-[#1F3D5A] flex-grow mb-4"></div>
                <p class="text-base md:text-lg font-medium text-neutral-dark md:max-w-[440px] leading-relaxed shrink-0 md:mb-1">
                    Whether you are creating a new website or looking to improve an existing one, check our white-label services to find exactly what you need.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Service 1 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">Multisite Development</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We help you set up a secure multisite network. Our developers handle the heavy tech lifting, helping you to focus on your business.</p>
                </div>
                <!-- Service 2 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">Theme Design & Dev</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We build a unique identity for you. Our experts create a purposeful WordPress theme keeping user experience at the forefront.</p>
                </div>
                <!-- Service 3 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">E-commerce Solutions</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We help you launch a professional online store with WooCommerce that makes shopping effortless for your customers.</p>
                </div>
                <!-- Service 4 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">Plugin Customization</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We build secure custom plugins to add exactly the functionalities you need to run your business successfully.</p>
                </div>
                <!-- Service 5 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">Responsive Web Design</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We design sites that work everywhere. A good-looking website isn't enough; it must be fast and responsive across all screens.</p>
                </div>
                <!-- Service 6 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">Migration Services</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">Move your existing business website securely. Our team ensures a stress-free transition with no broken links or downtime.</p>
                </div>
                <!-- Service 7 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">PSD To WordPress</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">Turn your Photoshop design into a dynamic site. Every element is brought to life using highly SEO-friendly code.</p>
                </div>
                <!-- Service 8 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">Support & Maintenance</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We help manage the overall health of your site, ensuring operational performance and stability all the time.</p>
                </div>
                <!-- Service 9 -->
                <div class="bg-white border border-[#EDEDED] p-8 rounded-2xl hover:border-[#2F6F73] transition-colors">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-4">Site Optimization</h3>
                    <p class="text-[#4A4A4A] text-sm leading-relaxed">We fine-tune all aspects of your site to make sure it loads blazingly fast and ranks higher on search engines.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6 tracking-tight">Our WordPress <span class="text-brand-base">Process</span></h2>
                <p class="text-lg text-[#4A4A4A] max-w-2xl mx-auto">We understand your custom needs and deliver a tool that works smoothly.</p>
            </div>
            
            <div class="grid md:grid-cols-5 gap-5">
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] p-7 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <span class="flex-shrink-0 w-10 h-10 rounded-full bg-[#1F3D5A] border-2 border-white/20 flex items-center justify-center font-bold text-white shadow-[0_0_0_4px_rgba(31,61,90,1)]">1</span>
                    <h3 class="text-xl font-black text-[#1F3D5A] mt-7 mb-3">Discovery</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">We discuss and define a website that truly reflects your vision and business goals.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] p-7 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <span class="flex-shrink-0 w-10 h-10 rounded-full bg-[#1F3D5A] border-2 border-white/20 flex items-center justify-center font-bold text-white shadow-[0_0_0_4px_rgba(31,61,90,1)]">2</span>
                    <h3 class="text-xl font-black text-[#1F3D5A] mt-7 mb-3">Design</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">We translate ideas into a design you can review, ensuring every element supports your goals.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] p-7 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <span class="flex-shrink-0 w-10 h-10 rounded-full bg-[#1F3D5A] border-2 border-white/20 flex items-center justify-center font-bold text-white shadow-[0_0_0_4px_rgba(31,61,90,1)]">3</span>
                    <h3 class="text-xl font-black text-[#1F3D5A] mt-7 mb-3">Development</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Once approved, we build from the ground up using scalable, secure code focused on functionality.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] p-7 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <span class="flex-shrink-0 w-10 h-10 rounded-full bg-[#1F3D5A] border-2 border-white/20 flex items-center justify-center font-bold text-white shadow-[0_0_0_4px_rgba(31,61,90,1)]">4</span>
                    <h3 class="text-xl font-black text-[#1F3D5A] mt-7 mb-3">Optimization</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">Our bespoke approach ensures the final site is optimized for top search performance.</p>
                </div>
                <div class="bg-[#FAFAFA] border border-[#EDEDED] rounded-[2rem] p-7 hover:shadow-xl hover:shadow-[#1F3D5A]/5 hover:-translate-y-1 transition-all duration-300">
                    <span class="flex-shrink-0 w-10 h-10 rounded-full bg-[#1F3D5A] border-2 border-white/20 flex items-center justify-center font-bold text-white shadow-[0_0_0_4px_rgba(31,61,90,1)]">5</span>
                    <h3 class="text-xl font-black text-[#1F3D5A] mt-7 mb-3">Launch</h3>
                    <p class="text-sm text-[#4A4A4A] leading-relaxed">We thoroughly test your site for issues and broken links before launching it to the world.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-24 bg-[#FAFAFA] border-t border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="bg-brand-dark rounded-[2.5rem] p-8 md:p-12 lg:p-16 text-center relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-br from-[#1F3D5A] via-[#2F6F73]/20 to-[#1F3D5A] pointer-events-none"></div>
                <div class="absolute bottom-0 right-0 w-[360px] h-[360px] bg-[#E5B93C]/10 rounded-full blur-[90px] pointer-events-none"></div>
                <div class="relative z-10 max-w-4xl mx-auto">
                    <p class="text-xs font-black uppercase tracking-[0.25em] text-[#E5B93C] mb-5">Ongoing Maintenance</p>
                    <h2 class="text-3xl md:text-5xl font-black text-white mb-6 tracking-tight">Let's discuss your project.</h2>
                    <p class="text-lg text-white/75 mb-10 max-w-2xl mx-auto">First impressions turn traffic into revenue. Our designers and developers will help you impress visitors and turn them into loyal customers.</p>
                    <a href="../contact.html" class="inline-flex items-center justify-center gap-2 px-12 py-4 bg-white text-[#2F6F73] font-bold rounded-2xl hover:bg-[#F0F4F8] transition-colors">
                        Contact Us Today
                        <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

# Replace the content
start_marker = r'<!-- React Hero Section -->'
end_marker = r'<!-- Footer -->'

pattern = re.compile(f"{start_marker}.*?{end_marker}", re.DOTALL)
new_content = pattern.sub(wordpress_html + "\n<!-- Footer -->", content)

with open("tech/wordpress.html", "w") as f:
    f.write(new_content)

print("WordPress page updated successfully.")
