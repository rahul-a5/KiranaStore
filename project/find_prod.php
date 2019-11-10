<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Colorlib Templates">
    <meta name="author" content="Colorlib">
    <meta name="keywords" content="Colorlib Templates">

    <!-- Title Page-->
    <title>Results Page</title>

    <!-- Icons font CSS-->
    <link href="vendor/mdi-font/css/material-design-iconic-font.min.css" rel="stylesheet" media="all">
    <link href="vendor/font-awesome-4.7/css/font-awesome.min.css" rel="stylesheet" media="all">
    <!-- Font special for pages-->
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i" rel="stylesheet">

    <!-- Vendor CSS-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <link href="vendor/select2/select2.min.css" rel="stylesheet" media="all">
    <link href="vendor/datepicker/daterangepicker.css" rel="stylesheet" media="all">

    <!-- Main CSS-->
    <link href="css/mainn.css" rel="stylesheet" media="all">
</head>

<body>
    <div class="page-wrapper bg-blue p-t-100 p-b-100 font-robo">
        <div class="wrapper wrapper--w680">
<?php
//session_start();

// initializing variables
$shop_list = array();

// connect to the database
$db = mysqli_connect('localhost', 'root', '', 'myproject');

// REGISTER USER
$item = $_POST['srch'];
// echo "rahul";
$sql="select curr_price,address,shop_name from item_info where item_id=\"".$item."\"";
if ($result=mysqli_query($db, $sql)) {
    while ($row=mysqli_fetch_row($result)) {
        //printf("%d %s %s\n", $row[0], $row[1], $row[2]);
        array_push($shop_list, $row);
    }
}
//var_dump($shop_list);
mysqli_free_result(($result));


//echo $shop_list[0][1];


for ($x = 0; $x < count($shop_list); $x++) 
{
?>
<div class="card card-1">
    <div class="card-heading"></div>
    <div class="card-body">
            <h2 align='center'>SHOP : <?php echo $shop_list[$x][2] ?></h2>
            <br>
            
            <br>
            <div align='center'>
                <button class='button spc'>Price: <i><?php echo $shop_list[$x][0] ?></i></button>
            </div>
            <div align='center' style="color:blue">
                <p class='button spc'>Address  : <?php echo $shop_list[$x][1] ?></p>
            </div>
            <div align='center'>
                <button class='button button2 spc'>Expiry</button>
            </div> 
    </div>
</div>

<?php 
} 
?>

<script src="vendor/jquery/jquery.min.js"></script>
    <!-- Vendor JS-->
    <script src="vendor/select2/select2.min.js"></script>
    <script src="vendor/datepicker/moment.min.js"></script>
    <script src="vendor/datepicker/daterangepicker.js"></script>

    <!-- Main JS-->
    <script src="js/global.js"></script>

</body><!-- This templates was made by Colorlib (https://colorlib.com) -->

</html>
<!-- end document-->
