<?php
$db = mysqli_connect('localhost', 'root', '', 'myproject');
$name = $_POST['name'];
$email = $_POST['email'];
$contact = $_POST['contact'];
$address = $_POST['address'];
$exp=$_POST['exp'];
$price=$_POST['price'];


$query = mysqli_query("insert into item_info(shop_id,shop_name, item id, address, curr_price,quantity,days_remain) values (1,'$name', '$email','$price', '$contact', '$exp','$address')");

echo "<br/><br/><span>Data Inserted successfully...!!</span>";
header("Location: ../../inesert.html");
?>