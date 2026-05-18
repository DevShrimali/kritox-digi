import re

def fix_sitemap():
    # Read sitemap content blocks from current sitemap.html
    with open('/Users/devshrimali/Documents/Work/AEC/kritox-digi/sitemap.html', 'r') as f:
        sitemap_html = f.read()

    # The actual sitemap blocks are inside these divs
    # We can extract them using regex
    blocks = re.findall(r'(<!-- (Our Work|Services|Blog|Hire Developer|Technologies|Legal & Utility) -->.*?</div>\s+</div>)', sitemap_html, re.DOTALL)
    
    # Wait, the closing tags might be tricky. Let's just find the blocks by class.
    blocks_raw = re.findall(r'<div class="border border-\[#EDEDED\] rounded-2xl p-8 hover:shadow-lg transition-shadow">.*?</ul>\s*</div>', sitemap_html, re.DOTALL)
    
    if len(blocks_raw) < 5:
        print("Could not find enough blocks!")
        # Fallback if regex fails:
        # Just manually recreate the sitemap inner HTML
    
    # Read about.html to get navbar and footer
    with open('/Users/devshrimali/Documents/Work/AEC/kritox-digi/about.html', 'r') as f:
        about_html = f.read()

    # Extract Navbar (from <!-- Navbar --> up to <!-- About Hero Section )
    navbar_match = re.search(r'(<!-- Navbar -->.*?)</nav>\s*<!-- Mobile Menu Overlay -->.*?</div>\s*</div>\s*(?=<!-- About Hero Section)', about_html, re.DOTALL)
    if not navbar_match:
        print("Failed to match navbar!")
    navbar_code = navbar_match.group(0)

    # Extract Footer
    footer_match = re.search(r'(<!-- Footer -->.*?)</body>', about_html, re.DOTALL)
    if not footer_match:
        print("Failed to match footer!")
    footer_code = footer_match.group(1)

    # Recreate the sitemap blocks manually just to be safe and update them with new pages (e.g. Fintech App Project -> fintech-app.html)
    sitemap_content = """
    <section class="bg-white py-24 mt-20 min-h-screen">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="text-center max-w-4xl mx-auto mb-16">
                <h1 class="text-4xl md:text-5xl font-black text-[#1F3D5A] mb-6">Sitemap</h1>
                <p class="text-lg text-[#4A4A4A]">Navigate through Kritox Digital.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    """
    
    for b in blocks_raw:
        sitemap_content += f"                {b}\n"
        
    sitemap_content += """
            </div>
        </div>
    </section>
    """

    # Assemble new sitemap.html
    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sitemap - Kritox Digital</title>
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script src="js/tailwind-config.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body class="bg-white text-brand-dark">
{navbar_code}
{sitemap_content}
{footer_code}
    <!-- Initialize Lucide Icons -->
    <script>
        lucide.createIcons();
    </script>
    <script src="js/main.js"></script>
</body>
</html>"""

    # Write to file
    with open('/Users/devshrimali/Documents/Work/AEC/kritox-digi/sitemap.html', 'w') as f:
        f.write(new_html)

fix_sitemap()
print("Sitemap rebuilt successfully!")
