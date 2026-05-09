import re

with open('index.html', 'r') as f:
    content = f.read()

# Define the old footer links section
# We will use regex to find the Right Column (Links Groups)
pattern = r'<!-- Right Column \(Links Groups\) -->.*?</div>\s*</div>\s*<!-- Certifications Banner -->'
match = re.search(pattern, content, re.DOTALL)

if match:
    old_section = match.group(0)
    
    new_section = """<!-- Right Column (Links Groups) -->
                <div class="lg:w-3/4 flex flex-col gap-8">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
                        
                        <!-- Group 1 -->
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] text-base mb-5">AI Services</h4>
                            <ul class="space-y-3 text-[14px] text-[#4A4A4A]">
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Artificial Intelligence</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Generative AI</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Generative AI Integration</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">AI Consulting</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">AI Model Fine-Tuning</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">AI Proof-of-Concept (POC)</a></li>
                            </ul>
                        </div>

                        <!-- Group 2 -->
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] text-base mb-5">Development Services</h4>
                            <ul class="space-y-3 text-[14px] text-[#4A4A4A]">
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Enterprise Software</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Mobile App Development</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Web Development</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">MVP Development</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Software Product Development</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">eCommerce Development</a></li>
                            </ul>
                        </div>

                        <!-- Group 3 -->
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] text-base mb-5">Hire Developers</h4>
                            <ul class="space-y-3 text-[14px] text-[#4A4A4A]">
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">MEAN Stack Developers</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">MERN Stack Developers</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Full Stack Developers</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Python Developers</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Web Developers</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Mobile Developers</a></li>
                            </ul>
                        </div>

                        <!-- Group 4 -->
                        <div>
                            <h4 class="font-bold text-[#1F3D5A] text-base mb-5">Company</h4>
                            <ul class="space-y-3 text-[14px] text-[#4A4A4A]">
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">About Us</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Career</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Blog</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Portfolio</a></li>
                                <li><a href="#" class="hover:text-[#2F6F73] hover:translate-x-1 transition-all inline-block">Q&A</a></li>
                            </ul>
                        </div>

                    </div>
                </div>
            </div>

            <!-- Certifications Banner -->"""
    
    content = content.replace(old_section, new_section)
    print("Footer replaced.")
else:
    print("Could not find footer section.")

with open('index.html', 'w') as f:
    f.write(content)

