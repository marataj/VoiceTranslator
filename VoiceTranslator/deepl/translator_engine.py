import requests
from enum import Enum
import base64
import speech_recognition as sr
import os
from dataclasses import dataclass

__all__ = ["TextTranslated, Translator, SpeechRecognizer"]

available_languages={
    "Polski": "PL",
    "English": "EN"
}

@dataclass
class TextTranslated:
    source_text: str 
    source_language: str
    target_language: str 
    translated_text: str


class Translator:
    API_KEY="5cce4070-ebdd-5a51-373d-d2f094b4c760:fx"
    API_ENDPOINT = "https://api-free.deepl.com/v2/translate"
    @classmethod
    def translate(cls, source_text: str, source_language: str, target_language: str) -> TextTranslated:
        raw_result = requests.get(
            cls.API_ENDPOINT,
            params={
                "auth_key": cls.API_KEY,
                "target_lang": target_language,
                "text": source_text,
                "source_lang": source_language
            },
        )

        return TextTranslated(source_text, source_language, target_language, raw_result.json()['translations'][0]['text'])

class SpeechRecognizer:
    TEMP_PATH = "temp/temp.wav"
    OUT_PATH = "temp/out.wav"

    @classmethod
    def analyze(cls, blob_base64: str, lang: str = "PL") -> str:
        os.unlink(cls.TEMP_PATH)
        os.unlink(cls.OUT_PATH)
        blob_base64=blob_base64.split(",")[1]
        blob=base64.decodebytes(bytes(blob_base64, 'UTF-8'))
             
        with open(cls.TEMP_PATH, "wb") as wav_file:
            wav_file.write(blob)
        
        os.system(f"ffmpeg -i {cls.TEMP_PATH} {cls.OUT_PATH}")

        r = sr.Recognizer()
        with sr.AudioFile(cls.OUT_PATH) as source:
            audio = r.record(source)
        
        try:
            text = r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            print("No speech recognized")
            return ""
                
        return text
