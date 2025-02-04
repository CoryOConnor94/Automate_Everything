from pydub import AudioSegment

original = AudioSegment.from_wav('beat.wav')

# Reverse original audio file
reversed_audio = original.reverse()
reversed_audio.export('reversed.wav')

# Extract first 2 seconds of original
first_two = original[0:2000]
first_two.export('first_two.wav')

# Merge original and reversed
merged = original + reversed_audio
merged.export('merged.wav')

# Merge original and reversed and add second of silence
merged_with_silence = original + AudioSegment.silent(1000) + reversed_audio
merged_with_silence.export('merged_with_silence.wav')

# Multiple audio files
merged_multiplied = original * 2 + AudioSegment.silent(1000) + reversed_audio
merged.export('merged_with_silence.wav')

# Higher decibels of audio
reversed_louder = reversed_audio + 15
