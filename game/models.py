from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    id = int
    creationDate = datetime.date
    login = models.TextField()
    password = models.TextField()
 
    def _str_(self):
        return self.title
