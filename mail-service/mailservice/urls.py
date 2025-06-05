from django.contrib import admin
from app.views import send_emails, get_emails
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', send_emails, name='send_emails'),
    path('get/', get_emails, name='get_emails'),
]