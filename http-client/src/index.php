<html>
<head>
    <title>App page</title>
</head>
<body>
    <h2>Rank matrix</h2>
    <h3>Parametrs:</h3>
//Вычисление ранга матрицы.
    <?php
    if (isset($_POST['first']) && isset($_POST['second']) && isset($_POST['third'])){
        $myCurl = curl_init();
    curl_setopt_array($myCurl, array(
        CURLOPT_URL => 'http://nginxserver/api/'.$_POST['first'].'/'.$_POST['second'].'/'.$_POST['third'],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
    ));
    $response = curl_exec($myCurl);
    curl_close($myCurl);
    $json = json_decode($response,true);
    echo "Ответ на Ваш запрос: ".$json['result'];
//        echo "Ответ на Ваш запрос: ".$response;
    }
    ?>
    <form action="index.php" method="post">
    <label for="Columns">Columns </label>
    <input type="number" name="first" id="first" required>
    <label for="Rows">Rows </label>
    <input type="number" name="second" id="second" required>
    <label for="Arguments">Arguments </label>
    <input type="string" name="third" id="third" required>
    <input type="submit" value="RUN!">
    </form>