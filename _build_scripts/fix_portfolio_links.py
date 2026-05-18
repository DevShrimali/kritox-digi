import os
import glob

files = glob.glob('portfolio/*.html')

for file_path in files:
    with open(file_path, 'r') as f:
        content = f.read()
    
    content = content.replace('project-1.html', 'fintech-app.html')
    content = content.replace('project-2.html', 'saas-platform.html')
    content = content.replace('EXPLORE NOW', 'VIEW PROJECT')
    
    with open(file_path, 'w') as f:
        f.write(content)

print("Updated links and buttons in all portfolio pages!")
