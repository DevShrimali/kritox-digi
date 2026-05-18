import re

file_path = '/Users/devshrimali/Documents/Work/AEC/kritox-digi/portfolio/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# Replace links
content = content.replace('project-1.html', 'fintech-app.html')
content = content.replace('project-2.html', 'saas-platform.html')

# Replace EXPLORE NOW with VIEW PROJECT
content = content.replace('EXPLORE NOW', 'VIEW PROJECT')

tags_fintech = """<div class="flex flex-wrap gap-2 mb-8">
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">Mobile App</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">Fintech</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">UI/UX</span>
                        </div>"""

tags_saas = """<div class="flex flex-wrap gap-2 mb-8">
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">Web App</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">SaaS</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">Dashboard</span>
                        </div>"""

tags_ecommerce = """<div class="flex flex-wrap gap-2 mb-8">
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">E-Commerce</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">Web Portal</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">React</span>
                        </div>"""

tags_cloud = """<div class="flex flex-wrap gap-2 mb-8">
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">Cloud</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">DevOps</span>
                            <span class="px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-white text-[12px] font-semibold border border-white/30">Migration</span>
                        </div>"""

def replace_card_stats(match):
    title = match.group(1)
    
    if "Fintech" in title:
        replacement = tags_fintech
    elif "SaaS" in title:
        replacement = tags_saas
    elif "E-Commerce" in title:
        replacement = tags_ecommerce
    elif "Cloud" in title:
        replacement = tags_cloud
    else:
        replacement = tags_fintech # fallback
        
    return f'{title}\n                        {replacement}'

pattern = re.compile(r'(<h3[^>]*>.*?</h3>)\s*<div class="space-y-2 mb-8">.*?</div>', re.DOTALL)
content = pattern.sub(replace_card_stats, content)

with open(file_path, 'w') as f:
    f.write(content)

print("Updated portfolio cards successfully!")
