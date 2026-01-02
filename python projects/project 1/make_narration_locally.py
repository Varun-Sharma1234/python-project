
"""
Generate professional male-style narration from script using offline TTS.

Usage:
    python make_narration_locally.py

Outputs:
    IR_Sensor_Arduino_Narration.wav
    IR_Sensor_Arduino_Narration.mp3 (if pydub+ffmpeg available)
"""
import os
import pyttsx3

# Load script text
script_path = "IR_Sensor_Arduino_Narration_Script.txt"
with open(script_path, "r", encoding="utf-8") as f:
    script = f.read().strip()

wav_out = "IR_Sensor_Arduino_Narration.wav"
mp3_out = "IR_Sensor_Arduino_Narration.mp3"

engine = pyttsx3.init()
# Professional pacing
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate * 0.95))
engine.setProperty('volume', 1.0)

# Try to choose a male English voice if available
try:
    voices = engine.getProperty('voices')
    chosen = None
    for v in voices:
        name = (getattr(v, "name", "") or "").lower()
        vid = (getattr(v, "id", "") or "").lower()
        if ("male" in name or "male" in vid) and ("en" in name or "english" in name or "en_" in vid):
            chosen = v.id
            break
    if not chosen and voices:
        # Fallback: first English voice
        for v in voices:
            name = (getattr(v, "name", "") or "").lower()
            vid = (getattr(v, "id", "") or "").lower()
            if ("en" in name or "english" in name or "en_" in vid):
                chosen = v.id
                break
    if chosen:
        engine.setProperty('voice', chosen)
except Exception:
    pass

# Synthesize to WAV
engine.save_to_file(script, wav_out)
engine.runAndWait()

print("WAV created:", os.path.exists(wav_out), wav_out, os.path.getsize(wav_out) if os.path.exists(wav_out) else 0)

# Try convert WAV -> MP3 (optional)
try:
    from pydub import AudioSegment
    audio = AudioSegment.from_wav(wav_out)
    audio.export(mp3_out, format="mp3")
    print("MP3 created:", os.path.exists(mp3_out), mp3_out, os.path.getsize(mp3_out) if os.path.exists(mp3_out) else 0)
except Exception as e:
    print("MP3 conversion skipped (install pydub + ffmpeg to enable). Error:", e)
