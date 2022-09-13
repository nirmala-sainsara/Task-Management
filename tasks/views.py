from django.shortcuts import render,redirect
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic import RedirectView
from .forms import LoginForm, RegisterForm, TaskForm
from tasks.models import Task
from tasks.mixins import LoginRequired
from django.db.models import Q
from django.contrib import messages

# serializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from tasks.models import Task
from  .serializers import TaskDetailSerializer, TaskSerializer
from rest_framework import generics


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'tasks/login.html'
    def get_success_url(self):
        return reverse('tasks:task_list')


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('tasks:login')

class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class TaskCreateView(generic.TemplateView):
  template_name = 'tasks/task_create.html'
  form_class = TaskForm
  success_message = "Task Created Successfully"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = TaskForm()
    return context

  def get_success_url(self):
    return reverse("tasks:task_list")

  def post(self, request, *args, **kwargs):
    post_request = (self.request.POST,)
    form = TaskForm(*post_request)
    if form.is_valid():
        task = form.save()
        user = self.request.user
        task.user = user
        task.save()
        return redirect(self.get_success_url())

    else:
        context = {
            "form":TaskForm
        }
        return self.render_to_response(context)

class TaskListView(generic.ListView):
  template_name = 'tasks/task_list.html'

  def get_queryset(self):
    if self.request.user.is_authenticated:
      queryset = Task.objects.filter(user=self.request.user.id).order_by('-start_date', '-end_date')
    else:
      queryset = Task.objects.none
    
    if self.request.GET.get('q'):
        query = self.request.GET.get('q')
        queryset = queryset.filter(
            Q(task_name__icontains=query)
            |Q(task_description=query)
        )
    
    if self.request.GET.get('task_name'):
        queryset = queryset.order_by('-task_name')

    if self.request.GET.get('start_date'):
        queryset = queryset.order_by('-start_date')

    if self.request.GET.get('end_date'):
        queryset = queryset.order_by('-end_date')

    return queryset


class TaskDetailView(generic.DetailView):
  template_name = 'tasks/task_detail.html'
  model = Task


class UpdateTaskView(LoginRequired, generic.UpdateView):
    template_name = 'tasks/edit_task.html'
    model = Task
    pk_url_kwarg = 'pk'
    fields = ['task_name', 'task_description', 'end_date']

    def get_success_url(self):
        return reverse('tasks:task_list',)
       

class DeleteTaskView(LoginRequired, generic.DeleteView):
    template_name = 'tasks/delete_task.html'
    model = Task
    pk_url_kwarg = 'pk'
    
    success_message = "Task Deleted successfully"

    def get_success_url(self):
        # messages.info(self.request, "Task Deleted successfully")
        return reverse_lazy('tasks:task_list')

# api views
class MarkTaskCompletedAPIView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_marked_completed_task = True
        task.save()
        data = TaskSerializer(task).data
        return Response(data)


class MarkTaskPendingAPIView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_marked_completed_task = False
        task.save()
        data = TaskSerializer(task).data
        return Response(data)


class TaskListApiView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

