from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset, load_from_disk

processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")
model.config.forced_decoder_ids = None

ds = load_dataset("/home/antonio/projetos/hugginface/servers", data_files="audio-junior.ogg")
sample = ds['train'][0]['audio']

input_features = processor(sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt").input_features 

predicted_ids = model.generate(input_features)

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

print(transcription[0])
