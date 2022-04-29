from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'portifilio/index.html')


# def about(request):
#     return render(request, 'portifilio/about.html')
#
#
# def skills(request):
#     return render(request, 'portifilio/skills.html')
#
#
# def projects(request):
#     return render(request, 'portifilio/projects.html')

def contact(request):
    if request.method == 'POST':
        formemail = request.POST['contact__Email']
        subject = request.POST['contact__Subject']
        message = request.POST['contact__Message']
        if formemail != "" and message != "":
            send_mail(subject=subject, message=message, from_email=formemail,
                      recipient_list=['omar.atef.2001@gmail.com', formemail])
            messages.success(request, 'Thanks for contacting us')
            context = {
                'message': message,
            }
            return main(request)
        else:
            messages.success(request, 'Please fill the Contact section.')
            context = {
                'message': message,
            }
            return main(request)
    else:
        return main(request)
