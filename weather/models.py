from django.db import models

class CityWeather(models.Model):
    name = models.CharField(max_length=500, unique=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
