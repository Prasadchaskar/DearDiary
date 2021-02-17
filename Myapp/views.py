from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Entry
from . forms import EntyForm
# Create your views here.
def home(request):
    entry = Entry.objects.all().order_by('-post_date')
    return render(request,'index.html',{'entry':entry})

def add(request):
    if request.method == "POST":
        form = EntyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =EntyForm()

    return render(request, 'add.html',{'form':form})