from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Word(models.Model):
    value = models.CharField(max_length=30)
    translate = models.CharField(max_length=30)
    meaning = models.CharField(max_length=510)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, default=None)

    @classmethod
    def get_words(cls, limit: int = 30):
        return cls.objects.all()[:limit]

    def __str__(self):
        return self.value
