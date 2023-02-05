from django.test import TestCase
from .views import VoiceRecordView
import pytest 
import speech_recognition as sr
import wave
# Create your tests here.

def test_if_wav_is_processed():
    r = sr.Recognizer()

    hellow=sr.AudioFile(VoiceRecordView.TEMP_DIR)
    with hellow as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Text: "+s)
    except Exception as e:
        print("Exception: "+str(e))
    
    obj=wave.open(VoiceRecordView.TEMP_DIR, 'rb')
    print(obj)