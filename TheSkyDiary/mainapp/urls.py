from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'skydiary'
urlpatterns = [
    path('', views.index, name='index'),
    path('thankyou/', views.thankyou, name="thankyou"),
    path('prints/', views.prints, name="prints"),
    path('reserve/', views.reserve, name="reserve"),
]
