from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'caption': 'ShrekDjango'
    }
    return render(request, 'my_app/index.html', data)

def data(request):
    return render(request, 'my_app/data.html')

def test(request):
    return render(request, 'my_app/test.html')

def four(request):
    return render(request, 'my_app/four.html')
