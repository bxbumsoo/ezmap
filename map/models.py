from django.db import models

# Create your models here.


class Yongloc(models.Model):
    no = models.AutoField(primary_key=True)
    model = models.TextField()
    modelcode = models.TextField()
    loc0 = models.TextField()
    loc1 = models.TextField()

    class Meta:
        managed = False
        db_table = 'yongloc'
