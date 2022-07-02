from django.db import models



# Create your models here.
PROFESSION_CHOICES = (
  ('professional','Professional'),
  ('hobbiest','Hobbiest'),
  ('instructor','Instructor'),
)

class SignUp(models.Model):
  prof = models.CharField(max_length=15, choices=PROFESSION_CHOICES, default='green')

#class ProfModel(models.Model):
#  prof = models.CharField(max_length=15, #choices=PROFESSION_CHOICES, default='green')



