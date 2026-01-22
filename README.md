# NLP-speech-to-text

Convert speech to text using HuggingFace, comparing Wav2Vec2 versus OpenAI Whisper.

## Data

Speech samples included a subset of sentences recorded for this study:

Reuter, T., Sullivan, M., & Lew-Williams, C. (2021). Look at that: Spatial deixis reveals experience- related changes in prediction. Language Acquisition. https://doi.org/10.1080/10489223.2021.1932905

Audio for lab-based experiments are very clean. So this *should* be an easy transcription task.

## Conclusion

Comparing Whisper and Wav2Vec2 reveals some important advantages for the Whisper model:

1. Performance
   - Approximately 20% faster transcription speed
   - Potential for further optimization

2. Accuracy
   - Better handling of singular and plural distinctions (e.g., "apple" vs. "apples")
   - More accurate spelling (e.g., "doggies" vs. "DOGGIYS")

3. Nuanced Output
   - Better inclusion of punctuation, indicating emphasis
   - May be better suited for NLP tasks like sentiment analysis

Whisper may be best for use cases requiring:
- High transcription accuracy
- Extracting appropriate punctuation
- Downstream sentiment analysis steps
- Real-time or near-real-time processing
