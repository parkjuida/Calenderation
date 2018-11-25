from django.db import models
from django.utils import timezone
from Account.models import Chronicler


class TimeStampModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Diary(TimeStampModel):
    author = models.ForeignKey(Chronicler, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title