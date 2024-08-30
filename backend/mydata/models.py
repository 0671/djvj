from django.db import models
from django.conf import settings

# Create your models here.
class Mydata(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mydatas',on_delete=models.CASCADE)
    key = models.CharField(max_length=225)
    property_name  = models.CharField(max_length=225)
    property_value = models.CharField(max_length=225)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['-id'] 

    def __str__(self) -> str:
        return self.key