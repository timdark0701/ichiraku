from django.http     import HttpResponse
from django.template import loader
from django.shortcuts import render
from feedback.models import  FeedBack

def index(request):
    return render(request, 'templates/mainpage/index.html')


def list(request):
    x = FeedBack.objects.all()
    template = loader.get_template('templates/mainpage/feeds.html')

    context = {
        'data': x,
    }

    return HttpResponse(template.render(context, request))
