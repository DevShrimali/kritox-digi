// Initialize Lucide Icons
lucide.createIcons();

// Navbar Scroll Logic
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
        navbar.classList.add('nav-scrolled');
    } else {
        navbar.classList.remove('nav-scrolled');
    }
});

// Mobile Menu Logic
const mobileMenu = document.getElementById('mobile-menu');
const openBtn = document.getElementById('mobile-menu-open');
const closeBtn = document.getElementById('mobile-menu-close');

openBtn.addEventListener('click', () => {
    mobileMenu.style.transform = 'translateX(0)';
});

closeBtn.addEventListener('click', () => {
    mobileMenu.style.transform = 'translateX(100%)';
});

// Form Submission Logic
const leadForm = document.getElementById('lead-form');
leadForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const emailInput = leadForm.querySelector('input[type="email"]');
    const email = emailInput.value;

    // Simple professional email validation (no generic providers for "Work Email")
    const genericProviders = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'];
    const domain = email.split('@')[1];

    if (genericProviders.includes(domain)) {
        showFormFeedback('Please provide a professional work email.', 'error');
        return;
    }

    const submitBtn = leadForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerText;

    // Visual feedback on button
    submitBtn.disabled = true;
    submitBtn.innerText = 'Sending...';
    submitBtn.classList.add('opacity-70', 'cursor-not-allowed');

    // Simulate API call
    setTimeout(() => {
        showFormFeedback('Consultation request sent! We will contact you shortly.', 'success');
        leadForm.reset();
        submitBtn.disabled = false;
        submitBtn.innerText = originalText;
        submitBtn.classList.remove('opacity-70', 'cursor-not-allowed');
    }, 1500);
});

function showFormFeedback(message, type) {
    const feedbackDiv = document.createElement('div');
    feedbackDiv.className = `fixed bottom-8 right-8 px-6 py-3 rounded-2xl text-white font-bold shadow-xl transition-all transform translate-y-20 opacity-0 ${
        type === 'success' ? 'bg-brand-base' : 'bg-red-500'
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
