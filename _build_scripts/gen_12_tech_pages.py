import os
import re

techs = [
    {"file": "brand-design.html", "name": "Brand Design", "cat": "Design Engineering", "img": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf", "icon": "pen-tool"},
    {"file": "uiux.html", "name": "UI/UX", "cat": "Design Engineering", "img": "https://images.unsplash.com/photo-1561070791-2526d30994b5", "icon": "layout"},
    {"file": "web-design.html", "name": "Web Design", "cat": "Design Engineering", "img": "https://images.unsplash.com/photo-1547658719-da2b51169166", "icon": "monitor"},
    {"file": "react.html", "name": "React.js", "cat": "Frontend Engineering", "img": "https://images.unsplash.com/photo-1633356122544-f134324a6cee", "icon": "code"},
    {"file": "node.html", "name": "Node.js", "cat": "Backend Engineering", "img": "https://images.unsplash.com/photo-1555099962-4199c345e5dd", "icon": "server"},
    {"file": "vue.html", "name": "Vue.js", "cat": "Frontend Engineering", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71", "icon": "code"},
    {"file": "angular.html", "name": "Angular.js", "cat": "Frontend Engineering", "img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97", "icon": "code"},
    {"file": "python.html", "name": "Python", "cat": "Backend Engineering", "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5", "icon": "terminal"},
    {"file": "laravel.html", "name": "Laravel", "cat": "Backend Engineering", "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c", "icon": "server"},
    {"file": "php.html", "name": "PHP", "cat": "Backend Engineering", "img": "https://images.unsplash.com/photo-1599507593499-a3f7d1d08731", "icon": "server"},
    {"file": "ios.html", "name": "iOS", "cat": "Mobile Engineering", "img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c", "icon": "smartphone"},
    {"file": "android.html", "name": "Android", "cat": "Mobile Engineering", "img": "https://images.unsplash.com/photo-1607252656733-fd7427926e5e", "icon": "smartphone"}
]

# Read template
with open('tech/mobile.html', 'r') as f:
    template = f.read()

# Fix font size in template (if not already 3.5rem)
template = re.sub(r'text-\[3rem\] md:text-\[3\.8rem\]', 'text-[2.5rem] md:text-[3.5rem]', template)

# Create/Update each tech page
for t in techs:
    content = template
    # Replace the Name
    content = content.replace("React Native &amp; Flutter", t["name"])
    content = content.replace("React Native & Flutter", t["name"])
    
    # Replace Category
    content = content.replace("Mobile Engineering", t["cat"])
    
    # Replace Image
    content = re.sub(r'https://images\.unsplash\.com/photo-1512428559087-[^"]+', t["img"] + '?auto=format&fit=crop&q=80&w=1000', content)
    
    # Write to file
    with open(f'tech/{t["file"]}', 'w') as f:
        f.write(content)
        
print("12 tech pages generated successfully.")
