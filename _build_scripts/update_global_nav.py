import os
import glob
import re

# The new HTML for the Technologies Mega Menu (Desktop)
mega_menu_content = """<div class="mega-menu-panel mega-menu-full bg-[#FAFAFA] border-b border-neutral-light py-8">
                        <div class="max-w-7xl mx-auto px-10 grid grid-cols-4 gap-0">
                            <div class="bg-brand-dark rounded-2xl p-7 mr-6 flex flex-col justify-between min-h-[200px]">
                                <div>
                                    <p class="text-white font-black text-2xl leading-snug mb-3">Tech that Scales</p>
                                    <p class="text-teal-50 text-[14px] leading-relaxed">Modern stack for modern businesses.</p>
                                </div>
                                <a href="PREFIXcontact.html"
                                    class="mt-6 inline-block bg-white text-[#2F6F73] font-bold text-[14px] px-6 py-3 rounded-xl hover:bg-[#2F6F73]/10 transition-colors text-center">Consult
                                    Experts</a>
                            </div>
                            <div class="flex flex-col gap-4 pr-6 border-r border-[#EDEDED]">
                                <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Frontend & Design</p>
                                <a href="PREFIXtech/uiux.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="layout" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">UI/UX Design</p>
                                </a>
                                <a href="PREFIXtech/brand-design.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="pen-tool" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Brand Design</p>
                                </a>
                                <a href="PREFIXtech/web-design.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="monitor" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Web Design</p>
                                </a>
                                <a href="PREFIXtech/react.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="code" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">React.js</p>
                                </a>
                                <a href="PREFIXtech/vue.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="code" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Vue.js</p>
                                </a>
                                <a href="PREFIXtech/angular.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="code" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Angular.js</p>
                                </a>
                            </div>
                            <div class="flex flex-col gap-4 px-6 border-r border-[#EDEDED]">
                                <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Backend & Cloud</p>
                                <a href="PREFIXtech/node.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="server" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Node.js</p>
                                </a>
                                <a href="PREFIXtech/python.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="terminal" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Python</p>
                                </a>
                                <a href="PREFIXtech/php.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="server" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">PHP</p>
                                </a>
                                <a href="PREFIXtech/laravel.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="server" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Laravel</p>
                                </a>
                                <a href="PREFIXtech/databases.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="database" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Databases</p>
                                </a>
                                <a href="PREFIXtech/aws.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="cloud" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">AWS & GCP</p>
                                </a>
                                <a href="PREFIXtech/docker.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="box" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Docker & K8s</p>
                                </a>
                            </div>
                            <div class="flex flex-col gap-4 pl-6">
                                <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 ml-2 mb-1">Mobile & More</p>
                                <a href="PREFIXtech/mobile.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="smartphone" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">React Native & Flutter</p>
                                </a>
                                <a href="PREFIXtech/ios.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="smartphone" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">iOS</p>
                                </a>
                                <a href="PREFIXtech/android.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="smartphone" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">Android</p>
                                </a>
                                <a href="PREFIXtech/wordpress.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="layout-template" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">WordPress</p>
                                </a>
                                <a href="PREFIXtech/ai.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="cpu" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">AI & ML</p>
                                </a>
                                <a href="PREFIXtech/cicd.html" class="group flex gap-3 items-center">
                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 border border-[#EDEDED]"><i data-lucide="git-branch" class="w-3 h-3"></i></div>
                                    <p class="font-bold text-[#1F3D5A] text-[13px] group-hover:text-[#2F6F73] transition-colors">CI/CD & DevOps</p>
                                </a>
                            </div>
                        </div>
                    </div>"""

mobile_menu_content = """<div class="mt-3 space-y-2 pl-1">
                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Frontend & Design</p>
                    <a href="PREFIXtech/uiux.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">UI/UX Design</a>
                    <a href="PREFIXtech/brand-design.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Brand Design</a>
                    <a href="PREFIXtech/web-design.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Web Design</a>
                    <a href="PREFIXtech/react.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">React.js</a>
                    <a href="PREFIXtech/vue.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Vue.js</a>
                    <a href="PREFIXtech/angular.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Angular.js</a>
                    
                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Backend & Cloud</p>
                    <a href="PREFIXtech/node.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Node.js</a>
                    <a href="PREFIXtech/python.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Python</a>
                    <a href="PREFIXtech/php.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">PHP</a>
                    <a href="PREFIXtech/laravel.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Laravel</a>
                    <a href="PREFIXtech/databases.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Databases</a>
                    <a href="PREFIXtech/aws.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">AWS & GCP</a>
                    <a href="PREFIXtech/docker.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Docker & K8s</a>
                    
                    <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60 mb-2 mt-4">Mobile & More</p>
                    <a href="PREFIXtech/mobile.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">React Native & Flutter</a>
                    <a href="PREFIXtech/ios.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">iOS</a>
                    <a href="PREFIXtech/android.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Android</a>
                    <a href="PREFIXtech/wordpress.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">WordPress</a>
                    <a href="PREFIXtech/ai.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">AI & ML</a>
                    <a href="PREFIXtech/cicd.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">CI/CD & DevOps</a>
                </div>"""

html_files = glob.glob('**/*.html', recursive=True)

for file_path in html_files:
    if "template_content.html" in file_path or "_build_scripts" in file_path or "w3nuts" in file_path:
        continue
        
    with open(file_path, 'r') as f:
        content = f.read()
        
    original_content = content
    depth = file_path.count('/')
    prefix = '../' * depth if depth > 0 else ''
    
    # 1. Mega Menu replacement
    # Using regex to find the mega menu div for Technologies
    # We look for `<div class="mega-menu-panel mega-menu-full bg-[#FAFAFA] border-b border-neutral-light py-8">`
    # after `Technologies <i data-lucide="chevron-down" class="w-3 h-3"></i>`
    
    mega_target = re.compile(
        r'(Technologies\s*<i data-lucide="chevron-down" class="w-3 h-3"></i>\s*</button>\s*)<div class="mega-menu-panel mega-menu-full bg-\[#FAFAFA\] border-b border-neutral-light py-8">.*?</div>\s*</div>\s*<!-- Hire Developer -->',
        re.DOTALL
    )
    
    formatted_mega_menu = mega_menu_content.replace('PREFIX', prefix)
    
    # Try replacing
    if mega_target.search(content):
        content = mega_target.sub(r'\1' + formatted_mega_menu + '\n                </div>\n\n                <!-- Hire Developer -->', content)
    
    # 2. Mobile Menu Replacement
    mobile_target = re.compile(
        r'(Technologies\s*<i data-lucide="chevron-down"\s*class="w-5 h-5 text-\[#4A4A4A\] transition-transform group-open:rotate-180"></i>\s*</summary>\s*)<div class="mt-3 space-y-2 pl-1">.*?</div>\s*</details>\s*<details class="group border-b border-\[#EDEDED\] pb-4">\s*<summary[^>]*>\s*Hire Developer',
        re.DOTALL
    )
    
    formatted_mobile_menu = mobile_menu_content.replace('PREFIX', prefix)
    
    if mobile_target.search(content):
        content = mobile_target.sub(r'\1' + formatted_mobile_menu + '\n            </details>\n            <details class="group border-b border-[#EDEDED] pb-4">\n                <summary class="flex items-center justify-between text-xl font-bold text-[#1F3D5A] cursor-pointer list-none">\n                    Hire Developer', content)
        
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated menus in {file_path}")

print("Done updating navigation!")
