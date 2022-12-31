from django.shortcuts import render
from .forms import TranslateForm
from django.views.generic.base import View
from deepl.translator_engine import Translator, SpeechRecognizer
# Create your views here.

class TranslateView(View):
    
    def get(self, request):
        return render(request, "translator/translator.html", {'form': TranslateForm()})

    def post(self, request):
        source_text = request.POST.get("source_text")
        source_language = request.POST.get("source_language")
        target_language = request.POST.get("target_language")
        target_text = request.POST.get("target_text")
        record = request.POST["record_field"]

        if "submit-btn" in request.POST:
            result=Translator.translate(source_text, source_language, target_language)

            form = TranslateForm(
                initial={'source_language': result.source_language,
                'source_text': result.source_text,
                'target_language': result.target_language,
                'target_text': result.translated_text})
        
        elif "swap-btn" in request.POST:
            form = TranslateForm({'source_language': target_language,
            'source_text': source_text,
            'target_language': source_language,
            'target_text': target_text})
            
        elif "record_field" in request.POST:
            output = SpeechRecognizer.analyze(record, source_language)
            result=Translator.translate(output,source_language, target_language)

            form = TranslateForm(
                initial={'source_language': result.source_language,
                'source_text': result.source_text,
                'target_language': result.target_language,
                'target_text': result.translated_text})
            

        return render(request, "translator/translator.html", {'form': form})

