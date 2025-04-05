document.addEventListener('DOMContentLoaded', () => {
    const glowCards = document.querySelectorAll('.cursor-glow-alt');
    
    glowCards.forEach(card => {
        // Initialize default position (center)
        card.style.setProperty('--mouse-x', '50%');
        card.style.setProperty('--mouse-y', '50%');
        
        card.addEventListener('mousemove', (e) => {
            // Get position relative to the card
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; // x position within the element
            const y = e.clientY - rect.top;  // y position within the element
            
            // Calculate the position in percentage
            const xPercent = (x / rect.width) * 100;
            const yPercent = (y / rect.height) * 100;
            
            // Update CSS variables
            card.style.setProperty('--mouse-x', `${xPercent}%`);
            card.style.setProperty('--mouse-y', `${yPercent}%`);
        });
        
        // Reset when mouse leaves
        card.addEventListener('mouseleave', () => {
            card.style.setProperty('--mouse-x', '50%');
            card.style.setProperty('--mouse-y', '50%');
        });
    });
});