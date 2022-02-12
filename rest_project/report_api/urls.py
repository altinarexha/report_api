from django.urls import path
from . import views
from .views import TaskReport

urlpatterns = [
	path('', views.list, name="list"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<int:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<int:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<int:pk>/', views.taskDelete, name="task-delete"),
	path('tasks/report', TaskReport.as_view(), name='report'),

]
