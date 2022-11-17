from django.shortcuts import render
from .forms import TranslateForm
from django.views.generic.base import View
from deepl.translator_engine import Translator, TextTranslated
# Create your views here.


class TranslateView(View):

    def get(self, request):
        return render(request, "translator/translator.html", {'form': TranslateForm()})

    def post(self, request):
        print('#' * 30)
        print(type(request.POST["source_text"]), 
        request.POST["source_language"],
        type(request.POST["target_language"]))
        t = Translator("5cce4070-ebdd-5a51-373d-d2f094b4c760:fx")
        result=t.translate(request.POST["source_text"], 
        request.POST["source_language"],
        request.POST["target_language"])

        form = TranslateForm(
            initial={'source_language': result.source_language,
            'source_text': result.source_text,
            'target_language': result.target_language,
            'target_text': result.translated_text})

        return render(request, "translator/translator.html", {'form': form})
