import base64
import os
from pathlib import Path

import speech_recognition as sr


class SpeechRecognizer:
    """
    Class responsible for processing the audio file and speech recognition.

    """

    TEMP_DIR = str(os.getenv("TEMP_DIR"))
    TEMP_WAV = Path(TEMP_DIR, "temp.wav")
    OUT_WAV = Path(TEMP_DIR, "out.wav")

    @classmethod
    def analyze(cls, blob_base64: str, lang: str = "PL") -> str:
        """
        Function responsible for analysis of the audio file and speech recognition.

        Parameters
        ----------
        blob_base64 : str
            .wav file as a base64.
        lang : str, optional
            The source language of the speech, by default "PL"

        Returns
        -------
        str
            Text recognized from the audio file.

        """
        try:
            cls.TEMP_WAV.unlink()
            cls.OUT_WAV.unlink()
        except FileNotFoundError:
            print("File not found.")
        blob_base64 = blob_base64.split(",")[1]
        blob = base64.decodebytes(bytes(blob_base64, "UTF-8"))
        with open(cls.TEMP_WAV, "wb") as wav_file:
            wav_file.write(blob)

        os.system(f"ffmpeg -i {cls.TEMP_WAV} {cls.OUT_WAV}")

        r = sr.Recognizer()
        with sr.AudioFile(str(cls.OUT_WAV)) as source:
            audio = r.record(source)

        try:
            text = r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            return ""

        return text
