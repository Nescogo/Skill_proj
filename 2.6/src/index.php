<html lang="en">
	<head>
		<title>Boardgame from BGG</title>
		<link rel="stylesheet" href="style.css" type="text/css" />
	</head>
	<body>
		<h1>Boardgames</h1>
		<table>
			<tr>
				<th>game</th>
				<th>g_type</th>
				<th>year</th>
			</tr>
			<?php
				$mysqli = new mysqli ("db","user","password","boardg");
				$result = $mysqli->query("SELECT * FROM  bg");
				foreach ($result as $row) {
					echo "
					<tr> 
						<td>{$row['game']}</td>
						<td>{$row['g_type']}</td>
						<td>{$row['year']}</td>
					</tr>";} ?>
			</table>
			<?php
				phpinfo(); ?>
	</body>
</html>
