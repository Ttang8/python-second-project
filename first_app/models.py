from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AccessRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
