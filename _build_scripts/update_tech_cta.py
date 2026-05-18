import os
import glob
import re

tech_mapping = {
    'ai.html': 'AI/ML',
    'android.html': 'Android',
    'angular.html': 'Angular',
    'aws.html': 'AWS & Cloud',
    'brand-design.html': 'Brand Design',
    'cicd.html': 'CI/CD & DevOps',
    'databases.html': 'Database',
    'docker.html': 'Docker & Kubernetes',
    'ios.html': 'iOS',
    'laravel.html': 'Laravel',
    'mobile.html': 'React Native & Flutter',
    'node.html': 'Node.js',
    'php.html': 'PHP',
    'python.html': 'Python',
    'react.html': 'React',
    'uiux.html': 'UI/UX Design',
    'vue.html': 'Vue.js',
    'web-design.html': 'Web Design',
    'wordpress.html': 'WordPress'
}

html_files = glob.glob('tech/*.html')

for file in html_files:
    filename = os.path.basename(file)
    tech_name = tech_mapping.get(filename, filename.replace('.html', '').capitalize())
    
    with open(file, 'r') as f:
        content = f.read()

    # Check if CTA already exists
    if 'Ready to build with' in content or 'CTA Section' in content and 'Projects</p>' in content:
        print(f"Skipping {file} - CTA already exists")
        continue
        
    cta_template = f"""
    <!-- CTA Section -->
    <section class="py-24 bg-[#FAFAFA] border-t border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="bg-brand-dark rounded-[2.5rem] p-8 md:p-12 lg:p-16 text-center relative overflow-hidden">
                <div
                    class="absolute inset-0 bg-gradient-to-br from-[#1F3D5A] via-[#2F6F73]/20 to-[#1F3D5A] pointer-events-none">
                </div>
                <div
                    class="absolute bottom-0 right-0 w-[360px] h-[360px] bg-[#E5B93C]/10 rounded-full blur-[90px] pointer-events-none">
                </div>
                <div class="relative z-10 max-w-4xl mx-auto">
                    <p class="text-xs font-black uppercase tracking-[0.25em] text-[#E5B93C] mb-5">{tech_name} Projects</p>
                    <h2 class="text-3xl md:text-5xl font-black text-white mb-6 tracking-tight">Ready to build with
                        {tech_name}?</h2>
                    <p class="text-lg text-white/75 mb-10 max-w-2xl mx-auto">Our {tech_name} experts are ready to scope,
                        build and ship your project. Get a free consultation today.</p>
                    <a href="../contact.html"
                        class="inline-flex items-center justify-center gap-2 px-12 py-4 bg-white text-[#2F6F73] font-bold rounded-2xl hover:bg-[#F0F4F8] transition-colors">
                        Contact Us Today
                        <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

    if '<!-- Footer -->' in content:
        content = content.replace('<!-- Footer -->', cta_template + '    <!-- Footer -->')
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Warning: Footer not found in {file}")

