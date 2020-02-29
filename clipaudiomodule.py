from pydub import AudioSegment


class AudioTrimmer:
    def detect_leading_silence(self, sound, silence_threshold=-50.0, chunk_size=10):
            trim_ms = 0  # ms
            while sound[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold:
                trim_ms += chunk_size
            return trim_ms

    def trim_audio(self, speech_file):
        sound = AudioSegment.from_file(speech_file, format="wav")
        start_trim = self.detect_leading_silence(sound)
        end_trim = self.detect_leading_silence(sound.reverse())
        duration = len(sound)
        trimmed_sound = sound[start_trim:duration - end_trim]
        file_handle = trimmed_sound.export("trimmed.wav", format="wav")