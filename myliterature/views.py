from django.http import HttpResponse
from django.shortcuts import render
from .forms import LiteratureForm


def literture_view(request,*args, **kwargs):
    form=LiteratureForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=LiteratureForm()
    context={
        'form':form,
    }
    return render(request, "mylitform.html", context)

def home(request,*args, **kwargs):
    return HttpResponse("<h1>Hello world<br>Welcome to my webpage</h1>")
