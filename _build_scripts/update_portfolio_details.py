import re

def update_detail(file_path, new_title, new_desc, new_img):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Update title
    content = re.sub(r'<h1 class="font-black text-\[28px\] md:text-\[38px\].*?</h1>', 
                     f'<h1 class="font-black text-[28px] md:text-[38px] tracking-tight leading-[1.1] mb-6 text-[#1A1A1A] max-w-4xl mx-auto" style="font-family: \'Plus Jakarta Sans\', sans-serif;">\n                {new_title}\n            </h1>', 
                     content, flags=re.DOTALL)
    
    # Update description
    content = re.sub(r'<p class="text-lg text-\[#4A4A4A\] max-w-3xl mx-auto leading-relaxed mb-8">.*?</p>',
                     f'<p class="text-lg text-[#4A4A4A] max-w-3xl mx-auto leading-relaxed mb-8">{new_desc}</p>',
                     content, flags=re.DOTALL)
    
    # Update main image
    content = re.sub(r'<img src="[^"]+" class="w-full h-auto rounded-\[2rem\] shadow-2xl mb-16">',
                     f'<img src="{new_img}" class="w-full h-auto rounded-[2rem] shadow-2xl mb-16">',
                     content)

    with open(file_path, 'w') as f:
        f.write(content)

update_detail('portfolio/fintech-app.html', 
              'Revolutionizing Digital Banking with a Modern Mobile App',
              'How Kritox Digital helped a leading financial institution rebuild their mobile platform for scale, security and speed.',
              'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200')

update_detail('portfolio/saas-platform.html',
              'Enterprise SaaS Platform for Seamless B2B Integrations',
              'A highly scalable dashboard and API solution enabling enterprises to connect with hundreds of partners efficiently.',
              'https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=1200')

print("Updated detail pages successfully!")
