import os
import glob
import re

html_files = glob.glob('hire/*.html')

new_testimonials = """    <!-- Testimonials Section -->
    <section id="testimonials" class="py-24 bg-white overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 md:px-10 mb-16">
            <!-- Header -->
            <div class="text-center max-w-2xl mx-auto">
                <p class="text-[12px] font-black text-brand-dark uppercase tracking-[0.2em] mb-4">TESTIMONIALS</p>
                <h2 class="text-4xl md:text-5xl font-extrabold mb-6">Real stories from <br /><span
                        class="teal-primary">happy clients.</span></h2>
            </div>
        </div>

        <div class="relative">
            <div class="pointer-events-none absolute left-0 top-0 h-full w-24 md:w-40 z-10"
                style="background: linear-gradient(to right, #ffffff 0%, rgba(255,255,255,0) 100%);"></div>

            <div id="testimonial-carousel"
                class="bleed-carousel-container carousel-container carousel-seamless carousel-no-hover-pause flex gap-6 overflow-x-auto snap-x snap-mandatory no-scrollbar pb-10 cursor-grab active:cursor-grabbing">

                <!-- Item 1 -->
                <div class="testimonial-card snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[380px] bg-[#F4F4F4] p-8 md:p-10 flex flex-col rounded-[1rem] cursor-pointer border border-[#E5E5E5] hover:shadow-md transition-shadow"
                    data-tagline="Transformed our digital presence!"
                    data-image="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop"
                    data-name="Michael Reynolds" data-role="CTO, FinSecure" data-location="New York | USA"
                    data-full-review="They didn't just build a mobile app; they completely reimagined our digital banking experience. The development process was incredibly smooth and transparent. Their team consistently delivered high-quality code and proactively solved complex architecture issues.">
                    <p class="text-[#4CAF50] italic font-semibold text-[15px] mb-6">Transformed our digital presence!
                    </p>
                    <div class="flex items-center gap-4 mb-6">
                        <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop"
                            alt="Michael Reynolds" draggable="false"
                            class="w-14 h-14 rounded-full object-cover select-none">
                        <div class="flex text-[#F5B015]">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                        </div>
                    </div>
                    <h4 class="text-2xl font-bold text-[#1F3D5A] mb-2">Michael Reynolds</h4>
                    <p class="text-[15px] font-bold text-[#1F3D5A]">CTO, FinSecure</p>
                    <p class="text-[14px] text-[#4A4A4A] mb-6">New York | USA</p>
                    <p class="italic text-[15px] text-[#4A4A4A] leading-relaxed mb-8">
                        They didn't just build a mobile app; they completely reimagined our digital banking experience.
                        The development process was incredibly smooth and transparent.
                    </p>
                    <div
                        class="mt-auto pt-4 flex items-center gap-2 text-[15px] font-bold text-[#1F3D5A] hover:text-[#2F6F73] transition-colors group w-fit">
                        Read full story
                        <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                    </div>
                </div>

                <!-- Item 2 -->
                <div class="testimonial-card snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[380px] bg-[#F4F4F4] p-8 md:p-10 flex flex-col rounded-[1rem] cursor-pointer border border-[#E5E5E5] hover:shadow-md transition-shadow"
                    data-tagline="Scaled our platform flawlessly!"
                    data-image="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop"
                    data-name="Sarah Jenkins" data-role="VP of Engineering, CloudScale" data-location="London | UK"
                    data-full-review="When we hit our scale limits, their team stepped in and migrated our entire monolithic architecture to microservices without a single minute of downtime. We can now deploy 10x faster, and our infrastructure costs have dropped by 30%. A truly spectacular engineering partner.">
                    <p class="text-[#4CAF50] italic font-semibold text-[15px] mb-6">Scaled our platform flawlessly!</p>
                    <div class="flex items-center gap-4 mb-6">
                        <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop"
                            alt="Sarah Jenkins" draggable="false"
                            class="w-14 h-14 rounded-full object-cover select-none">
                        <div class="flex text-[#F5B015]">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                        </div>
                    </div>
                    <h4 class="text-2xl font-bold text-[#1F3D5A] mb-2">Sarah Jenkins</h4>
                    <p class="text-[15px] font-bold text-[#1F3D5A]">VP of Engineering, CloudScale</p>
                    <p class="text-[14px] text-[#4A4A4A] mb-6">London | UK</p>
                    <p class="italic text-[15px] text-[#4A4A4A] leading-relaxed mb-8">
                        When we hit our scale limits, their team stepped in and migrated our entire monolithic
                        architecture to microservices without a single minute of downtime.
                    </p>
                    <div
                        class="mt-auto pt-4 flex items-center gap-2 text-[15px] font-bold text-[#1F3D5A] hover:text-[#2F6F73] transition-colors group w-fit">
                        Read full story
                        <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="testimonial-card snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[380px] bg-[#F4F4F4] p-8 md:p-10 flex flex-col rounded-[1rem] cursor-pointer border border-[#E5E5E5] hover:shadow-md transition-shadow"
                    data-tagline="Doubled our e-commerce sales!"
                    data-image="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop"
                    data-name="David Chen" data-role="Director of Tech, LuxRetail" data-location="Toronto | Canada"
                    data-full-review="Choosing my MBA through Leverage Online and enrolling at Toronto | Canada was an easy decision to make because of the excellent support and guidance provided by Kritox Digital. The digital platform they built handled everything seamlessly, and our enrollment numbers doubled in the first quarter! The UX is top-notch and highly converting.">
                    <p class="text-[#4CAF50] italic font-semibold text-[15px] mb-6">Doubled our e-commerce sales!</p>
                    <div class="flex items-center gap-4 mb-6">
                        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop"
                            alt="David Chen" draggable="false" class="w-14 h-14 rounded-full object-cover select-none">
                        <div class="flex text-[#F5B015]">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                        </div>
                    </div>
                    <h4 class="text-2xl font-bold text-[#1F3D5A] mb-2">David Chen</h4>
                    <p class="text-[15px] font-bold text-[#1F3D5A]">Director of Tech, LuxRetail</p>
                    <p class="text-[14px] text-[#4A4A4A] mb-6">Toronto | Canada</p>
                    <p class="italic text-[15px] text-[#4A4A4A] leading-relaxed mb-8">
                        Choosing my MBA through Leverage Online and enrolling at Toronto | Canada was an ea...
                    </p>
                    <div
                        class="mt-auto pt-4 flex items-center gap-2 text-[15px] font-bold text-[#1F3D5A] hover:text-[#2F6F73] transition-colors group w-fit">
                        Read full story
                        <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                    </div>
                </div>

                <!-- Item 4 -->
                <div class="testimonial-card snap-start shrink-0 w-[85%] sm:w-[50%] md:w-[42%] lg:w-[32%] xl:w-[28%] min-h-[380px] bg-[#F4F4F4] p-8 md:p-10 flex flex-col rounded-[1rem] cursor-pointer border border-[#E5E5E5] hover:shadow-md transition-shadow"
                    data-tagline="A true technology partner."
                    data-image="https://images.unsplash.com/photo-1531123897727-8f129e1bf98c?w=100&h=100&fit=crop"
                    data-name="Elena Rodriguez" data-role="Founder, HealthTech Innovators"
                    data-location="Berlin | Germany"
                    data-full-review="Finding an agency that truly understands HIPAA compliance and modern cloud infrastructure was tough until we met them. Their engineering quality is world-class, and they took our data security requirements as seriously as we do. Highly recommended for any healthcare SaaS company.">
                    <p class="text-[#4CAF50] italic font-semibold text-[15px] mb-6">A true technology partner.</p>
                    <div class="flex items-center gap-4 mb-6">
                        <img src="https://images.unsplash.com/photo-1531123897727-8f129e1bf98c?w=100&h=100&fit=crop"
                            alt="Elena Rodriguez" draggable="false"
                            class="w-14 h-14 rounded-full object-cover select-none">
                        <div class="flex text-[#F5B015]">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                <path
                                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                            </svg>
                        </div>
                    </div>
                    <h4 class="text-2xl font-bold text-[#1F3D5A] mb-2">Elena Rodriguez</h4>
                    <p class="text-[15px] font-bold text-[#1F3D5A]">Founder, HealthTech Innovators</p>
                    <p class="text-[14px] text-[#4A4A4A] mb-6">Berlin | Germany</p>
                    <p class="italic text-[15px] text-[#4A4A4A] leading-relaxed mb-8">
                        Finding an agency that truly understands HIPAA compliance and modern cloud infrastructure was
                        tough until we met them. Their engineering quality is world-class.
                    </p>
                    <div
                        class="mt-auto pt-4 flex items-center gap-2 text-[15px] font-bold text-[#1F3D5A] hover:text-[#2F6F73] transition-colors group w-fit">
                        Read full story
                        <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                    </div>
                </div>

            </div>

            <!-- Custom scrollbar container -->
            <div
                class="max-w-7xl mx-auto px-6 md:px-10 mt-6 relative z-20 pointer-events-auto flex items-center justify-between">
                <div class="flex gap-3">
                    <button id="testimonial-carousel-prev"
                        class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-[#1F3D5A] hover:bg-brand-base hover:text-white hover:border-brand-base transition-all group">
                        <svg class="w-5 h-5 transition-transform group-hover:-translate-x-1" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7">
                            </path>
                        </svg>
                    </button>
                    <button id="testimonial-carousel-next"
                        class="w-12 h-12 rounded-full border border-[#D5E0E2] flex items-center justify-center text-[#1F3D5A] hover:bg-brand-base hover:text-white hover:border-brand-base transition-all group">
                        <svg class="w-5 h-5 transition-transform group-hover:translate-x-1" fill="none"
                            stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7">
                            </path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </section>
"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We want to replace the old Testimonials section with the new Testimonials section.
    # We can use regex to find the section between "<!-- Testimonials -->" and the next "<!-- Portfolio Section -->"
    
    # Check if the file has the old pattern
    pattern = re.compile(r'<!-- Testimonials -->\s*<section class="bg-brand-base.*?CLIENT REVIEWS.*?</section>', re.DOTALL)
    
    if pattern.search(content):
        # We also need to be careful if there's any other </section> we might match early. 
        # But this regex .*? will stop at the first </section>, which is wrong if there are inner elements.
        pass
    
    # Actually, a better way is to find the exact block bounds based on comments or fixed string matching.
    
    start_str = '    <!-- Testimonials -->\n    <section class="bg-brand-base py-24 relative overflow-hidden">'
    end_str = '    <!-- Portfolio Section -->'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + new_testimonials + "\n\n" + content[end_idx:]
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file} - Pattern not found")

