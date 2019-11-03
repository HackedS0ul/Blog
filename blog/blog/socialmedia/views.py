from django.shortcuts import render
from .models import Post



def home(request):
    obj = Post.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'wall.html', context)

def userRegister(request):
    return render(request, 'signin.html')


