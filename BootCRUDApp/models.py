from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GarbageSellModel(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, default="")
    price = models.IntegerField(default=0)
    imageURL = models.CharField(max_length=800, default="")
    # foreignkeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "This collector is: " + str(self.name)
