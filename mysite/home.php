
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>php</title>
</head>
<body>

<?php
$to = "krishan260692@gmail.com";
$subject = "My subject";
$txt = "Hello world!";
$headers = "From: shyamkumar260692@gmail.com" . "\r\n";

mail($to,$subject,$txt,$headers);
?>

</body>
</html>


