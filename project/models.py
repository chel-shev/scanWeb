from django.db import models
import django.utils.timezone

class PC(models.Model):
    class Meta:
        db_table = "computer"

    id = models.AutoField(primary_key=True)
    pc = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    distro = models.CharField(max_length=100)
    isa = models.CharField(max_length=100)
    kernel = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    memory = models.FloatField()
    ram = models.FloatField()
    swap = models.FloatField()
    high = models.FloatField()
    crit = models.FloatField()
    limit = models.IntegerField()

class Data(models.Model):
    class Meta:
        db_table = "data"

    id = models.AutoField(primary_key=True)
    used_memory = models.IntegerField()
    ram = models.IntegerField()
    cpu_0 = models.IntegerField()
    cpu_1 = models.IntegerField()
    cpu_2 = models.IntegerField()
    cpu_3 = models.IntegerField()
    temp_0 = models.IntegerField()
    temp_1 = models.IntegerField()
    temp_2 = models.IntegerField()
    temp_3 = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    id_pc = models.ForeignKey(PC, on_delete=models.CASCADE)
