import os
import re

url_map = {
    'case-study.html': 'case-studies/index.html',
    'case-study-details.html': 'case-studies/template.html',
    'cs-fintech.html': 'case-studies/fintech.html',
    'cs-saas.html': 'case-studies/saas.html',
    'cs-ecommerce.html': 'case-studies/ecommerce.html',
    'cs-cloud.html': 'case-studies/cloud.html',
    'blog.html': 'blog/index.html',
    'blog-details.html': 'blog/template.html',
    'tech-react.html': 'tech/react.html',
    'tech-node.html': 'tech/node.html',
    'tech-databases.html': 'tech/databases.html',
    'tech-aws.html': 'tech/aws.html',
    'tech-mobile.html': 'tech/mobile.html',
    'tech-ai.html': 'tech/ai.html',
    'tech-docker.html': 'tech/docker.html',
    'tech-cicd.html': 'tech/cicd.html'
}

def replace_in_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_url, new_url in url_map.items():
        # Match href="old" or src="old"
        content = re.sub(r'(href|src)="' + re.escape(old_url) + r'"', r'\1="' + new_url + r'"', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html
replace_in_file('index.html')

# Update all build scripts
scripts_dir = '_build_scripts'
if os.path.exists(scripts_dir):
    for filename in os.listdir(scripts_dir):
        if filename.endswith('.html'):
            replace_in_file(os.path.join(scripts_dir, filename))

print("URLs refactored in source files.")
