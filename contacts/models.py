from django.db import models

class Contact(models.Model):
    nameContact = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.IntegerField()
    message = models.CharField(max_length = 200)

    def __str__(self):
        string = self.nameContact
        return string
