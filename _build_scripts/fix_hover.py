import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

for file_path in html_files:
    if "template_content.html" in file_path or "w3nuts" in file_path:
        continue
        
    with open(file_path, 'r') as f:
        content = f.read()
        
    original_content = content
    content = content.replace('hover:bg-[#2F6F73]/10', 'hover:bg-gray-100')
    content = content.replace('hover:bg-brand-base/10', 'hover:bg-gray-100')
    
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated hovers in {file_path}")

print("Done updating hovers!")
