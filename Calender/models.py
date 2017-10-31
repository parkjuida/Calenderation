from django.db import models
from django.utils import timezone

class Diary(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(null=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title