// Initialize Lucide Icons
if (typeof lucide !== 'undefined') lucide.createIcons();

// Navbar Scroll Logic
const navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('nav-scrolled');
        } else {
            navbar.classList.remove('nav-scrolled');
        }
    });
}

// Mobile Menu Logic
const mobileMenu = document.getElementById('mobile-menu');
const openBtn = document.getElementById('mobile-menu-open');
const closeBtn = document.getElementById('mobile-menu-close');

if (mobileMenu && openBtn && closeBtn) {
    openBtn.addEventListener('click', () => {
        mobileMenu.style.transform = 'translateX(0)';
    });

    closeBtn.addEventListener('click', () => {
        mobileMenu.style.transform = 'translateX(100%)';
    });
}

// Form Submission Logic
const leadForm = document.getElementById('lead-form');
if (leadForm) {
    leadForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const emailInput = leadForm.querySelector('input[type="email"]');
        const email = emailInput ? emailInput.value : '';

        // Simple professional email validation (no generic providers for "Work Email")
        const genericProviders = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'];
        const domain = email.includes('@') ? email.split('@')[1] : '';

        if (genericProviders.includes(domain)) {
            showFormFeedback('Please provide a professional work email.', 'error');
            return;
        }

        const submitBtn = leadForm.querySelector('button[type="submit"]');
        const originalText = submitBtn ? submitBtn.innerText : 'Submit';

        // Visual feedback on button
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerText = 'Sending...';
            submitBtn.classList.add('opacity-70', 'cursor-not-allowed');
        }

        // Simulate API call
        setTimeout(() => {
            showFormFeedback('Consultation request sent! We will contact you shortly.', 'success');
            leadForm.reset();
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerText = originalText;
                submitBtn.classList.remove('opacity-70', 'cursor-not-allowed');
            }
        }, 1500);
    });
}

function showFormFeedback(message, type) {
    const feedbackDiv = document.createElement('div');
    feedbackDiv.className = `fixed bottom-8 right-8 px-6 py-3 rounded-2xl text-white font-bold shadow-xl transition-all transform translate-y-20 opacity-0 z-[100] ${
        type === 'success' ? 'bg-[#2F6F73]' : 'bg-red-500'
    }`;
    feedbackDiv.innerText = message;
    document.body.appendChild(feedbackDiv);

    // Animate in
    requestAnimationFrame(() => {
        feedbackDiv.classList.remove('translate-y-20', 'opacity-0');
        feedbackDiv.classList.add('translate-y-0', 'opacity-100');
    });

    // Remove after 4 seconds
    setTimeout(() => {
        feedbackDiv.classList.add('translate-y-20', 'opacity-0');
        setTimeout(() => feedbackDiv.remove(), 300);
    }, 4000);
}

// --- Carousel pause registry (keyed by element id) ---
const _carouselPause = {};

// --- Global Scroll Helper for Arrows ---
window.scrollCarousel = function(id, direction) {
    const carousel = document.getElementById(id);
    if (!carousel) return;

    // Pause auto-scroll for 1.5 s so arrow scroll can complete
    _carouselPause[id] = true;
    clearTimeout(carousel._arrowTimer);
    carousel._arrowTimer = setTimeout(() => { _carouselPause[id] = false; }, 1500);

    const cardWidth = carousel.querySelector(':scope > div')?.offsetWidth || carousel.clientWidth * 0.30;
    const gap = 24; // gap-6 = 1.5rem = 24px
    carousel.scrollBy({ left: direction * (cardWidth + gap), behavior: 'smooth' });
}

/** Seamless infinite loop: duplicate track is exactly half of scrollWidth */
function normalizeSeamlessScroll(carousel) {
    if (!carousel.classList.contains('carousel-seamless')) return;
    const total = carousel.scrollWidth;
    if (total < 2) return;
    const loopWidth = total / 2;
    if (loopWidth < 1) return;
    if (carousel.scrollLeft >= loopWidth) {
        carousel.scrollLeft -= loopWidth;
    }
}

