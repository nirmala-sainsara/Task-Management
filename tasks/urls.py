from django.urls import path
from django.conf.urls import include
from tasks.views import DeleteTaskView, LoginView, LogoutView, MarkTaskPendingAPIView, RegisterView, TaskCreateView, TaskDetailApiView, TaskDetailView, TaskListApiView, TaskListView, UpdateTaskView, MarkTaskCompletedAPIView
app_name="tasks"

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('task/',TaskCreateView.as_view(), name='task_create'), 
    path('task_list/',TaskListView.as_view(), name='task_list'), 
    path('task_detail/<int:pk>/',TaskDetailView.as_view(), name='task_detail'), 
    path('task_edit/<int:pk>',UpdateTaskView.as_view(), name='editTask'),
    path('task_delete/<int:pk>',DeleteTaskView.as_view(), name='deleteTask'),
    path("mark_task_complete/<int:pk>", MarkTaskCompletedAPIView.as_view(), name="mark_task_complete_api"),
    path("task/list", TaskListApiView.as_view(), name="task_list_api"),
    path("task/detail/<int:pk>", TaskDetailApiView.as_view(), name="task_detail_api"),
    path("mark_task_pending/<int:pk>", MarkTaskPendingAPIView.as_view(), name="mark_task_pending_api"),

]
