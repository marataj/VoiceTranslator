from django.shortcuts import render
from .forms import TranslateForm
from .models import Translates, Language
from django.views.generic.base import View
from django.views.generic import ListView
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
            if result.translated_text != "":
                Translates(
                    user = request.user,
                    source_language = Language.objects.filter(translate_short=result.source_language)[0].language,
                    source_text = result.source_text,
                    target_language = Language.objects.filter(translate_short=result.target_language)[0].language,
                    target_text = result.translated_text
                ).save()
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
            if result.translated_text != "":
                Translates(
                    user = request.user,
                    source_language = Language.objects.filter(translate_short=result.source_language)[0].language,
                    source_text = result.source_text,
                    target_language = Language.objects.filter(translate_short=result.target_language)[0].language,
                    target_text = result.translated_text
                ).save()

            form = TranslateForm(
                initial={'source_language': result.source_language,
                'source_text': result.source_text,
                'target_language': result.target_language,
                'target_text': result.translated_text})
            
        print(request.user)
        return render(request, "translator/translator.html", {'form': form})

class HistoryView(ListView):
    paginate_by=5
    template_name: str="translator/history.html"
    model = Translates
    context_object_name = "Translates"

    def get_queryset(self):
        qs =  super().get_queryset()
        data = qs.filter(user=self.request.user).order_by("-date")
        return data