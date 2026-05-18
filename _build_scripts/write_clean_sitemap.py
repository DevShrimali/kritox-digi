import re

def create_clean_sitemap():
    # Read about.html to get navbar and footer
    with open('/Users/devshrimali/Documents/Work/AEC/kritox-digi/about.html', 'r') as f:
        about_html = f.read()

    # Extract Navbar
    navbar_match = re.search(r'(<!-- Navbar -->.*?)</nav>\s*<!-- Mobile Menu Overlay -->.*?</div>\s*</div>\s*(?=<!-- About Hero Section)', about_html, re.DOTALL)
    navbar_code = navbar_match.group(0)

    # Extract Footer
    footer_match = re.search(r'(<!-- Footer -->.*?)</body>', about_html, re.DOTALL)
    footer_code = footer_match.group(1)

    # Clean Sitemap Content
    sitemap_content = """
    <!-- Sitemap Content -->
    <section class="bg-[#FAFAFA] py-24 mt-20 min-h-screen">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <h1 class="text-4xl md:text-5xl font-black text-[#1F3D5A] mb-6">Sitemap</h1>
                <p class="text-lg text-[#4A4A4A]">Navigate through Kritox Digital.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Company -->
                <div class="bg-white border border-[#EDEDED] rounded-[1.5rem] p-8 hover:shadow-lg transition-shadow">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-10 h-10 rounded-xl bg-[#1F3D5A] flex items-center justify-center">
                            <i data-lucide="building" class="w-5 h-5 text-white"></i>
                        </div>
                        <h2 class="text-xl font-black text-[#1F3D5A]">Company</h2>
                    </div>
                    <ul class="space-y-3">
                        <li><a href="about.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>About Us</a></li>
                        <li><a href="contact.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Contact Us</a></li>
                        <li><a href="blog/index.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Blog</a></li>
                        <li><a href="engagement-models.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Engagement Models</a></li>
                        <li><a href="life-at-kritox.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Life at Kritox</a></li>
                        <li><a href="industries.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Industries</a></li>
                        <li><a href="career.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Career</a></li>
                    </ul>
                </div>

                <!-- Services -->
                <div class="bg-white border border-[#EDEDED] rounded-[1.5rem] p-8 hover:shadow-lg transition-shadow">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-10 h-10 rounded-xl bg-[#2F6F73] flex items-center justify-center">
                            <i data-lucide="layers" class="w-5 h-5 text-white"></i>
                        </div>
                        <h2 class="text-xl font-black text-[#1F3D5A]">Services</h2>
                    </div>
                    <ul class="space-y-3">
                        <li><a href="services.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>All Services</a></li>
                        <li><a href="services/web-development.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Web Development</a></li>
                        <li><a href="services/mobile-apps.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Mobile App Development</a></li>
                        <li><a href="services/ui-ux-design.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>UI/UX Design</a></li>
                        <li><a href="services/digital-marketing.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Digital Marketing</a></li>
                        <li><a href="services/cloud-solutions.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Cloud Solutions</a></li>
                        <li><a href="services/brand-strategy.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Brand Strategy</a></li>
                    </ul>
                </div>

                <!-- Our Work -->
                <div class="bg-white border border-[#EDEDED] rounded-[1.5rem] p-8 hover:shadow-lg transition-shadow">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-10 h-10 rounded-xl bg-[#E5B93C] flex items-center justify-center">
                            <i data-lucide="briefcase" class="w-5 h-5 text-[#1F3D5A]"></i>
                        </div>
                        <h2 class="text-xl font-black text-[#1F3D5A]">Our Work</h2>
                    </div>
                    <ul class="space-y-3">
                        <li><a href="portfolio/index.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Portfolio Overview</a></li>
                        <li><a href="portfolio/fintech-app.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Fintech App</a></li>
                        <li><a href="portfolio/saas-platform.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>SaaS Platform</a></li>
                        <div class="my-2 border-t border-[#EDEDED] w-full"></div>
                        <li><a href="case-studies/index.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Case Studies Overview</a></li>
                        <li><a href="case-studies/fintech.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Fintech Case Study</a></li>
                        <li><a href="case-studies/saas.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>SaaS Case Study</a></li>
                        <li><a href="case-studies/ecommerce.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>E-Commerce Case Study</a></li>
                        <li><a href="case-studies/cloud.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Cloud Case Study</a></li>
                    </ul>
                </div>

                <!-- Technologies -->
                <div class="bg-white border border-[#EDEDED] rounded-[1.5rem] p-8 hover:shadow-lg transition-shadow">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-10 h-10 rounded-xl bg-[#1F3D5A] flex items-center justify-center">
                            <i data-lucide="cpu" class="w-5 h-5 text-white"></i>
                        </div>
                        <h2 class="text-xl font-black text-[#1F3D5A]">Technologies</h2>
                    </div>
                    <ul class="space-y-3">
                        <li><a href="tech/react.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>React & Next.js</a></li>
                        <li><a href="tech/node.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Node.js & Go</a></li>
                        <li><a href="tech/databases.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Databases</a></li>
                        <li><a href="tech/aws.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>AWS Cloud</a></li>
                        <li><a href="tech/mobile.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Mobile Apps</a></li>
                        <li><a href="tech/ai.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>AI & ML</a></li>
                        <li><a href="tech/docker.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Docker & Containers</a></li>
                        <li><a href="tech/cicd.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>CI/CD & Automation</a></li>
                    </ul>
                </div>

                <!-- Hire Developers -->
                <div class="bg-white border border-[#EDEDED] rounded-[1.5rem] p-8 hover:shadow-lg transition-shadow">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-10 h-10 rounded-xl bg-[#2F6F73] flex items-center justify-center">
                            <i data-lucide="users" class="w-5 h-5 text-white"></i>
                        </div>
                        <h2 class="text-xl font-black text-[#1F3D5A]">Hire Developers</h2>
                    </div>
                    <ul class="space-y-3">
                        <li><a href="hire/hire-mean-stack.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Hire MEAN Stack</a></li>
                        <li><a href="hire/hire-mern-stack.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Hire MERN Stack</a></li>
                        <li><a href="hire/hire-full-stack.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Hire Full Stack</a></li>
                        <li><a href="hire/hire-python.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Hire Python Developers</a></li>
                        <li><a href="hire/hire-web-developers.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Hire Web Developers</a></li>
                        <li><a href="hire/hire-mobile-developers.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Hire Mobile Developers</a></li>
                    </ul>
                </div>

                <!-- Legal & Utility -->
                <div class="bg-white border border-[#EDEDED] rounded-[1.5rem] p-8 hover:shadow-lg transition-shadow">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-10 h-10 rounded-xl bg-[#E5B93C] flex items-center justify-center">
                            <i data-lucide="shield" class="w-5 h-5 text-[#1F3D5A]"></i>
                        </div>
                        <h2 class="text-xl font-black text-[#1F3D5A]">Legal & Utility</h2>
                    </div>
                    <ul class="space-y-3">
                        <li><span class="text-[#4A4A4A] font-medium text-sm opacity-70">Privacy Policy (coming soon)</span></li>
                        <li><span class="text-[#4A4A4A] font-medium text-sm opacity-70">Terms of Service (coming soon)</span></li>
                        <li><a href="testimonials.html" class="flex items-center gap-2 text-[#4A4A4A] hover:text-[#2F6F73] font-medium transition-colors group"><i data-lucide="arrow-right" class="w-4 h-4 opacity-0 group-hover:opacity-100 -ml-6 group-hover:ml-0 transition-all"></i>Testimonials</a></li>
                    </ul>
                </div>

            </div>
        </div>
    </section>
    """

    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sitemap - Kritox Digital</title>
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script src="js/tailwind-config.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body class="bg-white text-brand-dark">
{navbar_code}
{sitemap_content}
{footer_code}
    <!-- Initialize Lucide Icons -->
    <script>
        lucide.createIcons();
    </script>
    <script src="js/main.js"></script>
</body>
</html>"""

    with open('/Users/devshrimali/Documents/Work/AEC/kritox-digi/sitemap.html', 'w') as f:
        f.write(new_html)

create_clean_sitemap()
print("Sitemap rebuilt beautifully!")
