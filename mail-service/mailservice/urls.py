from django.contrib import admin
from django.urls import path
from app.views import send_emails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', send_emails, name='send_emails'),
]