from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'portifilio/index.html')


def about(request):
    return render(request, 'portifilio/about.html')


def skills(request):
    return render(request, 'portifilio/skills.html')


def projects(request):
    return render(request, 'portifilio/projects.html')


def contact(request):
    return render(request, 'portifilio/contact.html')
