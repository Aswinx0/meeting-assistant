from app.services.transcribe import transcribe_audio

print("Starting transcription...")
result = transcribe_audio("data/audio/sample.mp3")
print(f"Number of segments returned: {len(result)}")
for seg in result:
    print(seg)
print("Done.")