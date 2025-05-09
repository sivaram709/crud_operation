from django.db import models

class ContactModel(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=250)
    birthday=models.DateTimeField()

    def __str__(self):
        return self.name

"""class Meta:
    verbose_name=("ContactModel")
    verbose_name_plural=("ContactModel")"""


  
