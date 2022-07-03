from django.db import models

# Create your models here.
from users.models import CustomUser


class Workspace(models.Model):
    name = models.TextField(max_length=255)
    users = models.ManyToManyField(CustomUser)
    owner_id = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.TextField(max_length=255)
    workspace = models.ForeignKey(
        Workspace, related_name='projects', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Ticket(models.Model):
    STATUS = [
        ('TD', 'To do'),
        ('IP', 'In progress'),
        ('DO', 'Done')
    ]
    name = models.TextField(max_length=255)
    desc = models.TextField(max_length=255)
    status = models.CharField(max_length=2, choices=STATUS, default='TD')
    project = models.ForeignKey(
        Project, related_name='tickets', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    content = models.TextField(max_length=255)
    ticket = models.ForeignKey(
        Workspace, related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content
