from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Paper(models.Model):

    author = models.OneToOneField(User,on_delete=models.CASCADE)
    paper_title = models.CharField(max_length=400)
    paper_published_date = models.DateField()
    paper_publisher = models.CharField(max_length=400)
    paper_proof = models.FileField(upload_to='papers-proof')

    def __str__(self):
        return self.paper_title
