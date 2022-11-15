from django.shortcuts import render
from .forms import TranslateForm
from django.views.generic.base import View
# Create your views here.


class TranslateView(View):

    def get(self, request):
        return render(request, "translator/translator.html", {'form': TranslateForm()})

    def post(self, request):

        form = TranslateForm(
            initial={'target_text': request.POST['input_text']})

        return render(request, "translator/translator.html", {'form': form})
