from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    faculty_name = models.CharField(max_length=70)
    designation = models.CharField(max_length=200)
    employee_id = models.PositiveBigIntegerField()
    email = models.EmailField()
    contact_number = models.PositiveBigIntegerField()
    date_of_joining = models.DateField(auto_created=True)


    def __str__(self):
        return self.faculty_name