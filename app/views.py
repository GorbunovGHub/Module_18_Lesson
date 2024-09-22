from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    title = 'Мой сайт'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'index.html', context)

# class Index2(TemplateView):
#     template_name = 'index2.html'
