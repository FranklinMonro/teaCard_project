from django.db import models

# Create your models here.
class OperationModel(models.Model):
    wo_number = models.CharField(max_length = 7)
    parts_qty = models.CharField(max_length = 4)
    wo_operation = models.CharField(max_length = 5)
    start_date = models.DateField()
    compl_date = models.DateField()
class UserProfileInfo(models.Model):

    def __str__(self):
        return self.user.username