// Disable image dragging inside carousels
document.querySelectorAll('#testimonial-carousel img, #portfolio-carousel img, #industry-carousel img').forEach((img) => {
    img.setAttribute('draggable', 'false');
    img.classList.add('select-none');
});

// Arrow buttons (avoid inline onclick + Lucide dependency)
const industryPrev = document.getElementById('industry-carousel-prev');
const industryNext = document.getElementById('industry-carousel-next');
if (industryPrev) industryPrev.addEventListener('click', () => window.scrollCarousel('industry-carousel', -1));
if (industryNext) industryNext.addEventListener('click', () => window.scrollCarousel('industry-carousel', 1));

const portfolioPrev = document.getElementById('portfolio-carousel-prev');
const portfolioNext = document.getElementById('portfolio-carousel-next');
if (portfolioPrev) portfolioPrev.addEventListener('click', () => window.scrollCarousel('portfolio-carousel', -1));
if (portfolioNext) portfolioNext.addEventListener('click', () => window.scrollCarousel('portfolio-carousel', 1));

const testimonialPrev = document.getElementById('testimonial-carousel-prev');
const testimonialNext = document.getElementById('testimonial-carousel-next');
if (testimonialPrev) testimonialPrev.addEventListener('click', () => window.scrollCarousel('testimonial-carousel', -1));
if (testimonialNext) testimonialNext.addEventListener('click', () => window.scrollCarousel('testimonial-carousel', 1));

// --- Carousel Logic (Pointer drag + Auto) ---
document.querySelectorAll('.carousel-container').forEach((carousel) => {
    const id = carousel.id;
    if (id) _carouselPause[id] = false;

    let isPointerDown = false;
    let dragStartX = 0;
    let dragStartScrollLeft = 0;
    let autoScrollSpeed = 0.65;
    let isHovered = false;
    const hoverPausesAutoplay = !carousel.classList.contains('carousel-no-hover-pause');

    if (carousel.classList.contains('carousel-seamless')) {
        carousel.addEventListener('scroll', () => normalizeSeamlessScroll(carousel));
    }

    function endDrag(e) {
        if (!isPointerDown) return;
        isPointerDown = false;
        carousel.classList.remove('active', 'is-dragging');
        try {
            if (e && e.pointerId != null) carousel.releasePointerCapture(e.pointerId);
        } catch (_) { /* ignore */ }
    }

    carousel.addEventListener('pointerdown', (e) => {
        if (e.pointerType === 'mouse' && e.button !== 0) return;
        isPointerDown = true;
        dragStartX = e.clientX;
        dragStartScrollLeft = carousel.scrollLeft;
        carousel.classList.add('active', 'is-dragging');
    });

    carousel.addEventListener('pointermove', (e) => {
        if (!isPointerDown) return;
        
        // Capture pointer only when actually dragging to allow clicks to pass through
        if (!carousel.hasPointerCapture(e.pointerId)) {
            try {
                carousel.setPointerCapture(e.pointerId);
            } catch (_) { /* ignore */ }
        }
        
        e.preventDefault();
        const dx = e.clientX - dragStartX;
        carousel.scrollLeft = dragStartScrollLeft - dx;
    }, { passive: false });

    carousel.addEventListener('pointerup', endDrag);
    carousel.addEventListener('pointercancel', endDrag);
    carousel.addEventListener('lostpointercapture', () => {
        isPointerDown = false;
        carousel.classList.remove('active', 'is-dragging');
    });

    if (hoverPausesAutoplay) {
        carousel.addEventListener('mouseenter', () => { isHovered = true; });
        carousel.addEventListener('mouseleave', () => {
            isHovered = false;
        });
    }

    // Infinite auto-scroll loop via rAF
    function scrollLoop() {
        const paused = id ? _carouselPause[id] : false;
        const hoverBlocks = hoverPausesAutoplay && isHovered;
        if (!isPointerDown && !hoverBlocks && !paused) {
            carousel.scrollLeft += autoScrollSpeed;
            if (carousel.classList.contains('carousel-seamless')) {
                normalizeSeamlessScroll(carousel);
            } else {
                const maxScroll = carousel.scrollWidth - carousel.clientWidth;
                if (carousel.scrollLeft >= maxScroll - 2) {
                    carousel.scrollLeft = 2;
                }
            }
        }
        requestAnimationFrame(scrollLoop);
    }
    requestAnimationFrame(scrollLoop);
});

