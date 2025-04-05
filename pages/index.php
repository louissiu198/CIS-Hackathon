<?php
require 'navbar.php';







?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Personal Dashboard</title>
  <link rel="stylesheet" href="/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="glow-effect.js"></script>
</head>
<body>
    <!-- Navigation -->
    <?php create_navbar(0, 'Stamina'); ?>

    <!-- Hero Section - Redesigned with grid layout -->
    <section class="container mb-8">
        <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary p-6 mb-8">
            <div class="grid grid-cols-2 gap-6">
              <div>
                <!-- Welcome Column -->
                <div class="grid grid-cols-1 md:flex md:flex-row md:justify-between">
                    <div>
                      <h2 class="text-2xl mb-2">Hello!</h2>
                      <p class="text-sm text-muted mb-4">abc</p>
                    </div>
                    <div class="flex items-center mb-4">
                        <div>
                            <p class="mb-1"><?php echo date('l, F j, Y'); ?>&nbsp;&nbsp;<span class="badge badge-primary">Today</span></p>
                            <p class="text-md"></p>
                        </div>
                    </div>
                </div>
                
                <!-- New Suggestions Column -->
                <div class="border-l pl-6">
                    <div class="alert alert-warning">
                        <i class="fas fa-lightbulb text-warning mr-2"></i>
                        <span>good</span><br>
                        <button class="btn btn-sm btn-outline btn-warning mt-2">Continue Studying</button>
                    </div>

                    <h3 class="text-xl mb-3"><i class="fas fa-lightbulb text-warning mr-2"></i>&nbsp;&nbsp;Suggestions</h3>
                    <p class="text-sm text-muted mb-3">Things you might want to do right now:</p>
                    
                    <ul class="space-y-2 mb-4">

                        <li class="flex items-center">
                            <i class="fas fa-check-circle text-success mr-2"></i>&nbsp;&nbsp;
                            <span>Complete your daily task list</span>
                        </li>
                        <li class="flex items-center">
                            <i class="fas fa-book text-primary mr-2"></i>&nbsp;&nbsp;
                            <span>Review today's study material</span>
                        </li>
                        <li class="flex items-center">
                            <i class="fas fa-calendar-check text-warning mr-2"></i>&nbsp;&nbsp;
                            <span>Check upcoming deadlines</span>
                        </li>
                        <li class="flex items-center">
                            <i class="fas fa-chart-line text-info mr-2"></i>&nbsp;&nbsp;
                            <span><?=$message?></span>
                        </li>
                    </ul>
                    
                    <a href="#" class="text-sm text-primary hover:underline">Customize suggestions <i class="fas fa-cog ml-1"></i></a>
                </div>
                
              </div>
              <div>
                  G
              </div>
            </div>
        </div>
    </section>

    <!-- Quick Access Section -->
    <section id="quick-access" class="container mb-8">
        <div class="card-header">
            <h3>Quick Access</h3>
        </div>
        <div class="grid grid-cols-4">
            <a href="#" class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary text-center">
                <i class="fas fa-tasks text-primary text-2xl mb-2"></i>
                <h4>Tasks</h4>
            </a>
            <a href="/productivity/schedule/index.php" class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary text-center">
                <i class="fas fa-calendar-alt text-primary text-2xl mb-2"></i>
                <h4>Schedule</h4>
            </a>
            <a href="/academic/knowledge/" class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary text-center">
                <i class="fas fa-book text-primary text-2xl mb-2"></i>
                <h4>Revision Notes</h4>
            </a>
            <a href="#" class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary text-center">
                <i class="fas fa-bookmark text-primary text-2xl mb-2"></i>
                <h4>Bookmarks</h4>
            </a>
        </div>
    </section>

    <!-- Main Sections -->
    <section id="productivity" class="container mb-8">
        <div class="card-header">
            <h3>Productivity Tools</h3>
        </div>
        <div class="grid grid-cols-3 mb-4">
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-list-check text-primary mr-2"></i> &nbsp;Task Management</h4>
                <p class="text-muted mb-4">Organize and track your daily tasks and projects</p>
                <a href="#" class="btn btn-outline btn-sm">Open</a>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-chart-line text-primary mr-2"></i> &nbsp;Progress Tracking</h4>
                <p class="text-muted mb-4">Monitor progress on your personal goals</p>
                <a href="#" class="btn btn-outline btn-sm">Open</a>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-calendar-week text-primary mr-2"></i> &nbsp;Schedule</h4>
                <p class="text-muted mb-4">View and manage your weekly timetable</p>
                <a href="/productivity/schedule/index.php" class="btn btn-outline btn-sm">Open</a>
            </div>
        </div>
    </section>

    <section id="academic" class="container mb-8">
        <div class="card-header">
            <h3>Academic Resources</h3>
        </div>
        <div class="grid grid-cols-3 mb-4">
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-graduation-cap text-primary mr-2"></i> &nbsp;Knowledge Organizers</h4>
                <p class="text-muted mb-4">Quick subject revision materials and notes</p>
                <a href="/academic/knowledge/" class="btn btn-outline btn-sm">Open</a>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-clock text-primary mr-2"></i> &nbsp;Study Planner</h4>
                <p class="text-muted mb-4">Plan and organize your study sessions</p>
                <a href="#" class="btn btn-outline btn-sm">Open</a>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-pen-to-square text-primary mr-2"></i> &nbsp;Note Templates</h4>
                <p class="text-muted mb-4">Templates for effective note-taking</p>
                <a href="#" class="btn btn-outline btn-sm">Open</a>
            </div>
        </div>
    </section>

    <section id="utilities" class="container mb-8">
        <div class="card-header">
            <h3>Utilities</h3>
        </div>
        <div class="grid grid-cols-3 mb-4">
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-code text-primary mr-2"></i> &nbsp;Helper Scripts</h4>
                <p class="text-muted mb-4">Scripts for automating common tasks</p>
                <a href="#" class="btn btn-outline btn-sm">Open</a>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-book-open text-primary mr-2"></i> &nbsp;References</h4>
                <p class="text-muted mb-4">Important reference materials and guides</p>
                <a href="#" class="btn btn-outline btn-sm">Open</a>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4><i class="fas fa-link text-primary mr-2"></i> &nbsp;External Resources</h4>
                <p class="text-muted mb-4">Links to useful external tools and websites</p>
                <a href="#" class="btn btn-outline btn-sm">Open</a>
            </div>
        </div>
    </section>

    <!-- Recent Activity -->
    <section class="container mb-8">
      <div class="card no-hover-transform">
        <?php include 'dev/activities/widget.php'; ?>
      </div>
    </section>

    <!-- Status Summary -->
    <section class="container mb-8">
        <div class="grid grid-cols-3">
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4 class="mb-2">Task Progress</h4>
                <div class="progress mb-2">
                    <div class="progress-bar" style="width: 65%;"></div>
                </div>
                <p class="text-sm text-muted">65% of weekly tasks completed</p>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4 class="mb-2">Study Goals</h4>
                <div class="progress mb-2">
                    <div class="progress-bar" style="width: 40%; background-color: var(--color-warning);"></div>
                </div>
                <p class="text-sm text-muted">40% of study goals achieved</p>
            </div>
            <div class="card cursor-glow-alt cursor-glow-alt-large-weak glow-primary">
                <h4 class="mb-2">Project Status</h4>
                <div class="progress mb-2">
                    <div class="progress-bar" style="width: 80%; background-color: var(--color-success);"></div>
                </div>
                <p class="text-sm text-muted">80% of current project completed</p>
            </div>
        </div>
    </section>


    <script>
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
        }
    </script>
</body>
</html>