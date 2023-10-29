<p>Audio To Text</p>

<form method="post" action="index.php">
  <textarea type="text" name="value" cols="40" rows="10" placeholder="Informe o texto a ser resumido"></textarea>
  <input name="submit" type="submit" value="Enviar">
</form>

<?php
  if(isset($_POST['submit'])) {
      $value = $_POST['value'];

      $curl = curl_init();

      curl_setopt_array($curl, array(
        CURLOPT_URL => 'http://127.0.0.1:8000', // URL do servidor audioToText.py
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS => $value,
        CURLOPT_HTTPHEADER => array(
          'Content-Type: text/plain'
        ),
      ));
      $response = curl_exec($curl);
      curl_close($curl);

      $result = json_decode($response, true);
      echo $result;
  }
?>

