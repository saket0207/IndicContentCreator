from elevenlabs import generate, play, voices


def generate_audio():
    available_voices = voices()
    print(available_voices)
    audio = generate(
        text="Hello! I'm from the past!",
        voice="Rachel",
        model="eleven_monolingual_v1"
    )

    play(audio)
    print(audio)
    return audio
