<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-black">

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
  }
?>

<main id="content" role="main" class="relative max-w-3xl px-4 sm:px-6 lg:px-8 flex flex-col justify-center sm:items-center mx-auto w-full h-full before:absolute before:top-0 before:left-1/2 before:bg-[url('../svg/component/squared-bg-element-.svg')] before:bg-no-repeat before:bg-top before:w-full before:h-full before:-z-[1] before:transform before:-translate-x-1/2">
  <div class="text-center py-8 px-4 sm:px-6 lg:px-8">
    <h2 class="mt-1 sm:mt-3 text-4xl font-bold text-white sm:text-6xl">
      <span class="bg-clip-text bg-gradient-to-tr from-blue-600 to-purple-400 text-transparent">Audio To Text AI</span>
    </h2>

    <h1 class="text-lg text-white sm:text-2xl">
      Transcreva seus áudios em texto
    </h1>
    <form method="post" action="audioToText.php">
      <div class="mt-8 space-y-4">
        <div>
          <label for="hs-cover-with-gradient-form-name-1" class="sr-only">Link do áudio</label>
          <div class="relative">
            <input type="text" name="value" id="hs-cover-with-gradient-form-name-1" class="py-3 ps-11 pe-4 block w-full bg-white/[.03] border-white/20 text-white placeholder:text-white rounded-md text-sm focus:border-white/30 focus:ring-white/30 sm:p-4 sm:ps-11" placeholder="Link do áudio (.ogg ou .flac)">
            <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none z-20 ps-4">
              <svg class="h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
              </svg>
            </div>
          </div>
        </div>

        <div class="grid">
          <button type="submit" name="submit" class="py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md bg-white/10 border border-transparent font-medium text-white hover:bg-white/20 focus:outline-none focus:ring-2 focus:ring-white/30 transition-all text-sm sm:p-4">
            Transcrever
            <svg class="w-3 h-3" width="16" height="16" viewBox="0 0 16 16" fill="none">
              <path d="M5.27921 2L10.9257 7.64645C11.1209 7.84171 11.1209 8.15829 10.9257 8.35355L5.27921 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
        </div>

        <?php if(!empty($result)): ?>
          <div class="bg-white">
            <div class="relative">
                <ul class="mt-8 space-y-8">
                  <!-- Chat Bubble -->
                  <li class="max-w-4xl py-4 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 sm:gap-x-4">
                    <img src="image/wal-e.jpeg" class="flex-shrink-0 w-[2.375rem] h-[2.375rem] rounded-full" width="38" height="38" viewBox="0 0 38 38" fill="none" xmlns="http://www.w3.org/2000/svg">

                    <div class="space-y-3">
                      <h2 class="text-left font-medium text-gray-800 ">
                        Aqui está sua transcrição
                      </h2>
                      <h2 class="text-left text-gray-800">
                          <?php echo $result['text']; ?>
                      </h2>
                      <div class="space-y-1.5">
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        <?php endif; ?>

      </div>
    </form>
  </div>
</main>

<footer class="absolute bottom-0 inset-x-0 text-center py-5">
  <div class="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8">
    <p class="text-sm text-white/50">© 2023 AudioToText <a class="text-white font-medium hover:text-white/80" href="/">Home</a></p>
  </div>
</footer>

<script src=" https://cdn.jsdelivr.net/npm/@preline/preline@1.0.0/dist/hs-ui.bundle.min.js "></script>
</body>
</html>
