from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('Email'), unique=True)


class Task(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        related_name='user_task',
        null=True
    )

    task_name = models.CharField(
        "Task Name",
        max_length=100,
    )

    task_description = models.TextField(
        "Task Description",
        null=True,
        blank=True
    )

    start_date = models.DateField(
        auto_now_add=True
    )

    end_date = models.DateField()

    is_marked_completed_task = models.BooleanField(
        default=False
    )
   
