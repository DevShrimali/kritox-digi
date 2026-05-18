import os

file_path = '/Users/devshrimali/Documents/Work/AEC/kritox-digi/portfolio/index.html'
with open(file_path, 'r') as f:
    content = f.read()

filter_html = """
            <!-- Filter Category -->
            <div class="flex flex-wrap justify-center gap-3 mb-12">
                <button class="px-5 py-2 rounded-full bg-[#1F3D5A] text-white text-[14px] font-bold shadow-md transition-all">All Projects</button>
                <button class="px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">Web Design</button>
                <button class="px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">Mobile App</button>
                <button class="px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">SaaS</button>
                <button class="px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">E-Commerce</button>
            </div>
"""

# Replace the grid opening
old_grid = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">'
new_grid = filter_html + '\n            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">'

content = content.replace(old_grid, new_grid)

with open(file_path, 'w') as f:
    f.write(content)

print("Updated portfolio index page layout and filters!")
