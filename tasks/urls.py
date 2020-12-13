from django.urls import path
from .views import ListOfTasks, NewTask


urlpatterns = [
    path('', ListOfTasks.as_view(), name='tasks'),
    path('new_task/', NewTask.as_view(), name='new_task'),
]
