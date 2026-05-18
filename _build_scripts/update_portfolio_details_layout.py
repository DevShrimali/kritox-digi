import re

def update_portfolio_detail(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # The block we want to replace starts with <!-- Details Content --> and ends before <!-- More Projects
    
    new_details = """    <!-- Details Content -->
    <section class="bg-white py-24">
        <div class="max-w-5xl mx-auto px-6 md:px-10">
            <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200" class="w-full h-auto rounded-[2rem] shadow-2xl mb-16">
            
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-16 mb-20">
                <div class="lg:col-span-2">
                    <h2 class="text-3xl font-black text-[#1F3D5A] mb-6">Project Overview</h2>
                    <p class="text-[#4A4A4A] text-lg leading-relaxed mb-10">
                        We partnered with the client to design and develop a robust, scalable, and highly intuitive platform from the ground up. By focusing on modern architecture and seamless user experience, we delivered a product that not only looks stunning but performs exceptionally well under heavy load.
                    </p>
                    <h2 class="text-3xl font-black text-[#1F3D5A] mb-6">Scope of Work</h2>
                    <ul class="space-y-3 text-lg text-[#4A4A4A] mb-10 list-disc pl-5 marker:text-[#2F6F73]">
                        <li>UI/UX Design & Prototyping</li>
                        <li>Frontend & Backend Development</li>
                        <li>Cloud Infrastructure Setup</li>
                        <li>Quality Assurance & Testing</li>
                    </ul>
                </div>
                <div class="bg-[#FAFAFA] p-8 rounded-[2rem] border border-[#EDEDED] h-fit">
                    <h3 class="text-xl font-bold text-[#1F3D5A] mb-6">Technologies Used</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1.5 bg-white border border-[#EDEDED] rounded-lg text-sm font-semibold text-[#4A4A4A]">React Native</span>
                        <span class="px-3 py-1.5 bg-white border border-[#EDEDED] rounded-lg text-sm font-semibold text-[#4A4A4A]">Node.js</span>
                        <span class="px-3 py-1.5 bg-white border border-[#EDEDED] rounded-lg text-sm font-semibold text-[#4A4A4A]">AWS</span>
                        <span class="px-3 py-1.5 bg-white border border-[#EDEDED] rounded-lg text-sm font-semibold text-[#4A4A4A]">Figma</span>
                        <span class="px-3 py-1.5 bg-white border border-[#EDEDED] rounded-lg text-sm font-semibold text-[#4A4A4A]">PostgreSQL</span>
                    </div>
                </div>
            </div>

            <!-- Gallery Section -->
            <h2 class="text-3xl font-black text-[#1F3D5A] mb-8">Gallery</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-20">
                <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-[300px] object-cover rounded-[1.5rem] shadow-md hover:shadow-xl transition-shadow cursor-pointer">
                <img src="https://images.pexels.com/photos/1779487/pexels-photo-1779487.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-[300px] object-cover rounded-[1.5rem] shadow-md hover:shadow-xl transition-shadow cursor-pointer">
            </div>

            <!-- KPI Counter Section -->
            <h2 class="text-3xl font-black text-[#1F3D5A] mb-8">Key Achievements</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 p-10 bg-[#1F3D5A] rounded-[2rem] shadow-xl text-center text-white">
                <div>
                    <p class="text-5xl font-black text-[#E5B93C] mb-3">40%</p>
                    <p class="font-bold text-white/90">User Growth</p>
                </div>
                <div class="md:border-x border-white/10">
                    <p class="text-5xl font-black text-[#E5B93C] mb-3">5M+</p>
                    <p class="font-bold text-white/90">Downloads</p>
                </div>
                <div>
                    <p class="text-5xl font-black text-[#E5B93C] mb-3">99.9%</p>
                    <p class="font-bold text-white/90">Uptime</p>
                </div>
            </div>
        </div>
    </section>"""
    
    # regex sub
    pattern = re.compile(r'<!-- Details Content -->.*?<!-- More Projects', re.DOTALL)
    
    # Custom main image based on file
    if "saas" in filepath:
        new_details = new_details.replace('1181244', '439391')
        new_details = new_details.replace('React Native', 'React.js')
        new_details = new_details.replace('5M+', '100+')
        new_details = new_details.replace('Downloads', 'B2B Clients')
        new_details = new_details.replace('40%', '3x')
        new_details = new_details.replace('User Growth', 'Efficiency')
    
    content = pattern.sub(new_details + '\n    <!-- More Projects', content)

    with open(filepath, 'w') as f:
        f.write(content)

update_portfolio_detail('/Users/devshrimali/Documents/Work/AEC/kritox-digi/portfolio/fintech-app.html')
update_portfolio_detail('/Users/devshrimali/Documents/Work/AEC/kritox-digi/portfolio/saas-platform.html')

print("Details updated successfully!")
