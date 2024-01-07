from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=130)
    last_name=models.CharField(max_length=130)
    email=models.CharField(max_length=130)
    subject=models.CharField(max_length=130)
    mess=models.CharField(max_length=130)
    date=models.DateField()


    def __str__(self):
        return self.first_name

class subscribe(models.Model):
    Email=models.EmailField(null=True)

    def __str__(self):
        return self.Email


