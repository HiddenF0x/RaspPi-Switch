<html>
<head>
	<title>Starting Strobe</title>
</head>

<!-- 
	Vairables: time, speed
	Usage example http://.../strobe.php?time=1&speed=0.5

-->

<body>

	<?php
	$time = 2;
	$speed = 1;
	$speed = $_GET["speed"];
	$time = $_GET["time"];
	echo "Process ID:";
	echo exec("sudo /usr/bin/python /var/www/html/php/Strobe.py -t $time -s $speed");
	// The value of the variable name is found
	echo "<h1>time: " . $time . "</h1>";
	echo "<h1>speed: " . $speed . "</h1>";
	?>	

</body>
</html>
	