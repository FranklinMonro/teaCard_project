from django.contrib import admin
from .models import OperationModel, UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(OperationModel)
