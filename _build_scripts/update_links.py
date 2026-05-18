import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    if file.startswith('.git'): continue
    with open(file, 'r') as f:
        content = f.read()

    # Desktop menu Company -> Engagement Model
    # It might be in different depth, so href="services.html" or href="../services.html"
    
    # Let's replace the chunk containing the link for Engagement Model.
    
    # Pattern 1 (Desktop)
    # <a href="services.html" class="group flex gap-4 items-start">
    # ...
    # Engagement Model</p>
    
    # This is tricky with regex. Let's do it with split and replace.
    # Actually, we can use regex because the structure is quite consistent.
    
    import re
    # Desktop
    content = re.sub(
        r'<a href="([^"]*)services.html"([^>]*)>\s*(<div[^>]*>.*?</div>)\s*<div>\s*<p[^>]*>\s*Engagement Model</p>',
        r'<a href="\1engagement-models.html"\2>\n                                    \3\n                                    <div>\n                                        <p\n                                            class="font-bold text-brand-dark text-[14px] group-hover:text-brand-base transition-colors">\n                                            Engagement Model</p>',
        content,
        flags=re.DOTALL
    )
    
    # Some pages might have text-[#1F3D5A] instead of text-brand-dark
    content = re.sub(
        r'<a href="([^"]*)services.html"([^>]*)>\s*(<div[^>]*>.*?</div>)\s*<div>\s*<p[^>]*>\s*Engagement Model</p>',
        r'<a href="\1engagement-models.html"\2>\n                                    \3\n                                    <div>\n                                        <p\n                                            class="font-bold text-[#1F3D5A] text-[14px] group-hover:text-[#2F6F73] transition-colors">\n                                            Engagement Model</p>',
        content,
        flags=re.DOTALL
    )

    # Mobile menu
    # <a href="services.html" class="...">Engagement\n                        Model</a>
    content = re.sub(
        r'<a href="([^"]*)services.html"([^>]*)>\s*Engagement\s*Model</a>',
        r'<a href="\1engagement-models.html"\2>Engagement Model</a>',
        content,
        flags=re.DOTALL
    )

    # Footer link (if there is one)
    # Let's check footer
    content = re.sub(
        r'<a href="([^"]*)services.html"([^>]*)>Engagement Model</a>',
        r'<a href="\1engagement-models.html"\2>Engagement Model</a>',
        content,
        flags=re.DOTALL
    )

    with open(file, 'w') as f:
        f.write(content)
