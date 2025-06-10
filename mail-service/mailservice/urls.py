from django.contrib import admin

from app.views import send_emails, get_emails
from django.urls import path
from app.viewSet.status_view_set import StatusViewSet
from app.viewSet.email_view_set import EmailViewSet
from app.viewSet.task_view_set import TaskViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', send_emails, name='send_emails'),
    path('get/', get_emails, name='get_emails'),
    path('statuses/', StatusViewSet.as_view({'get': 'list'}), name='statuses'),
    path('emails/', EmailViewSet.as_view({'get': 'list'}), name='emails'),
    path('tasks/', TaskViewSet.as_view({'get': 'list'}), name='tasks'),
]