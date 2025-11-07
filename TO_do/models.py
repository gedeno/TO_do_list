from django.db import models

# Create your models here.
class ppl(models.Model):
    task = models.CharField(max_length=300)
    cond = models.CharField(max_length =34) 