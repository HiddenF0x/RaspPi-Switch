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
	exec('sudo /usr/bin/python /var/www/html/php/Strobe.py -t ' + $_GET["time"] + ' -s ' + $S_GET["speed"]);
	// The value of the variable name is found
	echo "<h1>Hello " . $_GET["time"] . "</h1>";
	echo "<h1>Hello " . $_GET["speed"] . "</h1>";
	?>	

</body>
</html>
	