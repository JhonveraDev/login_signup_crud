from django.db import models

class Client(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    address = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    email = models.EmailField(blank = True)

    def __str__(self):
        self.name