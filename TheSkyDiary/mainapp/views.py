from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Request, Skies, Customer
from django.core.mail import send_mail, EmailMessage
from datetime import datetime
import smtplib
import email.utils
from email.mime.text import MIMEText
from .forms import PostCustomerForm

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
        sky = Skies.objects.get(diary_date__year=sky_year, diary_date__month=sky_month, diary_date__day=sky_day)

        url = 'localhost:8000/prints/?inquiry_id=' + str(inquiry.id)

        email = EmailMessage(
            'Your Sky Diary Proof',
            'Your Sky Diary is attached below!  To purchase a print, click this link: ' + url,
            'yourskydiary@gmail.com',
            [inquiry.email],
        )
        email.attach_file('./uploaded_files/images/'+sky.proof_filename())
        email.send()
        inquiry.email_sent = True

    else:
        email_admin = EmailMessage(
            'Sky Diary Needed for:',
            'year:' + sky_year + ' month:' + sky_month + ' day:' + sky_day + ' for: ' + inquiry.email,
            'yourskydiary@gmail.com',
            ['sprread@gmail.com'],
        )
        email_admin.send()

    return render(request, 'TheSkyDiary/thankyou.html')


def prints(request):
    inquiry_id = request.GET['inquiry_id']
    # look inquiry with this id
    inquiry = Request.objects.get(id=inquiry_id)
    inquiry_date = inquiry.diary_date
    # pass that data to the template to be rendered

    if request.method == 'POST':
        print("buysky req:", request)
        form = PostCustomerForm(request.POST)
        if form.is_valid():
                customer = form.save(commit=False)
                customer.save()
        return render(request, 'TheSkyDiary/Bootstrap.html')
    else:
        form = PostCustomerForm()
    return render(request, 'TheSkyDiary/prints.html', {'inquiry_date': inquiry_date, 'form': form})





def Bootstrap(request):

    return render(request,'TheSkyDiary/Bootstrap.html')