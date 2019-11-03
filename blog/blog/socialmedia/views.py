from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Post




def home(request):
    obj = Post.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'wall.html', context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signin.html'


