from django.shortcuts import render
from .forms import Literature_form


def Literture_view(request,*args, **kwargs):
    form=Literature_form(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        'form':form,
    }
    return render(request, "mylitform.html", context)
# Create your views here.
