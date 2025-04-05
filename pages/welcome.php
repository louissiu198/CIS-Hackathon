<?php

// welcome.php

include 'navbar.php'; include 'dev/glow-effect/colors.php';

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stamina - Reduce Your Carbon Footprint</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="glow-effect.js"></script>
  <script src="scroll-animations.js" defer></script>
</head>
<body>
  <!-- Navbar -->
  <?php create_navbar(1, 'Stamina', '', false, true); ?>

  <!-- Hero Section -->
  <section class="section hero-section">
    <div class="container">
      <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
        <div class="text-center">
          <h1 class="text-4xl">Meet Stamina</h1>
          <p class="text-muted">Our solution to unnecessary electricity use. Simply take pictures of your room, and our AI identifies devices, providing insights on electricity consumption, carbon emissions, and costs—helping you save money and the planet.</p>
          <div class="mt-8">
            <a href="#features"><button class="btn btn-primary btn-lg scroll-cta">Discover How</button></a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Features Section -->
  <section id="features" class="section features-section bg-gradient">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <h2 class="text-3xl">Smart Features</h2>
        <p class="text-muted">Turn your smartphone into a powerful tool for sustainability</p>
      </div>
      
      <div class="grid grid-cols-3 features-grid mb-8">
        <div class="card feature-card cursor-glow-alt cursor-glow-alt-large-weak glow-crimson animate-on-scroll">
          <div class="feature-icon">
            <i class="fas fa-camera fa-2x"></i>
          </div>
          <h3>AI Device Recognition</h3>
          <p>Our advanced AI identifies electronic devices from your photos with remarkable accuracy.</p>
        </div>
        
        <div class="card feature-card cursor-glow-alt cursor-glow-alt-large-weak glow-crimson animate-on-scroll" data-delay="200">
          <div class="feature-icon">
            <i class="fas fa-bolt fa-2x"></i>
          </div>
          <h3>Energy Analysis</h3>
          <p>Get detailed breakdowns of your electricity consumption patterns and usage hotspots.</p>
        </div>
        
        <div class="card feature-card cursor-glow-alt cursor-glow-alt-large-weak glow-crimson animate-on-scroll" data-delay="400">
          <div class="feature-icon">
            <i class="fas fa-leaf fa-2x"></i>
          </div>
          <h3>Carbon Footprint</h3>
          <p>Visualize your environmental impact and track improvements over time.</p>
        </div>
      </div>

      <div class="section-header text-center animate-on-scroll">
        <h2 class="text-3xl">Save money. Save the planet.</h2>
      </div>
    </div>
  </section>

  <!-- How It Works Section -->
  <section class="section how-it-works-section">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <h2 class="text-3xl">How Stamina Works</h2>
        <p class="text-muted">Three simple steps to reduce your carbon footprint</p>
      </div>
      
      <div class="steps-container">
        <div class="step animate-on-scroll" data-animation="slide-right">
          <div class="step-number">1</div>
          <div class="step-content">
            <h3>Snap Photos</h3>
            <p>Take pictures of your room and electronic devices with your smartphone.</p>
          </div>
        </div>
        
        <div class="step animate-on-scroll" data-animation="slide-left" data-delay="200">
          <div class="step-number">2</div>
          <div class="step-content">
            <h3>Get Smart Insights</h3>
            <p>Our AI analyzes your devices, consumption patterns, and provides actionable data.</p>
          </div>
        </div>
        
        <div class="step animate-on-scroll" data-animation="slide-right" data-delay="400">
          <div class="step-number">3</div>
          <div class="step-content">
            <h3>Reduce & Save</h3>
            <p>Follow tailored recommendations to cut electricity use, costs, and carbon emissions.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Dashboard Preview Section -->
  <section class="section dashboard-preview-section bg-gradient-alt">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
      <h2 class="text-3xl">Powerful Insights Dashboard</h2>
      <p class="">Making sustainability simple and actionable.</p>
      </div>
      <div class="section-header text-center animate-on-scroll">

          
        <ul class="feature-list">
          <li class="animate-on-scroll" data-delay="100"><i class="fas fa-check"></i> Instant photo scan and analyzing</li>
          <li class="animate-on-scroll" data-delay="200"><i class="fas fa-check"></i> Cost projection and savings calculator</li>
          <li class="animate-on-scroll" data-delay="300"><i class="fas fa-check"></i> Device-specific efficiency recommendations</li>
        </ul>
      </div>
    </div>
  </section>


  <!-- Testimonials Section -->
  <section class="section testimonial-section">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <h2 class="text-3xl">What Users Say</h2>
        <p class="text-muted">Trusted by thousands of users worldwide</p>
      </div>
      
      <div class="testimonial-grid">
        <div class="testimonial-card animate-on-scroll" data-delay="100">
          <div class="quote"><i class="fas fa-quote-left"></i></div>
          <p class="testimonial-text">"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
          <div class="testimonial-author">
            <img src="https://placehold.co/100x100/2563eb/FFFFFF/png?text=A" alt="User Avatar" class="author-avatar">
            <div class="author-info">
              <h4>Alex Smith</h4>
              <p class="text-muted">Product Manager</p>
            </div>
          </div>
        </div>
        
        <div class="testimonial-card animate-on-scroll" data-delay="300">
          <div class="quote"><i class="fas fa-quote-left"></i></div>
          <p class="testimonial-text">"Lorem ipsum odor amet, consectetuer adipiscing elit. Faucibus praesent urna maximus suspendisse facilisi volutpat natoque.</p>
          <div class="testimonial-author">
            <img src="https://placehold.co/100x100/10b981/FFFFFF/png?text=S" alt="User Avatar" class="author-avatar">
            <div class="author-info">
              <h4>Sarah Smith</h4>
              <p class="text-muted">Freelance Designer</p>
            </div>
          </div>
        </div>
        
        <div class="testimonial-card animate-on-scroll" data-delay="500">
          <div class="quote"><i class="fas fa-quote-left"></i></div>
          <p class="testimonial-text">Imperdiet molestie primis purus dis odio. Faucibus molestie suspendisse maximus; ullamcorper consectetur cursus facilisi nullam rutrum.</p>
          <div class="testimonial-author">
            <img src="https://placehold.co/100x100/f59e0b/FFFFFF/png?text=M" alt="User Avatar" class="author-avatar">
            <div class="author-info">
              <h4>Michael Smith</h4>
              <p class="text-muted">Software Engineer</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

      <!-- CTA Section -->
  <section class="section cta-section" style="width: 100%;">
    <div class="container" style="width: 100%;">
      <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-purple cta-card animate-on-scroll" style="width: 100%;">
        <div class="text-center" style="width: 100%;">
          <h2 class="text-3xl">Ready to Get Started?</h2>
          <p class="mb-6">Begin your productivity journey today.</p>
          <a href="register.php"><button class="btn btn-primary btn-lg animate-on-scroll" style="z-index:6;">Register Now</button></a>
        </div>
      </div>
    </div>
  </section>

  <div class="scroll-indicator">
    <div class="scroll-progress"></div>
  </div>
</body>
</html>
