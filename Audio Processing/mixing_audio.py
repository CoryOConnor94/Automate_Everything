from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')
sax = AudioSegment.from_wav('sax.wav')

# Print length of audio files
print(len(beat), len(sax))

# Extend length of beat file so matches sax length
beat_two = beat * 2
beat_two.export('beat_two.wav')

# Mixed two audio files
mixed = beat_two.overlay(sax)
mixed.export('mixed.wav')

# Final mix
final_mix = beat_two + mixed * 2 + beat_two + sax
final_mix.export('final.wav')
