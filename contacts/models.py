from django.db import models


class Contact(models.Model):
    """
    Contact: record a contact made in the website
    """
    nameContact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    message = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200, default="0.0.0.0")

    def __str__(self):
        """
        Returns the name of the contact
        """
        string = self.nameContact
        return string
