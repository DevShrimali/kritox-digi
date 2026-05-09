import os
import re

pages = {
    'testimonials.html': '_build_scripts/testimonials_content.html',
    'case-studies/index.html': '_build_scripts/case_study_content.html',
    'case-studies/template.html': '_build_scripts/case_study_details_content.html',
    'about.html': '_build_scripts/about_content.html',
    'blog/index.html': '_build_scripts/blog_content.html',
    'blog/template.html': '_build_scripts/blog_details_content.html',
    'faq.html': '_build_scripts/faq_content.html',
    'contact.html': '_build_scripts/contact_content.html',
    'services.html': '_build_scripts/services_content.html',
    'life-at-kritox.html': '_build_scripts/life_content.html',
    'sitemap.html': '_build_scripts/sitemap_content.html',
    'tech/react.html': '_build_scripts/tech-react_content.html',
    'tech/node.html': '_build_scripts/tech-node_content.html',
    'tech/databases.html': '_build_scripts/tech-databases_content.html',
    'tech/aws.html': '_build_scripts/tech-aws_content.html',
    'tech/mobile.html': '_build_scripts/tech-mobile_content.html',
    'tech/ai.html': '_build_scripts/tech-ai_content.html',
    'tech/docker.html': '_build_scripts/tech-docker_content.html',
    'tech/cicd.html': '_build_scripts/tech-cicd_content.html',
    'case-studies/fintech.html': '_build_scripts/cs-fintech_content.html',
    'case-studies/saas.html': '_build_scripts/cs-saas_content.html',
    'case-studies/ecommerce.html': '_build_scripts/cs-ecommerce_content.html',
    'case-studies/cloud.html': '_build_scripts/cs-cloud_content.html'
}

def adjust_paths(content, depth):
    if depth == 0:
        return content
        
    prefix = '../' * depth
    
    # We want to replace href="xxx" and src="xxx" where xxx doesn't start with http, //, #, mailto:, tel:, or /
    def replacer(match):
        attr = match.group(1)
        quote = match.group(2)
        url = match.group(3)
        
        if url.startswith(('http', '//', '#', 'mailto:', 'tel:', 'data:', '/')):
            return match.group(0)
            
        return f'{attr}={quote}{prefix}{url}{quote}'
        
    # Match href="..." or src="..."
    content = re.sub(r'(href|src)=([\'"])(.*?)\2', replacer, content)
    return content

def build_pages():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    hero_index = content.find('<!-- Hero Section -->')
    footer_index = content.find('<!-- Footer -->')
    
    if hero_index == -1 or footer_index == -1:
        print("Error: Could not find Header or Footer markers in index.html")
        return
        
    header = content[:hero_index]
    footer = content[footer_index:]
    
    for output_path, content_file in pages.items():
        if os.path.exists(content_file):
            with open(content_file, 'r', encoding='utf-8') as f:
                main_content = f.read()
            
            full_content = header + main_content + footer
            
            # Calculate directory depth
            depth = output_path.count('/')
            
            # Adjust paths for this depth
            adjusted_content = adjust_paths(full_content, depth)
            
            # Create directories if they don't exist
            out_dir = os.path.dirname(output_path)
            if out_dir and not os.path.exists(out_dir):
                os.makedirs(out_dir)
                
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(adjusted_content)
            print(f'Built {output_path}')
        else:
            print(f'Missing {content_file}, skipping.')

if __name__ == '__main__':
    build_pages()
