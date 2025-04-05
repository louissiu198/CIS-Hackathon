<?php

/**
 * Returns a random glow effect class
 * 
 * @return string The class name including the "glow-" prefix
 */
function getRandomGlowClass()
{
  $classes = [
    'glow-primary', 'glow-success', 'glow-warning', 'glow-error',
    'glow-purple', 'glow-orange', 'glow-teal', 'glow-pink',
    'glow-yellow', 'glow-indigo', 'glow-cyan', 'glow-gray',
    'glow-green', 'glow-black', 'glow-white', 'glow-magenta', 
    'glow-azure', 'glow-burgundy', 'glow-coral',
    'glow-crimson', 'glow-emerald', 'glow-fuchsia', 'glow-gold',
    'glow-grape', 'glow-jade', 'glow-lavender', 'glow-lime',
    'glow-maroon', 'glow-mint', 'glow-navy', 'glow-olive',
    'glow-peach', 'glow-plum', 'glow-ruby', 'glow-salmon',
    'glow-sapphire', 'glow-scarlet', 'glow-silver', 'glow-sky',
    'glow-slate', 'glow-turquoise', 'glow-violet', 'glow-rose',
    'glow-amber', 'glow-chocolate', 'glow-coffee', 'glow-aqua',
    'glow-bronze', 'glow-charcoal', 'glow-tan', 'glow-forest'
  ];
  
  return $classes[array_rand($classes)];
}