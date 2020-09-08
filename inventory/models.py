from django.db import models

# Create your models here.
class Device(models.Model): #name of the table
    type = models.CharField(max_length=100, blank=False) # name of the column
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('OUT OF ORDER', 'Item is not working properly'),
        ('IN-USE', 'Item is being used by employee')
    )
    status = models.CharField(max_length=15, choices=choices, default="AVAILABLE") # available, sold, restocking
    issues = models.CharField(max_length=100, default="No issues")
    user = models.CharField(max_length=100, default="USER")
    location = models.CharField(max_length=10, default="LOCATION")

    def __str__(self):
        return 'Type : {0} Price : {1} User : {2} Location : {3}'.format(self.type, self.price, self.user, self.location)


    class Meta:
        abstract = True


class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass

class Equipment(Device):
    pass
