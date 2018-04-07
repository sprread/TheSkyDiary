from django.shortcuts import render
from django.http import HttpResponse
from . models import Request, Skies
from django.core.mail import send_mail, EmailMessage
from datetime import datetime


# Create your views here.

def index(request):
    return render(request, 'TheSkyDiary/index.html')



def thankyou(request):
    inquiry = Request() #request is the class from my model
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

    # check to see if I have that date, and if I don't, send email to myself.
    if Skies.objects.filter(diary_date__year=sky_year,
                      diary_date__month=sky_month,
                      diary_date__day=sky_day).count() >= 1:
        subject = "Your Sky Diary Proof"
        text = "Please find your Sky Diary attached"
        email = 'jackson.dh.reed@gmail.com'
        mail = EmailMessage(subject, text, ['sprread@gmail.com'], [email])
        sky = Skies.objects.get(diary_date__year=sky_year, diary_date__month=sky_month, diary_date__day=sky_day)
        mail.attach(sky.watermarked_proof.url)
        # mail.send()
    return render(request, 'TheSkyDiary/thankyou.html')


