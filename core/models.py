from django.db import models


class Suggestion(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    data = models.CharField(max_length=168)
    create_date = models.DateTimeField()
