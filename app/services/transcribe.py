from faster_whisper import WhisperModel
from app.config import WHISPER_MODEL_SIZE

# Loaded once when this module is first imported — NOT inside the function.
# Loading the model (reading weights off disk) takes a few seconds, so we
# don't want to repeat that cost on every single request.
_model = WhisperModel(WHISPER_MODEL_SIZE, device="cpu", compute_type="int8")


def transcribe_audio(file_path: str) -> list[dict]:
    """
    Transcribes an audio file and returns timestamped segments, e.g.:
        [{"start": 0.0, "end": 4.2, "text": "Okay let's get started."}, ...]

    We return segments (not one big string) because:
    1. Timestamps let you later show "this answer came from 12:45 in the meeting"
    2. The chunker (next step) groups these segments intelligently instead of
       having to re-split a flat block of text
    """
    segments, info = _model.transcribe(file_path, beam_size=5)

    result = []
    for seg in segments:
        result.append({
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip(),
        })

    return result