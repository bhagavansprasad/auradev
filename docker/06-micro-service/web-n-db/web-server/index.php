<!DOCTYPE html>
<html>
    <head>
		<title>Aura: Welcome to customized nginx!</title>
			<style>
    			body {
        			width: 35em;
        			margin: 0 auto;
        			font-family: Tahoma, Verdana, Arial, sans-serif;
    			}
			</style>
	</head>

    <body>
		<h1>Aura: Curstomized nginx!</h1>
		<p>If you see this page, the nginx web server is successfully installed and working</p>
        <ul>
            <?php
            #$json = file_get_contents('http://127.0.0.1:81/');
            $json = file_get_contents('http://172.17.0.2/');
            $obj = json_decode($json);
            $products = $obj->products;
            foreach ($products as $product) {
                echo "<li>$product</li>";
            }
            ?>
        </ul>
    </body>
</html>
