from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')

# Apply low pass filter
beat_low = beat.low_pass_filter(2000)
beat_low.export('beat_low.wav')

# Listen to only left speaker
beat_left = beat_low.pan(-1)
beat_left.export('beat_left.wav')

# Listen to only right speaker
beat_right = beat_low.pan(1)
beat_right.export('beat_right.wav')

# Mix of all effects
beat_final = beat_left + beat_right + beat_low
beat_final.export('beat_final.wav')
