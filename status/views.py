from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import StatusModel
from .forms import StatusForm
from datetime import datetime

def status(request):
    page_title = "How are you?"
    status = StatusModel.objects.all().values()

    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = StatusModel()
            status.content = form.cleaned_data['your_status']
            status.date = datetime.now()
            status.save()
            return HttpResponseRedirect('/status')
    else:
        form = StatusForm()

    response = {
        "title" : page_title,
        'form' : form,
        'status' : status,
    }
    return render(request, 'status.html', response)

def about(request):
    page_title = "About Ama"
    response = {"title" : page_title}
    return render(request, 'about.html', response)

def delete(request):
    status = StatusModel.objects.all()
    for item in status:
        item.delete()
    return redirect('/status')
