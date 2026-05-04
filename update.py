import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Header & Footer font size
content = content.replace('text-[13px]', 'text-[14px]')

# 3. Explore Our Services - Remove border
content = content.replace('border-2 border-dashed border-white/10 hover:border-brand-base', '')

# 4. Remove Kritox Digital text from all boxes
content = re.sub(r'\s*<h4 class="text-sm font-bold text-\[#1F3D5A\] mb-3">Kritox Digital</h4>', '', content)

# 5. Testimonials - Remove ratings
# Remove the star ratings from the stats overlay
content = re.sub(r'<div class="flex items-center gap-0\.5 text-\[#E5B93C\] mb-1">.*?</div>', '', content, flags=re.DOTALL)
# Remove the star ratings from the Testimonials section
content = re.sub(r'<div class="flex justify-center gap-1 text-yellow-400">.*?</div>', '', content, flags=re.DOTALL)

# 7. Our Process - Add 2 additional tabs
process_tabs = """                            <!-- Active Button -->
                            <button
                                class="w-full text-left px-6 py-4 rounded-2xl bg-brand-dark text-white font-extrabold flex justify-between items-center transition-all shadow-md group border border-brand-dark">
                                Fixed Cost Project
                                <i data-lucide="chevron-right"
                                    class="w-5 h-5 text-white/70 group-hover:text-white transition-colors"></i>
                            </button>
                            <!-- Inactive Button 1 -->
                            <button
                                class="w-full text-left px-6 py-4 rounded-2xl bg-white border border-[#EDEDED] text-[#4A4A4A] font-extrabold flex justify-between items-center hover:border-[#1F3D5A] hover:text-[#1F3D5A] transition-all group">
                                Hire Dedicated Developer(s)
                                <i data-lucide="chevron-right"
                                    class="w-5 h-5 text-[#4A4A4A]/40 group-hover:text-[#1F3D5A] transition-colors"></i>
                            </button>
                            <!-- Inactive Button 2 -->
                            <button
                                class="w-full text-left px-6 py-4 rounded-2xl bg-white border border-[#EDEDED] text-[#4A4A4A] font-extrabold flex justify-between items-center hover:border-[#1F3D5A] hover:text-[#1F3D5A] transition-all group">
                                Agile Development Process
                                <i data-lucide="chevron-right"
                                    class="w-5 h-5 text-[#4A4A4A]/40 group-hover:text-[#1F3D5A] transition-colors"></i>
                            </button>"""

new_tabs = process_tabs + """
                            <!-- Inactive Button 3 -->
                            <button
                                class="w-full text-left px-6 py-4 rounded-2xl bg-white border border-[#EDEDED] text-[#4A4A4A] font-extrabold flex justify-between items-center hover:border-[#1F3D5A] hover:text-[#1F3D5A] transition-all group">
                                Time & Material Model
                                <i data-lucide="chevron-right"
                                    class="w-5 h-5 text-[#4A4A4A]/40 group-hover:text-[#1F3D5A] transition-colors"></i>
                            </button>
                            <!-- Inactive Button 4 -->
                            <button
                                class="w-full text-left px-6 py-4 rounded-2xl bg-white border border-[#EDEDED] text-[#4A4A4A] font-extrabold flex justify-between items-center hover:border-[#1F3D5A] hover:text-[#1F3D5A] transition-all group">
                                Offshore Development Center
                                <i data-lucide="chevron-right"
                                    class="w-5 h-5 text-[#4A4A4A]/40 group-hover:text-[#1F3D5A] transition-colors"></i>
                            </button>"""

content = content.replace(process_tabs, new_tabs)

with open('index.html', 'w') as f:
    f.write(content)
