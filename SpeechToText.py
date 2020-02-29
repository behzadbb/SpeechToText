import speech_recognition as sr
import clipaudiomodule as ca

class SpeechToText:
    def trim_audio(self):
        trimmer = ca.AudioTrimmer()
        # Saves trimmed audio to trimmed.wav
        trimmer.trim_audio('converted.wav')
        
    def speechToText(self, speechData):
            audio = sr.AudioData(speechData,16000,2)
            r = sr.Recognizer()
            text = r.recognize_google(audio,language="fa-IR")
            return text