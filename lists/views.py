from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {
        # use dict.get to provide a default value
        'new_item_text': request.POST.get('item_text', ''),
    })
