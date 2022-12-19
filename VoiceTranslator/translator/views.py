from django.shortcuts import render
from .forms import TranslateForm
from django.views.generic.base import View
from deepl.translator_engine import Translator, TextTranslated
from django.http import HttpRequest
# Create your views here.


class TranslateView(View):

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