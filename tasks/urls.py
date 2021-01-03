from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.tasklist, name='tasks'),
    path('new_task/', views.NewTask.as_view(), name='new_task'),
    path('<int:pk>/update_task/',
         views.UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete_task/',
         views.DeleteTask.as_view(), name='delete_task'),
    path('new_status/', views.NewStatus.as_view(), name='new_status'),
    path('new_tag/', views.NewTag.as_view(), name='new_tag'),
    path('tags/',
         views.ListOfTags.as_view(), name='tags'),
    path('tags/<int:pk>/update_tag/',
         views.UpdateTag.as_view(), name='update_tag'),
    path('tags/<int:pk>/delete_tag/',
         views.DeleteTag.as_view(), name='delete_tag'),
    path('statuses/',
         views.ListOfStatuses.as_view(), name='statuses'),
    path('statuses/<int:pk>/update_status/',
         views.UpdateStatus.as_view(), name='update_status'),
    path('statuses/<int:pk>/delete_status/',
         views.DeleteStatus.as_view(), name='delete_status'),
]
