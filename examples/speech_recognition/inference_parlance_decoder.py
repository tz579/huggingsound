import torch
from huggingsound import SpeechRecognitionModel, ParlanceLMDecoder

device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 1
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device=device)
audio_paths = ["/path/to/sagan.mp3", "/path/to/asimov.wav"]

# The LM format used by the LM decoders is the KenLM format (arpa or binary file).
# You can download some LM files examples from here: https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english/tree/main/language_model
lm_path = "path/to/your/lm_files/lm.binary"

# To use this decoder you'll need to install the Parlance's ctcdecode first (https://github.com/parlance/ctcdecode)
decoder = ParlanceLMDecoder(model.token_set, lm_path=lm_path, alpha=2, beta=1, beam_width=100)

transcriptions = model.transcribe(audio_paths, batch_size=batch_size, decoder=decoder)

print(transcriptions)
