from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='provinces')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
