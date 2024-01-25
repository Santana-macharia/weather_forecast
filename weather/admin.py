from django.contrib import admin
from .models import CityWeather

admin.site.register(CityWeather)

admin.site.site_header = 'Weather Forecast'  # This will change the header text
admin.site.site_title = 'Weather Forecast'    # This will change the browser tab title
admin.site.index_title = 'Weather Forecast'   # This will change the main title on the admin index page
