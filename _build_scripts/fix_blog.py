import re
import os

with open("blog/index.html", "r") as f:
    content = f.read()

# 1. Fix hero section
hero_pattern = r"(<!-- Blog Hero Section -->.*?<section class=\"relative bg-white text-\[\#1F3D5A\].*?)(</section>)"
hero_match = re.search(hero_pattern, content, flags=re.DOTALL)
if hero_match:
    hero = hero_match.group(1)
    hero = re.sub(r"<section class=\"relative bg-white[^\"]*\">", "<section class=\"inner-hero selection-style\">", hero)
    hero = re.sub(r"text-\[\#1F3D5A\]", "", hero) # Clean up colors so it uses default
    
    # Add breadcrumb
    breadcrumb = """<nav class="inner-breadcrumb" aria-label="Breadcrumb">
                <a href="../index.html">Home</a>
                <i data-lucide="chevron-right"></i>
                <span>Blog</span>
            </nav>"""
    
    # Insert breadcrumb before closing div
    hero = re.sub(r"(\s*)(</div>\s*)$", r"\1    " + breadcrumb + r"\1\2", hero)
    
    content = content[:hero_match.start()] + hero + content[hero_match.end()-10:]

# 2. Extract one card from the grid to repeat
card_pattern = r"(<!-- Card 1 -->.*?)(?=<!-- Card 2 -->)"
card_match = re.search(card_pattern, content, flags=re.DOTALL)
if card_match:
    card_html = card_match.group(1).strip()
else:
    print("Could not find Card 1")
    exit(1)

# Generate 9 cards
grid_content = ""
for i in range(1, 10):
    grid_content += f"\n                <!-- Card {i} -->\n                {card_html}\n"

# Pagination HTML
pagination = """
            <!-- Pagination -->
            <div class="mt-16 flex justify-center items-center gap-2">
                <button class="w-10 h-10 flex items-center justify-center rounded-full border border-[#EDEDED] text-[#4A4A4A] hover:bg-[#1F3D5A] hover:text-white hover:border-[#1F3D5A] transition-all disabled:opacity-50 disabled:hover:bg-transparent disabled:hover:text-[#4A4A4A] disabled:hover:border-[#EDEDED]" disabled>
                    <i data-lucide="chevron-left" class="w-4 h-4"></i>
                </button>
                <button class="w-10 h-10 flex items-center justify-center rounded-full bg-[#1F3D5A] text-white font-bold transition-all">
                    1
                </button>
                <button class="w-10 h-10 flex items-center justify-center rounded-full border border-[#EDEDED] text-[#4A4A4A] font-bold hover:bg-[#FAFAFA] transition-all">
                    2
                </button>
                <button class="w-10 h-10 flex items-center justify-center rounded-full border border-[#EDEDED] text-[#4A4A4A] font-bold hover:bg-[#FAFAFA] transition-all">
                    3
                </button>
                <span class="px-2 text-[#4A4A4A]">...</span>
                <button class="w-10 h-10 flex items-center justify-center rounded-full border border-[#EDEDED] text-[#4A4A4A] font-bold hover:bg-[#FAFAFA] transition-all">
                    8
                </button>
                <button class="w-10 h-10 flex items-center justify-center rounded-full border border-[#EDEDED] text-[#4A4A4A] hover:bg-[#1F3D5A] hover:text-white hover:border-[#1F3D5A] transition-all">
                    <i data-lucide="chevron-right" class="w-4 h-4"></i>
                </button>
            </div>
"""

# Replace everything from "<!-- Featured Post -->" to "<!-- Footer -->" with the new grid
new_section = f"""
    <!-- Blog Grid -->
    <section class="bg-white py-24 border-t border-[#EDEDED]">
        <div class="max-w-7xl mx-auto px-6 md:px-10">
            <div class="grid md:grid-cols-3 gap-8 md:gap-10">
{grid_content}
            </div>
{pagination}
        </div>
    </section>

"""

content = re.sub(r"<!-- Featured Post -->.*?<!-- Footer -->", new_section + "<!-- Footer -->", content, flags=re.DOTALL)

with open("blog/index.html", "w") as f:
    f.write(content)

print("Fixed blog/index.html")

