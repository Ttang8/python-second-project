from django.contrib import admin
from first_app.models import User, AccessRecord

# Register your models here.
admin.site.register(User)
admin.site.register(AccessRecord)
