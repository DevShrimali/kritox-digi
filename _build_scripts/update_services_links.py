import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    dirname = os.path.dirname(filepath)
    if dirname == '' or dirname == '.':
        prefix = "services/"
    else:
        prefix = "../services/"

    original_content = content

    services = {
        "Web Development": "web-development.html",
        "UI/UX Design": "ui-ux-design.html",
        "Mobile Apps": "mobile-apps.html",
        "Digital Marketing": "digital-marketing.html",
        "Brand Strategy": "brand-strategy.html",
        "Cloud Solutions": "cloud-solutions.html"
    }

    for name, slug in services.items():
        # Build regex for the text allowing newlines and spaces
        name_parts = name.split()
        name_regex = r'\s*'.join([re.escape(part) for part in name_parts])

        # Mega Menu Pattern
        # Use (?:(?!<a\s).)*? to prevent matching across multiple <a> tags
        pattern = r'(<a\s+href=")[^"]+("\s+class="group\s+flex\s+gap-3\s+items-start">(?:(?!<a\s).)*?<p\s+class="font-bold[^>]+>\s*' + name_regex + r'\s*</p>)'
        replacement = r'\g<1>' + prefix + slug + r'\g<2>'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Mobile Menu Pattern
        mobile_pattern = r'(<a\s+href=")[^"]+("\s+class="block\s+text-\[12px\]\s+font-semibold\s+text-\[#[0-9A-F]+\]\s+hover:text-\[#[0-9A-F]+\]">\s*' + name_regex + r'\s*</a>)'
        mobile_replacement = r'\g<1>' + prefix + slug + r'\g<2>'
        content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    if '_build_scripts' in root or '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            if filepath.startswith('./'):
                filepath = filepath[2:]
            process_file(filepath)

print("Done")
