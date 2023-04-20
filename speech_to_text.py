# transcribe a .wav file with Wav2Vec2
# import NLP libraries
import librosa
import torch
# import Wav2Vec tokenizer
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import IPython.display as display
display.Audio("taken_clip.wav", autoplay=True)
# import Wav2Vec pretrained model
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
# load the audio file (.wav format, 16 kHz sampling rate)
audio, rate = librosa.load("taken_clip.wav", sr = 16000)
# confirm audio is loaded as an array, dtype=float32
# confirm sampling rate is 16 kHz
audio
rate
# get input_values
input_values = tokenizer(audio, return_tensors = "pt").input_values
input_values
# store logits (non-normalized prediction values)
logits = model(input_values).logits
logits
# store prediction
prediction = torch.argmax(logits, dim = -1)
prediction
# pass the prediction to the tokenzer to decode and generate the transcription
transcription = tokenizer.batch_decode(prediction)[0]
# print transcription
print(transcription)