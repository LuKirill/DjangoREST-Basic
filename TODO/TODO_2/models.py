from django.db import models

class Project(models.model):
    name = models.CharField(max_length=32)
    repo_link = models.URLField()

class Users(models.Model):
    project = models.OneToOneField(Project, related_name='user_set', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    email = models.EmailField()

class TODO(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    date = models.DateField()
    author = models.OneToOneField(Users, on_delete=models.CASCADE)
    active = models.BooleanField()

    def __str__(self):
        return self.title