// Tab Switching logic
window.switchTab = function(tabId) {
    // Update buttons
    const tabs = ['fixed', 'hire', 'agile'];
    tabs.forEach(t => {
        const btn = document.getElementById('btn-process-' + t);
        const timeline = document.getElementById('timeline-' + t);
        if(!btn || !timeline) return;

        const icon = btn.querySelector('svg') || btn.querySelector('i');
        
        if (t === tabId) {
            btn.className = "w-full text-left px-6 py-4 rounded-2xl bg-[#1F3D5A] text-white font-extrabold flex justify-between items-center transition-all shadow-md group border border-[#1F3D5A]";
            if (icon) icon.setAttribute('class', "w-5 h-5 text-white/70 group-hover:text-white transition-colors lucide lucide-chevron-right");
            timeline.classList.remove('hidden');
        } else {
            btn.className = "w-full text-left px-6 py-4 rounded-2xl bg-white border border-[#EDEDED] text-[#4A4A4A] font-extrabold flex justify-between items-center hover:border-[#1F3D5A] hover:text-[#1F3D5A] transition-all group";
            if (icon) icon.setAttribute('class', "w-5 h-5 text-[#4A4A4A]/40 group-hover:text-[#1F3D5A] transition-colors lucide lucide-chevron-right");
            timeline.classList.add('hidden');
        }
    });
    
    // Update description
    const descEl = document.getElementById('process-description');
    if (descEl) {
        // fade out
        descEl.style.opacity = 0;
        setTimeout(() => {
            if (tabId === 'fixed') {
                descEl.innerText = "We deliver a structured process for seamless project execution. From understanding your requirements to delivering the final solution, we ensure proactive technology services based on your business needs.";
            } else if (tabId === 'hire') {
                descEl.innerText = "Scale your team with top-tier talent. Our streamlined onboarding process ensures you get the right expertise seamlessly integrated into your workflows, giving you full control and visibility.";
            } else if (tabId === 'agile') {
                descEl.innerText = "Embrace flexibility and continuous improvement. Our agile methodology ensures iterative delivery, constant feedback loops, and rapid adaptation to your evolving business needs.";
            }
            // fade in
            descEl.style.opacity = 1;
        }, 150);
    }
}

