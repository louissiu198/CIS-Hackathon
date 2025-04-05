<?php

function create_navbar(int $selected, // Index of the selected item in the array
                       string $title = 'Personal Dashboard', 
                       string $currentUsername = '', 
                       bool $dev = false, 
                       bool $welcome_page = false, 
                       bool $logged_in = true) {

  $nav_items = [
    'Home' => '/',
    'Productivity' => '/productivity',
    'Academic' => '/academic',
    'Utilities' => '/utilities'
  ];
  
  echo '<header class="container">';
  echo '<nav class="nav">';
  
  // Mobile toggle button (only visible on small screens)
  echo '<div class="mobile-toggle-container">';
  echo '<button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Toggle menu">';
  echo '<i class="fas fa-bars"></i>';
  echo '</button>';
  
  // Title is always visible
  echo "<h1 class='text-xl font-bold nav-item'>";
  if ($dev) {
    echo "<span class='text-sm text-muted font-bold'>DEV</span>&nbsp;/&nbsp;";
  }
  echo htmlspecialchars($title) . "&nbsp;&nbsp;&nbsp;&nbsp;</h1>";
  echo '</div>';

  // Collapsible content
  echo '<div class="nav-content" id="navbar-content">';
  
  if ($dev) {
    echo '<div class="flex justify-between items-center collapsible-item">';
    echo '<ul class="nav-list">';
    echo '<li class="nav-item"><span class="text-sm text-muted btn-sm">You are on a Developer page!</span></li>';
    echo '</ul>';
    echo '</div>';
  } else if ($welcome_page) {
    $welcome_nav_items = [
      'Home' => '/',
      'About' => '/about.php',
      'Contact Us' => '/contact.php'
    ];

    echo '<div class="flex justify-between items-center collapsible-item">';
    echo '<ul class="nav-list">';
    foreach ($welcome_nav_items as $item => $url) {
        $active = $selected === array_search($item, array_keys($welcome_nav_items)) ? 'active' : '';
        echo "<li class='nav-item'><a href='$url' class='$active'>$item</a></li>";
    }
    echo '</ul>';
    echo '</div>';

  
  } else {
    echo '<div class="flex justify-between items-center collapsible-item">';
    echo '<ul class="nav-list">';
    foreach ($nav_items as $item => $url) {
        $active = $selected === array_search($item, array_keys($nav_items)) ? 'active' : '';
        echo "<li class='nav-item'><a href='$url' class='$active'>$item</a></li>";
    }
    echo '</ul>';
    echo '</div>';
  }

  echo '<br class="mobile-only-line-break">';
  
  echo '<div class="flex justify-between items-center collapsible-item">';
  echo '<ul class="nav-list">';

  
  

  if ($logged_in) {
    echo '<li class="nav-item">';
    echo '<a href="/settings/index.php" class="btn btn-sm btn-secondary">';
    echo '<i class="fas fa-cog"></i>&nbsp;Settings';
    echo '</a>';
    echo '</li>';
    echo '<li class="nav-item">';
    echo '</a>'; 
    echo '<a href="/account.php" class="btn btn-sm btn-secondary">';
    echo '<i class="fas fa-user"></i>&nbsp;Account';
    echo '</a>';
    echo '</li>';
    echo '<li class="nav-item">';
    echo '<a href="/logout.php" class="btn btn-sm btn-outline"><i class="fas fa-sign-out-alt"></i>&nbsp;Logout</a>';
    echo '</div></li>';
  } else {
    echo '<li class="nav-item">';
    echo '<a href="/login.php" class="btn btn-sm btn-outline"><i class="fas fa-sign-in-alt"></i>&nbsp;Login</a>';
    echo '</li>';
    echo '<li class="nav-item">';
    echo '<a href="/register.php" class="btn btn-sm btn-primary"><i class="fas fa-user-plus"></i>&nbsp;Register</a>';
    echo '</li>';
  }


  echo '</ul>';
  
  echo '</div>'; // Close collapsible content
  echo '</nav>';
  echo '</header>';

  // Add JavaScript for menu toggle
  echo '<script>
    document.getElementById("mobile-menu-btn").addEventListener("click", function() {
      document.getElementById("navbar-content").classList.toggle("show");
    });
  </script>';

  // Add CSS for responsive behavior
  echo '<style>
    @media (max-width: 768px) {
      .mobile-toggle-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
      }
      .mobile-menu-btn {
        display: block;
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        order: -1;
      }
      .nav-content {
        overflow: hidden;
        max-height: 0;
        width: 100%;
        flex-direction: column;
        opacity: 0;
        transition: max-height 0.2s ease-in-out, opacity 0.1s ease-in-out;
      }
      .nav-content.show {
        max-height: 300px; /* Adjust based on your menu height */
        opacity: 1;
      }
      .collapsible-item {
        width: 100%;
        margin-top: 2px;
      }
      .nav {
        flex-direction: column;
        align-items: flex-start;
      }
      .nav-right {
        margin-top: 2px;
        flex-direction: column;
        align-items: flex-start;
      }
      .nav-list {
        flex-direction: row;
        flex-wrap: wrap;
        width: 100%;
      }
      .nav-item {
        margin: 2px 0;
      }
      .btn-sm {
        margin-top: 1px;
        margin-bottom: 1px;
      }
      .mobile-only-line-break {
        display: block;
      }
    }
    @media (min-width: 769px) {
      .mobile-toggle-container {
        width: auto;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        flex-shrink: 0;
        margin-right: 20px;
        display: flex;
        align-items: baseline;
      }
      .mobile-menu-btn {
        display: none;
      }
      .nav-content {
        display: flex;
        justify-content: space-between;
        width: 100%;
        max-height: none;
        opacity: 1;
        align-items: baseline;
      }
      .mobile-only-line-break {
        display: none;
      }
      .nav {
        display: flex;
        flex-direction: row;
        align-items: baseline;
      }
      .nav-list {
        display: flex;
        align-items: baseline;
      }
      .collapsible-item {
        display: flex;
        align-items: baseline;
      }
    }
    /* Title-specific rules for all viewports */
    h1.text-xl.font-bold.nav-item {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 100%;
      margin-bottom: 0;
      line-height: normal;
    }
    .nav-item {
      display: flex;
      align-items: baseline;
    }
  </style>';
}

?>