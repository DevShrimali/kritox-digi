import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

patterns = [
    ("tech/hire-mean-stack.html", "hire/mean-stack.html"),
    ("tech/hire-mern-stack.html", "hire/mern-stack.html"),
    ("tech/hire-full-stack.html", "hire/full-stack.html"),
    ("tech/hire-python.html", "hire/python.html"),
    ("tech/hire-web-developers.html", "hire/web-developers.html"),
    ("tech/hire-mobile-developers.html", "hire/mobile-developers.html")
]

for file_path in html_files:
    if "_build_scripts" in file_path: continue
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    original = content
    
    for old, new in patterns:
        old_basename = os.path.basename(old)
        new_basename = os.path.basename(new)
        
        content = content.replace(f'"{old}"', f'"{new}"')
        content = content.replace(f'"../{old}"', f'"../{new}"')
        
        if file_path.startswith("tech/"):
            content = content.replace(f'"{old_basename}"', f'"../hire/{new_basename}"')
            
        if file_path.startswith("hire/"):
            content = content.replace(f'"{old_basename}"', f'"{new_basename}"')
            
    if content != original:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Fixed links in {file_path}")

print("Done")
