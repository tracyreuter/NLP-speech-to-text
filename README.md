# NLP-speech-to-text

Convert speech to text using HuggingFace, comparing Wav2Vec2 versus OpenAI Whisper

## Data

Speech samples included a subset of sentences recorded for this study:

Reuter, T., Sullivan, M., & Lew-Williams, C. (2021). Look at that: Spatial deixis reveals experience- related changes in prediction. Language Acquisition. https://doi.org/10.1080/10489223.2021.1932905

Audio for lab-based experiments are very clean. So this *should* be an easy transcription task.

## Conclusion

The comparison between Whisper and Wav2Vec2 reveals several key advantages of the Whisper model:

1. Performance
   - Approximately 20% faster transcription speed
   - Potential for further performance optimization

2. Accuracy
   - Better handling of singular/plural forms (e.g., "apple" vs. "apples")
   - More accurate spelling (e.g., "doggies" vs. "DOGGIYS")

3. Nuanced Output
   - Enhanced punctuation handling including emphatic marks
   - Better preservation of emotional context through punctuation
   - Improved potential for downstream tasks like sentiment analysis

These differences make Whisper particularly suitable for applications requiring:
- High transcription accuracy
- Preservation of emotional context
- Integration with sentiment analysis pipelines
- Real-time or near-real-time processing
