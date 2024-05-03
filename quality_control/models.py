from django.db import models
from tasks.models import Project, Task
from django.core import validators

class BugReport(models.Model):
    BUG_STATUSES = [('New', 'Новый'), ('In progress', 'В работе'), ('Completed', 'Завершён')]
    
    title = models.CharField(max_length=100)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        related_name='bug_reports',
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        related_name='bug_reports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length = 50,
        choices = BUG_STATUSES,
        default = 'Новый'
    )

    priority = models.PositiveIntegerField(
        default = 5,
        validators = [validators.MaxValueValidator(5)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    REQUEST_STATUSES = [('consideration', 'Рассмотрение'), ('accepted', 'Принято'), ('rejected', 'Отклонено')]
    
    title = models.CharField(max_length=100)
    
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        related_name='feature_request',
        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        related_name='feature_request',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length = 50,
        choices = REQUEST_STATUSES,
        default = 'Новый'
    )

    priority = models.PositiveIntegerField(
        default = 5,
        validators = [validators.MaxValueValidator(5)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    