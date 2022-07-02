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
            return redirect('contact')
    context = {'form': form}
    return render(request, 'portifilio/index.html', context)


def mailSent(requset):
    return render(requset, 'portifilio/contact.html')
