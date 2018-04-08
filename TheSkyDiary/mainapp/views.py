from django.shortcuts import render
from django.http import HttpResponse
from . models import Request, Skies
from django.core.mail import send_mail, EmailMessage
from datetime import datetime
# for sending email: https://superuser.com/questions/1292420/sending-an-email-from-python-using-local-python-smtp-server
import smtplib
import email.utils
from email.mime.text import MIMEText

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
        # # Create our message.
        # msg = MIMEText('The body of your message.')
        # msg['To'] = email.utils.formataddr(('Recipient Name', 'recipient@example.com'))
        # msg['From'] = email.utils.formataddr(('Your Name', 'yourname@yourdomain.com'))
        # msg['Subject'] = 'Your Subject'

        #server = smtplib.SMTP()
        #server.connect('localhost', 25)
        # try:
        #     server.sendmail('jackson.dh.reed@gmail.com', ['sprread@gmail.com'], msg.as_string())
        # finally:
        #     server.quit()
        # subject = "Your Sky Diary Proof"
        # text = "Please find your Sky Diary attached"
        # email_to = 'jackson.dh.reed@gmail.com'
        sky = Skies.objects.get(diary_date__year=sky_year, diary_date__month=sky_month, diary_date__day=sky_day)
        email = EmailMessage(
            'Your Sky Diary Proof',
            'Your Sky Diary is attached below!  To purchase a print, click this link',
            'yourskydiary@gmail.com',
            ['jackson.dh.reed@gmail.com'],
        )
        email.attach(sky.watermarked_proof.url)
        email.send()
        # mail.attach(sky.watermarked_proof.url)
        # send_mail(subject, text, 'yourskysiary@gmail.com', [email_to], fail_silently=False,)
        #mail = send_mail(subject, text, ['yourskysiary@gmail.com'], [email], fail_silently=False,)

        # path to images:/Users/jacksonreed/PycharmProjects/TheSkyDiary/TheSkyDiary/uploaded_files/images/
        #mail.send()
    return render(request, 'TheSkyDiary/thankyou.html')


def prints(request):

    return render(request, 'TheSkyDiary/prints.html')