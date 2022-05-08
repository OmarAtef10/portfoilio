from django.shortcuts import render, redirect
from .forms import MessageForm


# Create your views here.

def main(request):
    form = MessageForm()
    if request.method == 'POST':
        print("Posted!!")
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            print("Working!!!!!!!")
    context = {'form': form}
    return render(request, 'portifilio/index.html', context)
