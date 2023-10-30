from transformers import  pipeline

pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v2",
    generate_kwargs={"language": "br", "task": "transcribe"},
    device="cpu",
    use_fast=True
)

pipe('http://127.0.0.1:3000/audio-junior.ogg', batch_size=10, return_timestamps=True, chunk_length_s=30, stride_length_s=(4, 2))
# res = pipe('http://127.0.0.1:3000/audio-junior.ogg', batch_size=10, return_timestamps=True, chunk_length_s=30, stride_length_s=(4, 2))
# res = pipe('http://127.0.0.1:3000/audio-mae-3min.ogg')

print(res['text'])
