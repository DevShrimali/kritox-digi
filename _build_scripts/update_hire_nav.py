import os
import glob
import re

mega_menu_content = """<div class="mega-menu-panel mega-menu-full bg-[#FAFAFA] border-b border-neutral-light py-8">
                        <div class="max-w-7xl mx-auto px-10 grid grid-cols-4 gap-0">
                            <div class="bg-brand-dark rounded-2xl p-7 mr-6 flex flex-col justify-between min-h-[200px]">
                                <div>
                                    <p class="text-white font-black text-2xl leading-snug mb-3">Elite Talent, Fast</p>
                                    <p class="text-teal-50 text-[14px] leading-relaxed">Hire pre-vetted developers in days,
                                        not months.</p>
                                </div>
                                <a href="PREFIXcontact.html"
                                    class="mt-6 inline-block bg-white text-[#2F6F73] font-bold text-[14px] px-6 py-3 rounded-xl hover:bg-[#2F6F73]/10 transition-colors text-center">Book
                                    a Call</a>
                            </div>
                            <div class="flex flex-col gap-5 pr-8 border-r border-[#EDEDED]">
                                <a href="PREFIXhire/mean-stack.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="server" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            MEAN Stack</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">MongoDB, Express, Angular, Node</p>
                                    </div>
                                </a>
                                <a href="PREFIXhire/mern-stack.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="code" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            MERN Stack</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">MongoDB, Express, React, Node</p>
                                    </div>
                                </a>
                            </div>
                            <div class="flex flex-col gap-5 px-8 border-r border-[#EDEDED]">
                                <a href="PREFIXhire/full-stack.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="layers" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            Full Stack</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">End-to-end development</p>
                                    </div>
                                </a>
                                <a href="PREFIXhire/python.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="terminal" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            Python</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">Data, AI & Backend</p>
                                    </div>
                                </a>
                            </div>
                            <div class="flex flex-col gap-5 pl-8">
                                <a href="PREFIXhire/web-developers.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="monitor" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            Web Developers</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">Frontend & Backend</p>
                                    </div>
                                </a>
                                <a href="PREFIXhire/mobile-developers.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="smartphone" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            Mobile Developers</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">iOS & Android native apps</p>
                                    </div>
                                </a>
                            </div>
                        </div>
                    </div>"""

mobile_menu_content = """<div class="mt-3 space-y-2 pl-1">
                    <a href="PREFIXhire/mean-stack.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Hire MEAN Stack</a>
                    <a href="PREFIXhire/mern-stack.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Hire MERN Stack</a>
                    <a href="PREFIXhire/full-stack.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Hire Full Stack</a>
                    <a href="PREFIXhire/python.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Hire Python Developers</a>
                    <a href="PREFIXhire/web-developers.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Hire Web Developers</a>
                    <a href="PREFIXhire/mobile-developers.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Hire Mobile Developers</a>
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
    
    # 1. Mega Menu replacement for Hire Developer
    mega_target = re.compile(
        r'(Hire Developer\s*<i data-lucide="chevron-down" class="w-3 h-3"></i>\s*</button>\s*)<div class="mega-menu-panel mega-menu-full bg-\[#FAFAFA\] border-b border-neutral-light py-8">.*?</div>\s*</div>\s*<!-- Our Work -->',
        re.DOTALL
    )
    
    formatted_mega_menu = mega_menu_content.replace('PREFIX', prefix)
    
    if mega_target.search(content):
        content = mega_target.sub(r'\1' + formatted_mega_menu + '\n                </div>\n\n                <!-- Our Work -->', content)
    
    # 2. Mobile Menu Replacement for Hire Developer
    mobile_target = re.compile(
        r'(Hire Developer\s*<i data-lucide="chevron-down"\s*class="w-5 h-5 text-\[#4A4A4A\] transition-transform group-open:rotate-180"></i>\s*</summary>\s*)<div class="mt-3 space-y-2 pl-1">.*?</div>\s*</details>\s*<details class="group border-b border-\[#EDEDED\] pb-4">\s*<summary\s*class="flex items-center justify-between text-xl font-bold text-\[#1F3D5A\] cursor-pointer list-none">\s*Our Work',
        re.DOTALL
    )
    
    formatted_mobile_menu = mobile_menu_content.replace('PREFIX', prefix)
    
    if mobile_target.search(content):
        content = mobile_target.sub(r'\1' + formatted_mobile_menu + '\n            </details>\n            <details class="group border-b border-[#EDEDED] pb-4">\n                <summary\n                    class="flex items-center justify-between text-xl font-bold text-[#1F3D5A] cursor-pointer list-none">\n                    Our Work', content)
        
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated menus in {file_path}")

print("Done updating navigation!")