// FAQ Accordion Logic
document.addEventListener('DOMContentLoaded', () => {
    // Specifically target accordion items inside the FAQ panels
    const items = document.querySelectorAll('.faq-content-pane .group.cursor-pointer');
    items.forEach(item => {
        item.addEventListener('click', () => {
            // Find the paragraph that is meant to be hidden/shown
            const p = item.querySelector('p');
            const iconDiv = item.querySelector('.w-8.h-8');
            
            if (p) {
                const isClosed = p.classList.contains('hidden') || p.style.display === 'none' || p.style.maxHeight === '0px';
                
                if (isClosed) {
                    // Open
                    p.classList.remove('hidden');
                    p.style.display = 'block';
                    p.style.overflow = 'hidden';
                    
                    // Add margin top if missing, so we get correct height
                    if (!p.classList.contains('mt-4')) {
                        p.classList.add('mt-4');
                    }
                    
                    const scrollHeight = p.scrollHeight;
                    p.style.maxHeight = '0px';
                    p.style.opacity = '0';
                    p.style.transition = 'max-height 0.4s ease, opacity 0.4s ease, margin-top 0.4s ease';
                    
                    // Trigger reflow
                    p.offsetHeight;
                    
                    p.style.maxHeight = scrollHeight + 'px';
                    p.style.opacity = '1';
                    
                    item.classList.add('border-[#2F6F73]', 'shadow-md');
                    item.classList.remove('border-[#EDEDED]');
                    if (iconDiv) {
                        iconDiv.innerHTML = '<i data-lucide="minus" class="w-4 h-4"></i>';
                        iconDiv.classList.add('bg-[#2F6F73]', 'text-white');
                        iconDiv.classList.remove('bg-[#FAFAFA]', 'text-[#1F3D5A]', 'group-hover:bg-[#2F6F73]', 'group-hover:text-white');
                    }
                    
                    // Clean up max-height after transition so resizing works
                    setTimeout(() => {
                        if (p.style.maxHeight !== '0px') {
                            p.style.maxHeight = 'none';
                        }
                    }, 400);
                    
                } else {
                    // Close
                    p.style.maxHeight = p.scrollHeight + 'px';
                    p.style.overflow = 'hidden';
                    p.style.transition = 'max-height 0.4s ease, opacity 0.4s ease, margin-top 0.4s ease';
                    
                    // Trigger reflow
                    p.offsetHeight;
                    
                    p.style.maxHeight = '0px';
                    p.style.opacity = '0';
                    p.classList.remove('mt-4');
                    
                    item.classList.remove('border-[#2F6F73]', 'shadow-md');
                    item.classList.add('border-[#EDEDED]');
                    if (iconDiv) {
                        iconDiv.innerHTML = '<i data-lucide="plus" class="w-4 h-4"></i>';
                        iconDiv.classList.remove('bg-[#2F6F73]', 'text-white');
                        iconDiv.classList.add('bg-[#FAFAFA]', 'text-[#1F3D5A]', 'group-hover:bg-[#2F6F73]', 'group-hover:text-white');
                    }
                    
                    setTimeout(() => {
                        if (p.style.maxHeight === '0px') {
                            p.style.display = 'none';
                            p.classList.add('hidden');
                        }
                    }, 400);
                }
            }
            if (window.lucide && iconDiv) {
                lucide.createIcons({ root: iconDiv });
            }
        });
        
        // Initialize state for already hidden or shown items
        const p = item.querySelector('p');
        if (p) {
            if (p.classList.contains('hidden')) {
                p.style.display = 'none';
                p.style.maxHeight = '0px';
                p.style.opacity = '0';
                p.style.overflow = 'hidden';
                p.classList.remove('mt-4');
            } else {
                p.style.display = 'block';
                p.style.maxHeight = 'none';
                p.style.opacity = '1';
                p.style.overflow = 'hidden';
                if (!p.classList.contains('mt-4')) {
                    p.classList.add('mt-4');
                }
            }
        }
    });
});

// Testimonial Modal Logic
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('testimonial-modal');
    if (!modal) return;
    
    const modalContent = modal.querySelector('div');
    const closeBtn = document.getElementById('close-modal');
    
    const mTagline = document.getElementById('modal-tagline');
    const mImage = document.getElementById('modal-image');
    const mName = document.getElementById('modal-name');
    const mRole = document.getElementById('modal-role');
    const mLocation = document.getElementById('modal-location');
    const mReview = document.getElementById('modal-review');
    
    document.querySelectorAll('.testimonial-card').forEach(card => {
        card.addEventListener('click', () => {
            if (mTagline) mTagline.textContent = card.getAttribute('data-tagline') || '';
            if (mImage) mImage.src = card.getAttribute('data-image') || '';
            if (mName) mName.textContent = card.getAttribute('data-name') || '';
            if (mRole) mRole.textContent = card.getAttribute('data-role') || '';
            if (mLocation) mLocation.textContent = card.getAttribute('data-location') || '';
            if (mReview) mReview.textContent = card.getAttribute('data-full-review') || '';
            
            // Show modal
            modal.classList.remove('hidden');
            // Small delay to allow display:block to apply before animating opacity
            setTimeout(() => {
                modal.classList.remove('opacity-0');
                modalContent.classList.remove('scale-95');
            }, 10);
            
            // Re-render lucide icons
            const starsContainer = document.getElementById('modal-stars');
            if(starsContainer && window.lucide) {
                starsContainer.innerHTML = `
                    <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                `;
                lucide.createIcons({ root: starsContainer });
            }
        });
    });
    
    function closeModal() {
        modal.classList.add('opacity-0');
        modalContent.classList.add('scale-95');
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 300);
    }
    
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
});


