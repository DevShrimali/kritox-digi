import re

def update_portfolio_index():
    file_path = '/Users/devshrimali/Documents/Work/AEC/kritox-digi/portfolio/index.html'
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update Title above Filters
    old_grid_start = r'<!-- Filter Category -->'
    
    title_html = """<!-- Title -->
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-8 mb-12">
                <div>
                    <div class="inline-block px-4 py-1.5 border border-[#1F3D5A] text-[#1F3D5A] text-xs font-bold uppercase tracking-[0.15em] rounded-full mb-6 hover:bg-[#1F3D5A] hover:text-white transition-colors cursor-pointer">
                        Our Work
                    </div>
                    <h2 class="text-3xl md:text-5xl font-black text-brand-dark leading-tight shrink-0">
                        Featured <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-base to-[#E5B93C]">Projects.</span>
                    </h2>
                </div>
            </div>
            
            <!-- Filter Category -->"""
            
    content = content.replace(old_grid_start, title_html)
    
    # 2. Update Filter Buttons with data-filter
    old_filters = r'<div class="flex flex-wrap justify-center gap-3 mb-12">.*?</div>'
    
    new_filters = """<div class="flex flex-wrap justify-center md:justify-start gap-3 mb-12" id="portfolio-filters">
                <button data-filter="all" class="filter-btn active px-5 py-2 rounded-full bg-[#1F3D5A] text-white text-[14px] font-bold shadow-md transition-all">All Projects</button>
                <button data-filter="web-design" class="filter-btn px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">Web Design</button>
                <button data-filter="mobile-app" class="filter-btn px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">Mobile App</button>
                <button data-filter="saas" class="filter-btn px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">SaaS</button>
                <button data-filter="ecommerce" class="filter-btn px-5 py-2 rounded-full bg-[#FAFAFA] text-[#4A4A4A] border border-[#EDEDED] text-[14px] font-bold hover:bg-[#F0F4F8] hover:text-[#1F3D5A] transition-all">E-Commerce</button>
            </div>"""
    
    content = re.sub(old_filters, new_filters, content, flags=re.DOTALL)
    
    # 3. Add data-category to Cards
    # Item 1 -> Mobile App
    content = content.replace('<!-- Item 1 -->\n                <a href="../portfolio/fintech-app.html" class="block',
                              '<!-- Item 1 -->\n                <a href="../portfolio/fintech-app.html" data-category="mobile-app" class="portfolio-card block')
    # Item 2 -> SaaS
    content = content.replace('<!-- Item 2 -->\n                <a href="../portfolio/saas-platform.html" class="block',
                              '<!-- Item 2 -->\n                <a href="../portfolio/saas-platform.html" data-category="saas" class="portfolio-card block')
    # Item 3 -> Ecommerce
    content = content.replace('<!-- Item 3 -->\n                <a href="../portfolio/fintech-app.html" class="block',
                              '<!-- Item 3 -->\n                <a href="../portfolio/fintech-app.html" data-category="ecommerce" class="portfolio-card block')
                              
    # Add JS script before </body>
    filter_script = """
    <!-- Portfolio Filter Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const filterBtns = document.querySelectorAll('.filter-btn');
            const portfolioCards = document.querySelectorAll('.portfolio-card');
            
            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Update active styling
                    filterBtns.forEach(b => {
                        b.classList.remove('bg-[#1F3D5A]', 'text-white', 'shadow-md', 'active');
                        b.classList.add('bg-[#FAFAFA]', 'text-[#4A4A4A]');
                    });
                    btn.classList.remove('bg-[#FAFAFA]', 'text-[#4A4A4A]');
                    btn.classList.add('bg-[#1F3D5A]', 'text-white', 'shadow-md', 'active');
                    
                    const filterValue = btn.getAttribute('data-filter');
                    
                    portfolioCards.forEach(card => {
                        if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                            card.style.display = 'block';
                            setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'scale(1)'; }, 50);
                        } else {
                            card.style.opacity = '0';
                            card.style.transform = 'scale(0.95)';
                            setTimeout(() => { card.style.display = 'none'; }, 300);
                        }
                    });
                });
            });
        });
    </script>
    """
    
    if "Portfolio Filter Script" not in content:
        content = content.replace('</body>', filter_script + '\n</body>')
        
    with open(file_path, 'w') as f:
        f.write(content)

update_portfolio_index()
print("Portfolio filtering and title updated!")
