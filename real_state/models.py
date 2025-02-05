from django.db import models
from core.models import Country, Province, City
# Create your models here.


class HouseCase(models.Model):
    HOUSE_STATUS_SELL = 's'
    HOUSE_STATUS_RENT = 'r'
    HOUSE_STATUS = [
        (HOUSE_STATUS_SELL, 'فروش'),
        (HOUSE_STATUS_RENT, 'اجاره'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    full_address = models.TextField()
    post_code = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='house_cases')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='house_cases')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='house_cases')
