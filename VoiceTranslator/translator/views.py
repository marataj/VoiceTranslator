from django.shortcuts import render
from .forms import TranslateForm
from django.views.generic.base import View
from deepl.translator_engine import Translator, TextTranslated
from django.http import HttpRequest
import base64
import speech_recognition as sr
import wave
import librosa
import soundfile
from pathlib import Path
import moviepy.editor as moviepy
from pydub import AudioSegment
import os
import ffmpeg
# Create your views here.


class TranslateView(View):
    #TEMP_DIR = Path(r"C:/temp")

    def get(self, request):
        return render(request, "translator/translator.html", {'form': TranslateForm()})

    def post(self, request):
        if "submit-btn" in request.POST:
            t = Translator("5cce4070-ebdd-5a51-373d-d2f094b4c760:fx")
            result=t.translate(request.POST["source_text"], 
            request.POST["source_language"],
            request.POST["target_language"])

            form = TranslateForm(
                initial={'source_language': result.source_language,
                'source_text': result.source_text,
                'target_language': result.target_language,
                'target_text': result.translated_text})
        
        elif "swap-btn" in request.POST:
            form = self.swap_langs(request)

        return render(request, "translator/translator.html", {'form': form})


    def swap_langs(self, request: HttpRequest) -> TranslateForm:
        return TranslateForm({'source_language': request.POST["target_language"],
            'source_text': request.POST["source_text"],
            'target_language': request.POST["source_language"],
            'target_text': request.POST["target_text"]})


class VoiceRecordView(View):
    
    input_path = "temp.wav"
    output_path = "out.wav"
    def get(self, request):
        return render(request, "translator/voice_rec.html", {'typ': "get"})

    def post(self, request):
        blob=request.POST["record_field"]
        blob=blob.split(",")
        blob=blob[1]
        blob=base64.decodebytes(bytes(blob, 'UTF-8'))
             
        wav_file = open(self.input_path, "wb")
        wav_file.write(blob)
   
        wav_file.close()
        
        os.system(f"ffmpeg -i {self.input_path} {self.output_path}")

        r = sr.Recognizer()

        hellow=sr.AudioFile(self.output_path)
        with hellow as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio, language="pl-PL")
            print("Text: "+s)
        except Exception as e:
            print("Exception: "+str(e))
        
        os.unlink(self.input_path)
        os.unlink(self.output_path)
        
        return render(request, "translator/voice_rec.html", {'typ': "post"})