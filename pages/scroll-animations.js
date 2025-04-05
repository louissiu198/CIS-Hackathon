
document.addEventListener('DOMContentLoaded', () => {
  // Initialize scroll animations
  initScrollAnimations();
  
  // Set up scroll progress indicator
  setupScrollProgress();
  
  // Handle smooth scroll for anchor links
  setupSmoothScroll();
  
  // Initialize parallax effects
  initParallaxEffects();
  
  // Add initial animations to visible elements
  animateVisibleElements();
});

// Configure the Intersection Observer for scroll animations
function initScrollAnimations() {
  const options = {
    root: null, // viewport
    rootMargin: '0px',
    threshold: 0.15 // 15% of the element must be visible
  };
  
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = el.dataset.delay || 0;
        const animation = el.dataset.animation || 'fade-in';
        
        // Add animation after delay
        setTimeout(() => {
          el.classList.add('animated', animation);
        }, delay);
        
        // Unobserve after animation
        observer.unobserve(el);
      }
    });
  }, options);
  
  // Observe all elements with animate-on-scroll class
  document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
  });
}

// Setup the scroll progress indicator
function setupScrollProgress() {
  const scrollIndicator = document.querySelector('.scroll-progress');
  
  if (scrollIndicator) {
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      scrollIndicator.style.width = scrolled + '%';
    });
  }
}

// Handle smooth scrolling for anchor links
function setupSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 100, // Offset for fixed header
          behavior: 'smooth'
        });
      }
    });
  });
}

// Initialize parallax effects for elements
function initParallaxEffects() {
  let ticking = false;
  const parallaxElements = document.querySelectorAll('.parallax-element');
  
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        updateParallaxElements(parallaxElements);
        ticking = false;
      });
      
      ticking = true;
    }
  });
}

// Update position of parallax elements based on scroll
function updateParallaxElements(elements) {
  const scrollY = window.scrollY;
  
  elements.forEach(el => {
    const speed = el.dataset.speed || 0.1;
    const animation = el.dataset.animation || 'parallax';
    
    if (animation === 'parallax') {
      const yPos = -(scrollY * speed);
      el.style.transform = `translateY(${yPos}px)`;
    } else if (animation === 'float') {
      // Apply floating animation controlled by scroll
      const scrollProgress = Math.min(1, Math.max(0, getElementScrollProgress(el)));
      const floatValue = Math.sin(scrollProgress * Math.PI) * 20;
      el.style.transform = `translateY(${floatValue}px)`;
    }
  });
}

// Calculate how far an element has been scrolled through viewport
function getElementScrollProgress(element) {
  const rect = element.getBoundingClientRect();
  const windowHeight = window.innerHeight;
  
  // Element is fully above the viewport
  if (rect.bottom <= 0) return 1;
  
  // Element is fully below the viewport
  if (rect.top >= windowHeight) return 0;
  
  // Element is partially visible
  const visibleHeight = Math.min(rect.bottom, windowHeight) - Math.max(rect.top, 0);
  const elementHeight = rect.height;
  
  return 1 - (visibleHeight / elementHeight);
}

// Animate elements that are initially visible without scrolling
function animateVisibleElements() {
  const heroTitle = document.querySelector('.animate-title');
  const heroSubtitle = document.querySelector('.animate-subtitle');
  const heroButton = document.querySelector('.animate-button');
  
  if (heroTitle) {
    setTimeout(() => heroTitle.classList.add('animated', 'fade-in'), 300);
  }
  
  if (heroSubtitle) {
    setTimeout(() => heroSubtitle.classList.add('animated', 'fade-in'), 600);
  }
  
  if (heroButton) {
    setTimeout(() => heroButton.classList.add('animated', 'fade-in'), 900);
  }
}