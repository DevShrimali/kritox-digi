import os
import glob
import re

# Find all HTML files
html_files = glob.glob('**/*.html', recursive=True)

for file_path in html_files:
    if "template_content.html" in file_path or "_build_scripts" in file_path or "w3nuts" in file_path:
        continue
        
    with open(file_path, 'r') as f:
        content = f.read()
        
    original_content = content
    
    # Path adjustment for links
    depth = file_path.count('/')
    prefix = '../' * depth if depth > 0 else ''
    
    # Mobile Menu Replacement
    mobile_target = r'(<a href="[^"]*" class="block text-\[12px\] font-semibold text-\[#4A4A4A\] hover:text-\[#2F6F73\]">\s*AI &\s*ML</a>\s*)</div>'
    mobile_replacement = r'\1    <a href="' + prefix + r'tech/wordpress.html" class="block text-[12px] font-semibold text-[#4A4A4A] hover:text-[#2F6F73]">WordPress</a>\n                </div>'
    
    content = re.sub(mobile_target, mobile_replacement, content)
    
    # Mega Menu Replacement
    # Find the CI/CD block
    mega_target = r'(<p\s+class="font-bold text-\[#1F3D5A\] text-\[14px\] group-hover:text-\[#2F6F73\] transition-colors">\s*CI/CD & DevOps</p>\s*<p class="text-\[12px\] text-\[#4A4A4A\] mt-0\.5">Automated pipelines</p>\s*</div>\s*</a>)'
    
    mega_replacement = r'\1\n                                <a href="' + prefix + r'tech/wordpress.html" class="group flex gap-3 items-start">\n                                    <div class="bg-white p-2 rounded-lg text-[#2F6F73] shrink-0 mt-0.5 border border-[#EDEDED]">\n                                        <i data-lucide="layout-template" class="w-4 h-4"></i>\n                                    </div>\n                                    <div>\n                                        <p class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">\n                                            WordPress</p>\n                                        <p class="text-[12px] text-[#4A4A4A] mt-0.5">Custom development</p>\n                                    </div>\n                                </a>'
    
    content = re.sub(mega_target, mega_replacement, content)
    
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated {file_path}")
