import sounddevice as sd
import struct
import pvporcupine
import assistant  # Your assistant logic

def listen_hotword():
    access_key = "ZIZcj+rEmRY118oZ2rRtjJgus9hk0hvDjqN3HNALO5bAXARUFoqHUA=="
    porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis"])

    def audio_callback(indata, frames, time, status):
        pcm = struct.unpack_from("h" * len(indata), indata)
        if porcupine.process(pcm) >= 0:
            print("Wake word detected.")
            assistant.run_assistant()

    with sd.InputStream(channels=1, samplerate=porcupine.sample_rate,
                        blocksize=porcupine.frame_length, dtype='int16',
                        callback=audio_callback):
        print("Say 'jarvis' to activate.")
        while True:
            pass

listen_hotword()

