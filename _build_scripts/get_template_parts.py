import re

with open('services/brand-strategy.html', 'r', encoding='utf-8') as f:
    content = f.read()

head = content[:content.find('<!-- WordPress Hero Section -->')]
if head == content:
    head = content[:content.find('<!-- Hero Section -->')]

footer = content[content.find('<!-- Footer -->'):]

with open('_build_scripts/head_template.html', 'w', encoding='utf-8') as f:
    f.write(head)

with open('_build_scripts/footer_template.html', 'w', encoding='utf-8') as f:
    f.write(footer)

