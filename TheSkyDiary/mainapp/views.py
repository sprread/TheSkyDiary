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
    if (int(sky_day) < 10):
        sky_day = '0' + sky_day


    sky_month = request.POST['sky-month']
    if sky_month == 'January':
        sky_month = '01'
    if sky_month == 'February':
        sky_month = '02'
    if sky_month == 'March':
        sky_month = '03'
    if sky_month == 'April':
        sky_month = '04'
    if sky_month == 'May':
        sky_month = '05'
    if sky_month == 'June':
        sky_month = '06'
    if sky_month == 'July':
        sky_month = '07'
    if sky_month == 'August':
        sky_month = '08'
    if sky_month == 'September':
        sky_month = '09'
    if sky_month == 'October':
        sky_month = '10'
    if sky_month == 'November':
        sky_month = '11'
    if sky_month == 'December':
        sky_month = '12'
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


