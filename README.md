## PLN HugginFace

### Iniciando app audioToText


> #### Whisper
> Whisper is a pre-trained model for automatic speech recognition (ASR) and speech translation. Trained on 680k hours of labelled data, Whisper models demonstrate a strong ability to generalise to many datasets and domains without the need for fine-tuning.

A aplicação audioToText recebe um arquivo de áudio e retorna o texto transcrito.

```bash
uvicorn audioToText:app
php -S 127.0.0.1:8001 audioToText.php
```
