# NLP-speech-to-text

Convert speech to text using HuggingFace, comparing Wav2Vec2 versus OpenAI Whisper

## Data

Speech samples included a subset of sentences recorded for this study:

Reuter, T., Sullivan, M., & Lew-Williams, C. (2021). Look at that: Spatial deixis reveals experience- related changes in prediction. Language Acquisition. https://doi.org/10.1080/10489223.2021.1932905

Audio for lab-based experiments are very clean. So this *should* be an easy transcription task.

## Conclusion

IMO, Whisper beats Wav2Vec2 in at least 3 ways:

1. More performant.

- Transcribed 20% faster.

- Future enhancements could increase speed.

2. More accurate.

- Transcribed "apple" versus "apples" correctly.

- Spelled "doggies" correctly as "doggies", not as "DOGGIYS".

3. More nuanced.

- Transcribed 3 sentences with emphatic punctuation (! instead of .)

- Punctuation indicates emphasis and emotion, useful for downstream sentiment analysis.
