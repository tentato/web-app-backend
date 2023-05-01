from django.db import models

class Tab(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=100000, null=True)

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.CharField(max_length=100000, null=True)
    tag = models.CharField(max_length=255, default='informacja')
    posting_date = models.DateTimeField(null=False)