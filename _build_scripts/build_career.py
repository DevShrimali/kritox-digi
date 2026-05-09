import os
import re

def build_career():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract Header (everything before <!-- Hero Section -->)
    hero_index = content.find('<!-- Hero Section -->')
    if hero_index == -1:
        print("Could not find <!-- Hero Section -->")
        return
        
    header = content[:hero_index]
    
    # Extract Footer (everything from <!-- Footer -->)
    footer_index = content.find('<!-- Footer -->')
    if footer_index == -1:
        print("Could not find <!-- Footer -->")
        return
        
    footer = content[footer_index:]
    
    # Read career main content
    with open('_build_scripts/career_content.html', 'r', encoding='utf-8') as f:
        main_content = f.read()
        
    # Combine and save to career.html
    career_html = header + main_content + footer
    
    # Let's also make sure the body class is suitable for dark mode below the navbar.
    # The navbar itself has bg-white, which is fine, but the body has bg-white. 
    # That's okay because our sections have bg-[#0A0A0A].
    
    with open('career.html', 'w', encoding='utf-8') as f:
        f.write(career_html)
        
    print("Successfully built career.html")

if __name__ == '__main__':
    build_career()
