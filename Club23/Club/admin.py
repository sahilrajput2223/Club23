from django.contrib import admin
from .models import Bookclub, Payment, News
# Register your models here.

admin.site.register(Bookclub)
admin.site.register(Payment)
admin.site.register(News)