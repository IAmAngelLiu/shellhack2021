from django.contrib import admin

# Register your models here.

from .models import Employee
from .models import Data
from .models import Points

admin.site.register(Employee)
admin.site.register(Data)
admin.site.register(Points)

