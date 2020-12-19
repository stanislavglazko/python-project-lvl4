from django.urls import path
from .views import ListOfTasks, NewTask, NewStatus
from .views import ListOfStatuses, UpdateStatus, DeleteStatus
from .views import tasklist, NewTag
# from django.views.generic.base import TemplateView


urlpatterns = [
    path('', tasklist, name='tasks'),
    path('new_task/', NewTask.as_view(), name='new_task'),
    path('new_status/', NewStatus.as_view(), name='new_status'),
    path('new_tag/', NewTag.as_view(), name='new_tag'),
    path('statuses/',
         ListOfStatuses.as_view(), name='statuses'),
    path('statuses/<int:pk>/update_status/',
         UpdateStatus.as_view(), name='update_status'),
    path('statuses/<int:pk>/delete_status/',
         DeleteStatus.as_view(), name='delete_status'),
]
