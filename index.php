<?php 
      header('Content-type: text/html; charset=utf-8')
?>
<html>
<head>
<title>Hello!</title>
</head>
<body>
<b>Number of Visitors: <?php echo exec("python numvisitors.py");
 ?>
</b>

<?php exec("python addtovisitors.py"); ?>
<?php $time = localtime();
      $hour = $time[2];
      echo shell_exec("python parsetime.py $hour");       
?>
</body>
</html>
