

from django.urls import path
from .views import MailCreate

app_name = 'mails'

urlpatterns = [

    path('', MailCreate, name='mail_create'),
    
]