// Image Gallery Modal Logic
document.addEventListener("DOMContentLoaded", () => {
    const galleryGrid = document.getElementById("joy-gallery-grid");
    const galleryModal = document.getElementById("gallery-modal");
    if (!galleryGrid || !galleryModal) return;
    
    const modalImg = document.getElementById("gallery-modal-img");
    const closeBtn = document.getElementById("close-gallery");
    
    // Add click event to all images in the grid
    const images = galleryGrid.querySelectorAll("img");
    images.forEach(img => {
        img.addEventListener("click", () => {
            modalImg.src = img.src;
            modalImg.alt = img.alt;
            
            galleryModal.classList.remove("hidden");
            setTimeout(() => {
                galleryModal.classList.remove("opacity-0");
                modalImg.classList.remove("scale-95");
            }, 10);
        });
    });
    
    function closeGallery() {
        galleryModal.classList.add("opacity-0");
        modalImg.classList.add("scale-95");
        setTimeout(() => {
            galleryModal.classList.add("hidden");
        }, 300);
    }
    
    if (closeBtn) {
        closeBtn.addEventListener("click", closeGallery);
    }
    
    galleryModal.addEventListener("click", (e) => {
        if (e.target === galleryModal) closeGallery();
    });
    
    // Close on escape key
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && !galleryModal.classList.contains("hidden")) {
            closeGallery();
        }
    });
});

// KPI Numbering Counter Animation
document.addEventListener("DOMContentLoaded", () => {
    const potentialKpis = document.querySelectorAll('p.text-5xl.font-black, h2.text-5xl.font-black, p.text-4xl.font-black, h2.text-4xl.font-black');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const targetText = el.getAttribute('data-target');
                const target = parseFloat(targetText.replace(/[^0-9.]/g, ''));
                const suffix = targetText.replace(/[0-9.]/g, '');
                
                let start = 0;
                const duration = 2000;
                let startTime = null;

                function animation(currentTime) {
                    if (startTime === null) startTime = currentTime;
                    const timeElapsed = currentTime - startTime;
                    const progress = Math.min(timeElapsed / duration, 1);
                    
                    const easeOut = 1 - Math.pow(1 - progress, 3);
                    const currentVal = start + (target - start) * easeOut;
                    
                    if (target % 1 === 0) {
                        el.innerText = Math.round(currentVal) + suffix;
                    } else {
                        el.innerText = currentVal.toFixed(1) + suffix;
                    }

                    if (progress < 1) {
                        requestAnimationFrame(animation);
                    } else {
                        el.innerText = targetText;
                    }
                }
                
                requestAnimationFrame(animation);
                observer.unobserve(el);
            }
        });
    }, { threshold: 0.1 });

    potentialKpis.forEach(el => {
        const text = el.innerText.trim();
        if (/^[0-9]+(\.[0-9]+)?[+%]?$/.test(text)) {
            el.setAttribute('data-target', text);
            el.innerText = '0' + text.replace(/[0-9.]/g, '');
            observer.observe(el);
        }
    });
});
