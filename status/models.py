from django.db import models
from datetime import datetime

class StatusModel(models.Model):
    content = models.TextField(max_length=300)
    date = models.DateTimeField(default=datetime.now)
