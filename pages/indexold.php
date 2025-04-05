<?php
include 'navbar.php';
?>

<!DOCTYPE html>

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CIS</title>
  <script src="glow-effect.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="icon" href="./static/icon.png" type="image/x-icon">
  <link rel="stylesheet" href="/style.css">
</head>
<body>
    <!-- Navigation -->


    <div class="icon-bar">
        <a class="active" href="/"><i class="fa fa-home"></i></a> 
        <a href="/"><i class="fa fa-search"></i></a> 
        <a href="/about"><i class="fa fa-info"></i></a>
    </div>

    <h1 style="margin-left:32px;">Why Reduce Your Carbon Footprint?</h1>

    <div style="margin-left:32px">
        <p>Reducing your carbon footprint is essential for combating climate change and protecting the environment. By minimizing greenhouse gas emissions, we can help preserve natural resources, improve air quality, and promote a sustainable future for generations to come. Every small action counts, and together we can make a significant impact.</p>
        <p>By reducing your carbon footprint, you can also save money on energy bills, improve your health by reducing pollution, and support local economies through sustainable practices. It's a win-win situation for both individuals and the planet.</p>
        <p>Join the movement towards a greener future by taking steps to reduce your carbon footprint today. Whether it's using public transportation, reducing energy consumption, or supporting renewable energy sources, every action matters.</p>
        <p>Let's work together to create a healthier planet for ourselves and future generations. Start making a difference today!</p>
    </div>

    <div>About Your Appliances</div>
    <div style="margin-left:32px">
        <p>Understanding the energy consumption of your appliances is crucial for reducing your carbon footprint. By being aware of how much energy each appliance uses, you can make informed decisions about when and how to use them. This knowledge can help you identify energy-hungry appliances and find ways to reduce their usage or replace them with more efficient models.</p>
        <p>For example, older refrigerators and air conditioners tend to consume more energy than newer, energy-efficient models. By upgrading to Energy Star-rated appliances, you can significantly reduce your energy consumption and lower your carbon footprint.</p>
        <p>Additionally, using appliances during off-peak hours can help reduce strain on the electrical grid and lower your overall energy costs. Consider using timers or smart home technology to optimize your appliance usage.</p>
        <p>By understanding your appliances' energy consumption, you can take proactive steps towards a more sustainable lifestyle and contribute to a healthier planet.</p>
    </div>

    <div class="scanner-div">
        <label id="label-div">
            <input id="file-input" type="file" accept="image/*"/>
            <i class="fa fa-camera scanner-btn" id="scanner-btn"></i>
        </label>
        <button class="scanner-btn hidden-btn" id="hidden-btn"></button>
    </div>
    <script src="./static/script.js"></script> <!-- It needs to load after the element load, might need to update on the script side-->
</body>
</html>