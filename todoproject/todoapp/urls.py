from . import views
from django.urls import path
app_name='todoapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:task_id>/',views.delete_task,name='delete_task'),
    path('update/<int:task_id>/',views.update_task,name='update_task'),

]