import re

with open("blog/template.html", "r") as f:
    content = f.read()

# 1. Update hero header
# Old: <section class="bg-white pt-20 pb-6 md:pt-24 md:pb-8">
# New: <section class="bg-[#FFFBF0] pt-12 pb-6 md:pt-16 md:pb-8 selection-style">
content = content.replace(
    '<section class="bg-white pt-20 pb-6 md:pt-24 md:pb-8">',
    '<section class="bg-[#FFFBF0] pt-12 pb-6 md:pt-16 md:pb-8 selection-style">'
)

# 2. Blog Title 24px
# Old: <h1 class="font-black text-4xl md:text-5xl lg:text-6xl tracking-tight leading-[1.1] mb-10 text-[#1A1A1A] max-w-4xl mx-auto" style="font-family: 'Plus Jakarta Sans', sans-serif;">
# New: <h1 class="font-black text-2xl tracking-tight leading-[1.1] mb-10 text-[#1A1A1A] max-w-4xl mx-auto" style="font-family: 'Plus Jakarta Sans', sans-serif;">
content = re.sub(
    r'<h1 class="font-black text-4xl md:text-5xl lg:text-6xl tracking-tight leading-\[1\.1\] mb-10 text-\[\#1A1A1A\] max-w-4xl mx-auto"',
    r'<h1 class="font-black text-[24px] tracking-tight leading-[1.1] mb-10 text-[#1A1A1A] max-w-4xl mx-auto"',
    content
)

# 3. Blog body content 18px
# Old: <article class="text-[#2A2A2A] text-xl leading-[1.8] font-medium">
# New: <article class="text-[#2A2A2A] text-[18px] leading-[1.8] font-medium">
content = content.replace(
    '<article class="text-[#2A2A2A] text-xl leading-[1.8] font-medium">',
    '<article class="text-[#2A2A2A] text-[18px] leading-[1.8] font-medium">'
)

# 4. Remove "Section Contents" under "More Blogs"
# Specifically the <p class="text-lg text-[#4A4A4A] leading-relaxed max-w-3xl mx-auto">
# that contains "We work with our clients to create online strategies..."
p_pattern = r'<p class="text-lg text-\[\#4A4A4A\] leading-relaxed max-w-3xl mx-auto">\s*We work with our clients to create online strategies that produce more traffic, more leads, and more\s*business\. Our teams use combination of expertises, knowledges and experiences to deliver the best\s*digital results\.\s*</p>'
content = re.sub(p_pattern, '', content)

with open("blog/template.html", "w") as f:
    f.write(content)

print("Updated blog/template.html")
