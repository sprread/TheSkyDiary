from django.shortcuts import render
from django.http import HttpResponse
from . models import Request
from django.core.mail import send_mail, EmailMessage


# Create your views here.

def index(request):
    return render(request, 'TheSkyDiary/index.html')

#look at todolab
def thankyou(request):
    inquiry = Request()
    sky_day = request.POST['sky-day']
    if int(sky_day) < 10:
        sky_day = '0' + sky_day
    sky_month = request.POST['sky-month']
    month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09','October': '10', 'November': '11', 'December': '12'}
    sky_month = month_dict[sky_month]
    sky_year = request.POST['sky-year']
    inquiry.diary_date = sky_year + '-' + sky_month + '-' + sky_day
    inquiry.email_sent = False
    inquiry.email = request.POST['email']
    inquiry.save()

    #check to see if I have that date, and if I don't, send email to myself.
    # mail = EmailMessage(subject, text, ['EMAIL_ADDRESS'], [email])
    # mail.attach(image1.name, attach.read(), attach.content_type)
    # mail.send()
    #look at Matthew's doc on email like the SMTP settings.

    return render(request, 'TheSkyDiary/thankyou.html')


