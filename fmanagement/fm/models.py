from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length = 40, primary_key= True)
    contactno = models.IntegerField(max_length = 10,blank=True)
    academic_qualifiacation = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    subjects_profeciencies = models.TextField(blank=True)
    
    def __str__(self):
        return full_name
