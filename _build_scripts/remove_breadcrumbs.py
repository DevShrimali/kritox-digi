import os
import re
import glob

# Search in specific files that showed up in grep
files_to_check = [
    'faq.html',
    'case-studies/index.html',
    'hire/mobile-developers.html',
    'hire/mean-stack.html',
    'hire/full-stack.html',
    'hire/web-developers.html',
    'hire/mern-stack.html',
    'hire/python.html',
    'career.html',
    'testimonials.html',
    'blog/index.html'
]

breadcrumb_pattern = re.compile(r'\s*<nav[^>]*class="inner-breadcrumb[^>]*>.*?<\/nav>', re.DOTALL)

for rel_path in files_to_check:
    filepath = os.path.join('/Users/devshrimali/Documents/Work/AEC/kritox-digi', rel_path)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, count = breadcrumb_pattern.subn('', content)
        
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed breadcrumbs from {rel_path} ({count} occurrences)")
        else:
            print(f"No breadcrumbs found in {rel_path}")

