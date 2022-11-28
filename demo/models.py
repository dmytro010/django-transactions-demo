from django.db import models

"""Create Demo model with id field"""
class Demo(models.Model):

    class Meta:
        db_table = 'demo'