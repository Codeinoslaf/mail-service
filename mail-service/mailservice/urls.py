from django.contrib import admin

from app.views import send_emails
from django.urls import path
from app.viewSet.status_view_set import StatusViewSet
from app.viewSet.email_view_set import EmailViewSet
from app.viewSet.task_view_set import TaskViewSet
from app.viewSet.recipient_view_set import RecipientViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', send_emails, name='send_emails'),


    path('statuses/', StatusViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='statuses'),
    path('statuses/<int:pk>/', StatusViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    }), name='status-detail'),


    path('emails/', EmailViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='emails'),
    path('emails/<int:pk>/', EmailViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    }), name='email-detail'),


    path('tasks/', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='tasks'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    }), name='task-detail'),


    path('recipients/', RecipientViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='recipient'),
    path('recipients/<int:pk>/',RecipientViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    }), name='recipient' )
]