import os
import re

files = [
    'index.html', 'about.html', 'career.html', 'contact.html', 
    'faq.html', 'life-at-kritox.html', 'sitemap.html', 'testimonials.html'
]

target = r'<button\s+class="nav-link-item flex items-center gap-1 py-2 px-3 text-\[16px\] text-neutral-dark font-semibold hover:text-brand-base transition-colors">\s*Services <i data-lucide="chevron-down" class="w-3 h-3"></i>\s*</button>'
replacement = r'<a href="services.html" class="nav-link-item flex items-center gap-1 py-2 px-3 text-[16px] text-neutral-dark font-semibold hover:text-brand-base transition-colors">Services <i data-lucide="chevron-down" class="w-3 h-3"></i></a>'

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        new_content = re.sub(target, replacement, content, flags=re.MULTILINE | re.DOTALL)
        
        if new_content != content:
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No match in {filename}")
