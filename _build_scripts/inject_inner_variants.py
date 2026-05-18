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

    <!-- Testimonials Section -->
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

    <!-- Client Logos Section -->
    <section class="pt-20 pb-10 bg-white">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-5xl font-black text-brand-dark leading-tight mb-6">Empowering <span
                        class="text-brand-base">Industry Leaders</span><br>Worldwide</h2>
                <p class="text-sm md:text-base text-[#4A4A4A] leading-relaxed">Join hundreds of global enterprises and
                    rapid-growth startups leveraging our cutting-edge technology solutions.</p>
            </div>

            <div
                class="grid grid-cols-2 lg:grid-cols-5 gap-x-10 gap-y-14 md:gap-x-14 md:gap-y-16 items-center justify-items-center">
                <img src="{prefix}assets/client%20logo/hello%20healthy.png" alt="Hello Healthy"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/HP%20Logo(PantoneU)%20copy.png" alt="HP"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/Stern-logo-blue.png" alt="Stern"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/logo-skedulo-navy.svg" alt="Skedulo"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/smarteinc.png" alt="Smarteinc"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/KBOnline.png" alt="KBOnline"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/Quietlight.webp" alt="Quietlight"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/vitaskan.png" alt="Vitaskan"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/myally.webp" alt="MyAlly"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
                <img src="{prefix}assets/client%20logo/paris%20creative.png" alt="Paris Creative"
                    class="h-12 md:h-14 w-auto grayscale opacity-60 mix-blend-multiply object-contain">
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
