import re

def update_page(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update the Gallery Section
    old_gallery = r'<!-- Gallery Section -->\s*<h2 class="text-3xl font-black text-\[#1F3D5A\] mb-8">Gallery</h2>\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-20">.*?</div>'
    
    new_gallery = """<!-- Gallery Section -->
            <h2 class="text-3xl font-black text-[#1F3D5A] mb-8">Gallery</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-20" id="portfolio-gallery">
                <img src="https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-[200px] object-cover rounded-[1rem] shadow-sm hover:shadow-md transition-shadow cursor-pointer gallery-trigger" data-index="0">
                <img src="https://images.pexels.com/photos/1779487/pexels-photo-1779487.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-[200px] object-cover rounded-[1rem] shadow-sm hover:shadow-md transition-shadow cursor-pointer gallery-trigger" data-index="1">
                <img src="https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-[200px] object-cover rounded-[1rem] shadow-sm hover:shadow-md transition-shadow cursor-pointer gallery-trigger" data-index="2">
                <div class="relative w-full h-[200px] rounded-[1rem] overflow-hidden cursor-pointer group gallery-trigger" data-index="3">
                    <img src="https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-black/60 flex items-center justify-center group-hover:bg-black/50 transition-colors">
                        <span class="text-white text-3xl font-black">+4</span>
                    </div>
                </div>
            </div>"""
    
    content = re.sub(old_gallery, new_gallery, content, flags=re.DOTALL)

    # 2. Update the "More Portfolio" title to standard left-aligned
    old_more = r'<div class="text-center max-w-4xl">\s*<h2 class="text-3xl md:text-5xl font-black text-brand-dark mb-6 tracking-tight">More Portfolio</h2>\s*</div>'
    
    new_more = """<div class="flex flex-col md:flex-row md:items-end justify-between gap-8 mb-6">
                <div>
                    <div class="inline-block px-4 py-1.5 border border-[#1F3D5A] text-[#1F3D5A] text-xs font-bold uppercase tracking-[0.15em] rounded-full mb-6 hover:bg-[#1F3D5A] hover:text-white transition-colors cursor-pointer">
                        Our Work
                    </div>
                    <h2 class="text-3xl md:text-5xl font-black text-brand-dark leading-tight shrink-0">
                        More <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-base to-[#E5B93C]">Portfolio.</span>
                    </h2>
                </div>
                <a href="../portfolio/index.html" class="inline-flex items-center gap-2 font-bold text-brand-base hover:text-brand-dark transition-colors">
                    View All Projects <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </a>
            </div>"""
            
    content = re.sub(old_more, new_more, content, flags=re.DOTALL)
    
    # 3. Add Modal HTML before </body>
    modal_html = """
    <!-- Image Gallery Modal -->
    <div id="gallery-modal" class="fixed inset-0 z-[200] bg-black/95 opacity-0 pointer-events-none transition-opacity duration-300 flex items-center justify-center">
        <button id="close-gallery" class="absolute top-6 right-6 text-white/70 hover:text-white transition-colors z-[210]">
            <i data-lucide="x" class="w-10 h-10"></i>
        </button>
        
        <button id="prev-gallery" class="absolute left-6 text-white/70 hover:text-white transition-colors z-[210]">
            <i data-lucide="chevron-left" class="w-12 h-12"></i>
        </button>
        
        <img id="gallery-image" src="" class="max-h-[85vh] max-w-[90vw] object-contain select-none transition-opacity duration-300">
        
        <button id="next-gallery" class="absolute right-6 text-white/70 hover:text-white transition-colors z-[210]">
            <i data-lucide="chevron-right" class="w-12 h-12"></i>
        </button>
        
        <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-white/70 font-medium">
            <span id="gallery-counter">1</span> / <span id="gallery-total">8</span>
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const galleryImages = [
                "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200",
                "https://images.pexels.com/photos/1779487/pexels-photo-1779487.jpeg?auto=compress&cs=tinysrgb&w=1200",
                "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200",
                "https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=1200",
                "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200",
                "https://images.pexels.com/photos/1779487/pexels-photo-1779487.jpeg?auto=compress&cs=tinysrgb&w=1200",
                "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200",
                "https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=1200"
            ];
            
            const modal = document.getElementById('gallery-modal');
            const mainImg = document.getElementById('gallery-image');
            const closeBtn = document.getElementById('close-gallery');
            const prevBtn = document.getElementById('prev-gallery');
            const nextBtn = document.getElementById('next-gallery');
            const counter = document.getElementById('gallery-counter');
            const total = document.getElementById('gallery-total');
            
            let currentIndex = 0;
            total.textContent = galleryImages.length;
            
            document.querySelectorAll('.gallery-trigger').forEach(trigger => {
                trigger.addEventListener('click', (e) => {
                    currentIndex = parseInt(e.currentTarget.dataset.index);
                    updateGallery();
                    modal.classList.remove('opacity-0', 'pointer-events-none');
                    document.body.style.overflow = 'hidden';
                });
            });
            
            const updateGallery = () => {
                mainImg.style.opacity = '0.5';
                setTimeout(() => {
                    mainImg.src = galleryImages[currentIndex];
                    mainImg.style.opacity = '1';
                }, 150);
                counter.textContent = currentIndex + 1;
            };
            
            const nextImg = () => {
                currentIndex = (currentIndex + 1) % galleryImages.length;
                updateGallery();
            };
            
            const prevImg = () => {
                currentIndex = (currentIndex - 1 + galleryImages.length) % galleryImages.length;
                updateGallery();
            };
            
            nextBtn.addEventListener('click', nextImg);
            prevBtn.addEventListener('click', prevImg);
            
            closeBtn.addEventListener('click', () => {
                modal.classList.add('opacity-0', 'pointer-events-none');
                document.body.style.overflow = '';
            });
            
            // Keyboard nav
            document.addEventListener('keydown', (e) => {
                if(modal.classList.contains('opacity-0')) return;
                if(e.key === 'Escape') closeBtn.click();
                if(e.key === 'ArrowRight') nextImg();
                if(e.key === 'ArrowLeft') prevImg();
            });
        });
    </script>
    """
    
    if "<!-- Image Gallery Modal -->" not in content:
        content = content.replace('</body>', modal_html + '\n</body>')

    with open(file_path, 'w') as f:
        f.write(content)

update_page('/Users/devshrimali/Documents/Work/AEC/kritox-digi/portfolio/fintech-app.html')
update_page('/Users/devshrimali/Documents/Work/AEC/kritox-digi/portfolio/saas-platform.html')

print("Gallery updated successfully!")
