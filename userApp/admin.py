from django.contrib import admin
from .models import User
# Register your models here.


# admin.site.register(User)

"""by default it given but if we implemented custome user model so it disable"""
"""for enable object.model to user permission so it add permisiion in admin panel  write follwing code"""
@admin.register(User)
class usermodelAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions')

