from django.http import HttpResponse


from django.http     import HttpResponse
from django.template import loader
from .models          import foods, category

def index(request):


    x = foods.objects.all()
    template = loader.get_template('templates/main/index.html')

    context = {
        'data': x,
    }

    return HttpResponse(template.render(context, request))
