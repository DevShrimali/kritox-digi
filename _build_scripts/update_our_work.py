import os
import glob
import re

mega_menu_content = """<div class="mega-menu-panel mega-menu-full bg-[#FAFAFA] border-b border-neutral-light py-8">
                        <div class="max-w-7xl mx-auto px-10 grid grid-cols-4 gap-0">
                            <div class="bg-brand-dark rounded-2xl p-7 mr-6 flex flex-col justify-between min-h-[200px]">
                                <div>
                                    <p class="text-white font-black text-2xl leading-snug mb-3">See Our Work</p>
                                    <p class="text-teal-50 text-[14px] leading-relaxed">Real projects, real results —
                                        worldwide.</p>
                                </div>
                                <a href="PREFIXportfolio/index.html"
                                    class="mt-6 inline-block bg-white text-[#2F6F73] font-bold text-[14px] px-6 py-3 rounded-xl hover:bg-[#2F6F73]/10 transition-colors text-center">View
                                    Portfolio</a>
                            </div>
                            <div class="flex flex-col gap-5 pr-8 border-r border-[#EDEDED]">
                                <a href="PREFIXportfolio/index.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="layout-grid" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            Portfolio</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">Deep-dive project reviews</p>
                                    </div>
                                </a>
                                <a href="PREFIXcase-studies/index.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="folder-open" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            Case Studies</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">In-depth success stories</p>
                                    </div>
                                </a>
                            </div>
                            <div class="flex flex-col gap-5 px-8 border-r border-[#EDEDED]">
                                <a href="PREFIXtestimonials.html" class="group flex gap-3 items-start">
                                    <div
                                        class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">
                                        <i data-lucide="star" class="w-4 h-4"></i>
                                    </div>
                                    <div>
                                        <p
                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">
                                            Testimonials</p>
                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">What clients say</p>
                                    </div>
                                </a>
                            </div>
                            <div class="flex flex-col gap-4 pl-8">
                                <p class="text-[11px] font-black uppercase tracking-widest text-[#4A4A4A]/60">Industries
                                    Served</p>
                                <div class="flex flex-wrap gap-2">
                                    <span
                                        class="px-3 py-1 bg-white border border-[#EDEDED] text-slate-700 text-[12px] font-semibold rounded-full">Fintech</span>
                                    <span
                                        class="px-3 py-1 bg-white border border-[#EDEDED] text-slate-700 text-[12px] font-semibold rounded-full">Healthcare</span>
                                    <span
                                        class="px-3 py-1 bg-white border border-[#EDEDED] text-slate-700 text-[12px] font-semibold rounded-full">E-commerce</span>
                                    <span
                                        class="px-3 py-1 bg-white border border-[#EDEDED] text-slate-700 text-[12px] font-semibold rounded-full">SaaS</span>
                                    <span
                                        class="px-3 py-1 bg-white border border-[#EDEDED] text-slate-700 text-[12px] font-semibold rounded-full">EdTech</span>
                                </div>
                            </div>
                        </div>
                    </div>"""

mobile_menu_content = """<div class="mt-3 space-y-2 pl-1">
                    <a href="PREFIXportfolio/index.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Portfolio</a>
                    <a href="PREFIXcase-studies/index.html"
                        class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Case
                        Studies</a>
                    <a href="PREFIXtestimonials.html"
                        class="block text-[13px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">Testimonials</a>
                </div>"""

html_files = glob.glob('**/*.html', recursive=True)

for file_path in html_files:
    if "template_content.html" in file_path or "_build_scripts" in file_path or "w3nuts" in file_path:
        continue
        
    with open(file_path, 'r') as f:
        content = f.read()
        
    original_content = content
    depth = file_path.count('/')
    if file_path.startswith('./'):
        depth -= 1
    prefix = '../' * depth if depth > 0 else ''
    
    # Desktop Menu Match
    mega_target = re.compile(
        r'(Our Work\s*<i data-lucide="chevron-down" class="w-3 h-3"></i>\s*</button>\s*)<div class="mega-menu-panel mega-menu-full bg-\[#FAFAFA\] border-b border-neutral-light py-8">.*?</div>\s*</div>\s*<!-- Career \(no mega menu\) -->',
        re.DOTALL
    )
    
    formatted_mega_menu = mega_menu_content.replace('PREFIX', prefix)
    
    if mega_target.search(content):
        content = mega_target.sub(r'\1' + formatted_mega_menu + '\n                </div>\n\n                <!-- Career (no mega menu) -->', content)

    # Mobile Menu Match
    mobile_target = re.compile(
        r'(Our Work\s*<i data-lucide="chevron-down"\s*class="w-5 h-5 text-\[#4A4A4A\] transition-transform group-open:rotate-180"></i>\s*</summary>\s*)<div class="mt-3 space-y-2 pl-1">.*?</div>\s*</details>\s*<a href="[^"]*career\.html" class="block text-xl font-bold text-\[#1F3D5A\] py-2">Career</a>',
        re.DOTALL
    )
    
    formatted_mobile_menu = mobile_menu_content.replace('PREFIX', prefix)
    career_href = f"{prefix}career.html"
    
    if mobile_target.search(content):
        content = mobile_target.sub(r'\1' + formatted_mobile_menu + f'\n            </details>\n            <a href="{career_href}" class="block text-xl font-bold text-[#1F3D5A] py-2">Career</a>', content)
        
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated Our Work menu in {file_path}")

