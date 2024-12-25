import io

from pydub import AudioSegment


def resample_audio(audio_bytes, original_sample_rate, target_sample_rate):
    resampled_audio = AudioSegment.from_raw(
        io.BytesIO(audio_bytes),
        sample_width=2,
        frame_rate=original_sample_rate,
        channels=1,
    ).set_frame_rate(target_sample_rate)
    return resampled_audio.raw_data
# Modified on Tue Jan 21 11:33:50 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:34:01 PM +01 2025
print('Debug message')
